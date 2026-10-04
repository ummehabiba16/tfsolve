---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Reading ADCL locks ADCH/ADCL until ADCH is read. If ADCH is always read first, every ADCL read locks the registers and the next conversion finishes while they are locked, so its result is lost: the reading stays stuck at the first value, or (free running) updates only rarely and may mix the high byte of one conversion with the low byte of another."
sources: ["EHP 6. AVR ADC slides 26-28 (read ADCL before ADCH, data registers blocked after ADCL read, results lost)"]
---
**The rule (datasheet / slide 27):** once **ADCL** is read, the ADC can no longer update ADCL and ADCH until **ADCH** is read. A conversion that finishes in between is **lost**. Reading ADCH re-enables updates.

**Reading ADCH first, then ADCL, every time** (e.g. start conversion, wait for ADIF, read ADCH, read ADCL):

| Step | What happens |
|:--|:--|
| Conversion 1 finishes | Registers are free, so they get result 1 |
| Read ADCH | High byte of result 1 (registers were not locked) |
| Read ADCL | Low byte of result 1, and the registers are now **locked** |
| Conversion 2 finishes | Registers locked, so **result 2 is lost** |
| Read ADCH | Still **result 1** (unlocks) |
| Read ADCL | Still **result 1**, locked again |
| Conversion 3, 4, ... | Lost in the same way |

**Pattern:** the program reads the **same (first) value again and again**, even when the input voltage changes. The reading looks frozen.

In free-running mode a conversion sometimes finishes **between** the ADCH read and the ADCL read. Then the value is updated only occasionally, and the two bytes belong to **different conversions**: the old high byte with a new low byte. This gives sudden jumps of about 256 counts when the input crosses a high-byte boundary.

**Correct order:** read ADCL first, then ADCH (or read the 16-bit `ADC` register, which the compiler reads in that order). If only 8 bits are needed, set ADLAR = 1 and read **only ADCH**.
