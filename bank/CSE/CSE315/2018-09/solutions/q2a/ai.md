---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Invalid. The 74LS636 (8 data + 5 Hamming check bits) corrects single-bit errors itself (SEF switches it to correct mode, no interrupt) and flags double-bit errors on DEF, which is wired to NMI; errors of 3 or more bits are beyond SEC-DED and may be missed or miscorrected. Also it interrupts a microprocessor (8086/8088 NMI), not a microcontroller."
sources: ["Brey, The Intel Microprocessors, Sec. 10-2 (error correction with the 74LS636, SEF and DEF, check memory)"]
---
**The statement is not valid.**

**How the circuit works.** The 74LS636 is an 8-bit error detection and correction chip using a Hamming code with **5 check bits**. The data byte is stored in one 4016 (2K $\times$ 8) RAM and the 5 check bits in another 4016.

- **Write** ($\overline{WR}$ active): the 636 generates the check bits from the data on the bus and stores them in the check memory at the same address.
- **Read** ($\overline{RD}$ active): data and check bits are read back; the 636 recomputes the check bits and compares them (syndrome). It sets two flags:
  - **SEF** (single error flag): exactly **one** bit is wrong. Through the inverter and the '08 gate this changes S1/S0 so the chip enters its **correct** mode, and the **corrected** byte is driven to the data bus through the '245. The program never notices.
  - **DEF** (double error flag): **two** bits are wrong. The error can be detected but not corrected. DEF is connected to **NMI**, so only this case interrupts the processor.

**Checking each part of the statement**

| Error | What happens | NMI? |
|:--|:--|:-:|
| Single-bit | detected and **corrected automatically** (SEF) | **No** |
| 2-bit | detected, not correctable (DEF) | **Yes** |
| 3 or more bits | outside the capability of a SEC-DED code: may look like a single error (wrongly "corrected") or like no error | **Not guaranteed** |

So NMI is generated only for **double-bit** errors, not for "any single-bit, 2-bit or multi-bit error". Also, NMI here goes to a **microprocessor** (8086/8088), not a microcontroller.
