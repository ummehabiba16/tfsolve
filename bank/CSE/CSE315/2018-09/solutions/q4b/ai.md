---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Use a 74LS257 (quad 2-to-1 MUX with three-state outputs): select = IO/M' (8088) or M/IO' (8086); inputs RD', WR' and +5 V make MEMR', MEMW', IOR', IOW'; its output enable is driven by HLDA so the lines float during DMA and the DMA controller (8237) drives them. HOLD from the DMA controller, HLDA back to it; HLDA also floats the address/data buffers."
sources: ["Brey, The Intel Microprocessors, Sec. 13-1 (HOLD and HLDA, generating MEMR, MEMW, IOR, IOW with a 74LS257 in a DMA system)"]
---
In a DMA system the bus control lines must be driven by the **processor** normally and by the **DMA controller** (e.g. 8237) during DMA. The 8088 gives only $\overline{RD}$, $\overline{WR}$ and IO/$\overline{M}$, so a circuit is needed to make the four system commands $\overline{MEMR}$, $\overline{MEMW}$, $\overline{IOR}$, $\overline{IOW}$, and to release them when HLDA = 1.

**Circuit: 74LS257 (quad 2-to-1 multiplexer with three-state outputs)**

```text
                 74LS257
            +-----------------+
  RD'  ---->| 1A          1Y  |----> MEMR'
  +5V  ---->| 1B              |
  WR'  ---->| 2A          2Y  |----> MEMW'
  +5V  ---->| 2B              |
  +5V  ---->| 3A          3Y  |----> IOR'
  RD'  ---->| 3B              |
  +5V  ---->| 4A          4Y  |----> IOW'
  WR'  ---->| 4B              |
  IO/M' --->| S (select)      |      S = 0: A inputs, S = 1: B inputs
  HLDA ---->| OE' (G)         |      HLDA = 1: outputs float
            +-----------------+
```

**Operation**

| HLDA | IO/$\overline{M}$ | $\overline{MEMR}$ | $\overline{MEMW}$ | $\overline{IOR}$ | $\overline{IOW}$ |
|:-:|:-:|:--|:--|:--|:--|
| 0 | 0 (memory) | $\overline{RD}$ | $\overline{WR}$ | 1 | 1 |
| 0 | 1 (I/O) | 1 | 1 | $\overline{RD}$ | $\overline{WR}$ |
| 1 | x | Z (driven by 8237) | Z | Z | Z |

1. The DMA controller requests the bus with **HOLD**. The processor finishes its bus cycle, floats its own pins and answers **HLDA = 1**.
2. HLDA disables the 74LS257 outputs (high impedance) and also the address latches/data transceivers' output enables, so the **8237** can drive the address bus and $\overline{MEMR}$/$\overline{MEMW}$/$\overline{IOR}$/$\overline{IOW}$ directly. For a DMA read it asserts $\overline{MEMR}$ and $\overline{IOW}$ together; for a DMA write, $\overline{IOR}$ and $\overline{MEMW}$.
3. When the transfer ends the 8237 drops HOLD, the processor drops HLDA, and the 74LS257 drives the commands again.

For the **8086**, use M/$\overline{IO}$ as the select input with the A/B inputs swapped (M/$\overline{IO}$ = 1 means memory).
