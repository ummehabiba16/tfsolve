---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "During DMA (HLDA = 1) both ends are driven at once: a DMA write (I/O -> memory, W/R' = 1) needs WS = I/O read and WD = memory write; a DMA read (memory -> I/O, W/R' = 0) needs RS = memory read and RD = I/O write. So WS = WD = HLDA AND W/R', RS = RD = HLDA AND (W/R')'; when HLDA = 0 the normal MEMR/MEMW/IOR/IOW come from M/IO' and W/R'."
sources: ["Brey, The Intel Microprocessors, Sec. 13-1 (DMA read and DMA write, HOLD/HLDA, control-signal generation in a DMA system)"]
---
**Definitions (Brey):** a **DMA write** moves data **from I/O to memory**; a **DMA read** moves data **from memory to I/O**. In a DMA cycle both the source and the destination are active in the **same** bus cycle (the data goes straight from one to the other), so the usual one-command-at-a-time decoding of M/$\overline{IO}$ cannot be used.

| Signal | Meaning | Device command |
|:--|:--|:--|
| WS | source of a DMA write | **I/O read** (I/O puts data on the bus) |
| WD | destination of a DMA write | **memory write** |
| RS | source of a DMA read | **memory read** |
| RD | destination of a DMA read | **I/O write** |

**Logic** (active-high, assumption W/$\overline{R}$ = 1 for a write)

$$WS = WD = HLDA \cdot W/\overline{R}, \qquad RS = RD = HLDA \cdot \overline{W/\overline{R}}$$

To use the same command lines for normal processor cycles too (HLDA = 0, where M/$\overline{IO}$ chooses memory or I/O), each command is the OR of its CPU term and its DMA term:

$$MEMW\ (WD) = \overline{HLDA}\cdot M \cdot W + HLDA \cdot W$$

$$IOR\ (WS) = \overline{HLDA}\cdot \overline{M} \cdot \overline{W} + HLDA \cdot W$$

$$MEMR\ (RS) = \overline{HLDA}\cdot M \cdot \overline{W} + HLDA \cdot \overline{W}$$

$$IOW\ (RD) = \overline{HLDA}\cdot \overline{M} \cdot W + HLDA \cdot \overline{W}$$

(M = M/$\overline{IO}$, W = W/$\overline{R}$.)

**Truth table**

| HLDA | M/$\overline{IO}$ | W/$\overline{R}$ | WD (MEMW) | WS (IOR) | RS (MEMR) | RD (IOW) | Cycle |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| 0 | 1 | 1 | 1 | 0 | 0 | 0 | CPU memory write |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | CPU memory read |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | CPU I/O write |
| 0 | 0 | 0 | 0 | 1 | 0 | 0 | CPU I/O read |
| 1 | x | 1 | **1** | **1** | 0 | 0 | **DMA write** (I/O $\to$ memory) |
| 1 | x | 0 | 0 | 0 | **1** | **1** | **DMA read** (memory $\to$ I/O) |

**Circuit**

```text
 W/R' ----+--------------------------+-----------------+
          |                          |                 |
         [>o] W'                     |                 |
          |                          |                 |
 HLDA ----+--[AND]-- HLDA.W ---------+--> to OR of WD and WS
          +--[AND]-- HLDA.W' -----------> to OR of RS and RD
         [>o] HLDA'
          |
 M/IO' ---+--[AND3: HLDA', M,  W ]--+
             [AND3: HLDA', M', W']--|  each AND3 output is ORed with
             [AND3: HLDA', M,  W']--|  the matching DMA term:
             [AND3: HLDA', M', W ]--+
   WD = OR(HLDA'.M.W,   HLDA.W)     WS = OR(HLDA'.M'.W', HLDA.W)
   RS = OR(HLDA'.M.W',  HLDA.W')    RD = OR(HLDA'.M'.W,  HLDA.W')
```

Real buses use active-low commands ($\overline{MWTC}$, $\overline{IORC}$, $\overline{MRDC}$, $\overline{IOWC}$): invert each output (use NOR gates instead of OR). During DMA, M/$\overline{IO}$ from the floating processor is ignored because HLDA = 1 removes the CPU terms.
