---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Minimum mode (MN/MX' = 1, +5 V): single-processor system; the 8086 itself generates the bus control signals (M/IO', RD', WR', ALE, DEN', DT/R', INTA', HOLD/HLDA). Maximum mode (MN/MX' = 0, ground): multiprocessor/coprocessor systems; pins 24-31 give status S0'-S2', QS0/QS1, RQ'/GT0', RQ'/GT1', LOCK', and an 8288 bus controller decodes the status into MRDC', MWTC', IORC', IOWC', INTA', ALE, DEN, DT/R'. Selected by the MN/MX' pin (pin 33)."
sources: ["MHE 8086 Hardware Specifications slides (MN/MX pin, minimum and maximum mode pins)", "Brey, The Intel Microprocessors, Sec. 9-1 and 9-6 (minimum and maximum mode, 8288)"]
---
**Minimum mode** is for a **small, single-processor** system. The 8086 generates all bus control signals itself on pins 24-31:

| Pin | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Min mode | $\overline{INTA}$ | ALE | $\overline{DEN}$ | DT/$\overline{R}$ | M/$\overline{IO}$ | $\overline{WR}$ | HLDA | HOLD |

No extra bus controller is needed; HOLD/HLDA serve a DMA controller.

**Maximum mode** is for **larger systems with several processors or a coprocessor** (8087, 8089). These pins change function:

| Pin | 24, 25 | 26, 27, 28 | 29 | 30, 31 |
|:--|:-:|:-:|:-:|:-:|
| Max mode | QS1, QS0 (queue status, for the 8087) | $\overline{S0}$, $\overline{S1}$, $\overline{S2}$ (bus cycle status) | $\overline{LOCK}$ | $\overline{RQ}/\overline{GT1}$, $\overline{RQ}/\overline{GT0}$ |

An **8288 bus controller** decodes $\overline{S2}$-$\overline{S0}$ into $\overline{MRDC}$, $\overline{MWTC}$, $\overline{IORC}$, $\overline{IOWC}$, $\overline{INTA}$, ALE, DEN, DT/$\overline{R}$ (with higher drive), and an 8289 bus arbiter can share the system bus among processors.

**Selecting the mode:** by the **MN/$\overline{MX}$ pin (pin 33)**: connected to **+5 V (logic 1) for minimum mode**, to **ground (logic 0) for maximum mode**. It is a fixed hardware connection, not changed by software.
