---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The 8086 has a 16-bit data bus but byte-addressable memory, so memory is split into an even bank (D0-D7) and an odd bank (D8-D15), selected by A0 and BHE, to move a word in one cycle and still access single bytes."
sources: ["MHE 8086-Memory_Organization slides 2-6 (odd/even banks, BHE and A0 table)"]
---
- The 8086 has a **16-bit data bus** but memory is **byte-addressable** (1MB, one byte per address).
- To transfer a 16-bit word in **one bus cycle**, two consecutive bytes must be accessed in parallel. So the 1MB is organized as two 512KB banks: the **even (low) bank** on D0-D7 and the **odd (high) bank** on D8-D15, both addressed by A1-A19.
- **A0** (selects the even bank when 0) and **$\overline{BHE}$** (selects the odd bank when 0) choose the bank:

| $\overline{BHE}$ | A0 | Bank(s) accessed |
|:-:|:-:|:--|
| 0 | 0 | both: 16-bit word at an even address |
| 0 | 1 | odd (high) bank only, D8-D15 |
| 1 | 0 | even (low) bank only, D0-D7 |
| 1 | 1 | none |

So a word at an even address is read in one cycle, and single bytes can still be read or written. A word at an odd address needs two cycles.
