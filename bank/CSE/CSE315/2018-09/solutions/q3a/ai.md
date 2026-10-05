---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Mode 2 (bidirectional bus on Port A), e.g. linking two computers or a processor to a disk/GPIB controller. Inputs: WR', RD' (CPU) and ACK', STB' (peripheral); outputs: OBF', IBF, INTR and Port A. WR' falling -> INTR low; WR' rising -> OBF' low; ACK' low -> OBF' high and Port A drives the data; STB' low -> IBF high (data latched); STB' rising -> INTR high; RD' falling -> INTR low; RD' rising -> IBF low."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 2 bidirectional operation and timing)", "Hall, Microprocessors and Interfacing, Ch. 9 (8255 mode 2)"]
---
**(i) Mode and application**

The diagram has both output handshake signals ($\overline{WR}$, $\overline{OBF}$, $\overline{ACK}$) and input handshake signals ($\overline{STB}$, IBF, $\overline{RD}$) on the **same Port A**, so it is **Mode 2: strobed bidirectional bus I/O** (Port A only).

*Applications:* a bidirectional 8-bit bus between two computers or processors (e.g. a host and a slave controller), or an interface to a peripheral that both sends and receives, such as a disk controller or an IEEE-488 (GPIB) bus.

**(ii) Inputs, outputs and their relation**

- **Inputs to the 82C55:** $\overline{WR}$ and $\overline{RD}$ (from the CPU), $\overline{ACK}$ and $\overline{STB}$ (from the peripheral).
- **Outputs from the 82C55:** $\overline{OBF}$ and IBF (to the peripheral), INTR (to the CPU), and Port A (driven only while $\overline{ACK}$ is low).

| # | Input change | $\to$ | Output change |
|:-:|:--|:-:|:--|
| 1 | $\overline{WR}\downarrow$ (CPU writes Port A) | $\to$ | INTR $\downarrow$ (old request cleared) |
| 2 | $\overline{WR}\uparrow$ | $\to$ | $\overline{OBF}\downarrow$ (output buffer full) |
| 3 | $\overline{STB}\downarrow$ (peripheral strobes data in) | $\to$ | IBF $\uparrow$ (data latched in Port A input latch) |
| 4 | $\overline{STB}\uparrow$ | $\to$ | INTR $\uparrow$ (input data ready, if INTE2 = 1) |
| 5 | $\overline{ACK}\downarrow$ (peripheral asks for output data) | $\to$ | $\overline{OBF}\uparrow$ and **Port A drives the output data** |
| 6 | $\overline{ACK}\uparrow$ | $\to$ | Port A returns to high impedance (and INTR $\uparrow$ for output, if INTE1 = 1) |
| 7 | $\overline{RD}\downarrow$ (CPU reads Port A) | $\to$ | INTR $\downarrow$ |
| 8 | $\overline{RD}\uparrow$ | $\to$ | IBF $\downarrow$ (input buffer empty) |

```text
WR'    ----+    +--------------------------------------------------
           |____|
OBF'   ----------+                      +--------------------------
                 |______________________|
INTR   -----+               +-------------------------+
            |_______________|                         |____________
ACK'   --------------------------------+     +---------------------
                                       |_____|
STB'   --------------+     +---------------------------------------
                     |_____|
IBF                   +-------------------------------------+
       _______________|                                     |______
PortA  ............<=========>.........<=====>.....................
                     in                  out
RD'    ----------------------------------------------+     +-------
                                                     |_____|
```

Arrows (cause $\to$ effect): $\overline{WR}\downarrow \to$ INTR$\downarrow$; $\overline{WR}\uparrow \to \overline{OBF}\downarrow$; $\overline{STB}\downarrow \to$ IBF$\uparrow$; $\overline{STB}\uparrow \to$ INTR$\uparrow$; $\overline{ACK}\downarrow \to \overline{OBF}\uparrow$ and output data on Port A; $\overline{RD}\downarrow \to$ INTR$\downarrow$; $\overline{RD}\uparrow \to$ IBF$\downarrow$.

*Note:* the given figure does not show INTR falling at the falling edge of $\overline{RD}$; by the Mode 1 input rule (which Mode 2 follows) it should (row 7).
