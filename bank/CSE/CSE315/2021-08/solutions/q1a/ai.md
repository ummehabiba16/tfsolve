---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(a) not workable: RQ/GT, LOCK and multiprocessing need maximum mode, so MN/MX' must be 0. (b) not workable: both GND pins (1 and 20; there is no pin 42) must be grounded. (c) workable once in maximum mode. (d) partly wrong: LOCK' locks the system bus against other bus masters (via the 8289 arbiter) during a LOCK-prefixed instruction, not peripherals. (e) not workable on an 8086: IO/M' and SS0' are 8088 pins; in maximum mode the 8288 decodes S2', S1', S0' into MRDC', MWTC', IORC', IOWC'."
sources: ["MHE 8086 Hardware Specifications slides (pin descriptions, MN/MX, GND pins 1 and 20, minimum/maximum mode pins)", "MHE 8086-Architecture slide 'Pin overview' (two GND pins in parallel)", "Brey, The Intel Microprocessors, Sec. 9-1 and 9-6 (8086 pin-out, maximum mode, 8288 bus controller, RQ/GT, LOCK)"]
---
| Usage | Workable? | Reason and fix |
|:-:|:-:|:--|
| a | **No** | MN/$\overline{MX}$ = 1 selects **minimum mode**. In minimum mode pins 24-31 are $\overline{INTA}$, ALE, $\overline{DEN}$, DT/$\overline{R}$, M/$\overline{IO}$, $\overline{WR}$, HLDA, HOLD; the $\overline{RQ}/\overline{GT}$ and $\overline{LOCK}$ pins of (c) and (d) **do not exist**. A design with **multiple processors** must use **maximum mode** with the 8288 bus controller (and 8289 arbiter). **Fix: connect MN/$\overline{MX}$ to logic 0 (GND).** |
| b | **No** | The 8086 is a 40-pin chip; its GND pins are **1 and 20** (pin 42 does not exist). Both GND pins must be connected to ground. They are in parallel so that the large transient currents of the chip are shared without a significant voltage drop; leaving one floating can cause ground bounce and unreliable logic levels. **Fix: connect both pins 1 and 20 to logic 0 (GND).** |
| c | **Yes** (in maximum mode) | $\overline{RQ}/\overline{GT0}$ (pin 31) and $\overline{RQ}/\overline{GT1}$ (pin 30) are bidirectional: another bus master (coprocessor, second processor or DMA controller) sends a request pulse, the 8086 answers with a grant pulse, and a release pulse returns the bus. $\overline{RQ}/\overline{GT0}$ has the higher priority. This works only after (a) is fixed. |
| d | **Not as stated** | $\overline{LOCK}$ (pin 29, maximum mode) is an output that goes low during an instruction with the LOCK prefix (e.g. `LOCK XCHG` for a semaphore). It tells the bus arbiter (8289) **not to give the system bus to any other bus master** until the instruction finishes. It locks the **bus**, not peripherals. **Fix: connect $\overline{LOCK}$ to the LOCK input of the 8289 bus arbiter** and use it for atomic read-modify-write of shared memory. |
| e | **No** | IO/$\overline{M}$ and $\overline{SS0}$ are **8088** minimum-mode pins. The 8086 has M/$\overline{IO}$ (opposite polarity) on pin 28 and $\overline{BHE}$/S7 on pin 34. Also, in maximum mode (needed by (a)), pins 26-28 become the status lines $\overline{S0}$, $\overline{S1}$, $\overline{S2}$. **Fix: connect $\overline{S2}$, $\overline{S1}$, $\overline{S0}$ to the 8288 bus controller**, which decodes them into $\overline{MRDC}$, $\overline{MWTC}$, $\overline{IORC}$, $\overline{IOWC}$ (and $\overline{INTA}$, ALE, DEN, DT/$\overline{R}$). |

**8288 decoding used in the fix for (e)**

| $\overline{S2}$ $\overline{S1}$ $\overline{S0}$ | Bus cycle | 8288 command |
|:-:|:--|:--|
| 0 0 0 | Interrupt acknowledge | $\overline{INTA}$ |
| 0 0 1 | I/O read | $\overline{IORC}$ |
| 0 1 0 | I/O write | $\overline{IOWC}$ |
| 0 1 1 | Halt | none |
| 1 0 0 | Opcode fetch | $\overline{MRDC}$ |
| 1 0 1 | Memory read | $\overline{MRDC}$ |
| 1 1 0 | Memory write | $\overline{MWTC}$ |
| 1 1 1 | Passive | none |
