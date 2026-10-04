---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "So that both bytes belong to the same conversion: reading ADCL locks ADCL/ADCH (the ADC cannot update them) until ADCH is read. Reading ADCH first would let a new conversion change ADCL in between (mixed result), and then ADCL would lock the registers, losing later results until the next ADCH read."
sources: ["EHP 6. AVR ADC slides 26-28 (ADCH and ADCL, read ADCL before ADCH)"]
---
The 10-bit result does not fit in one 8-bit register, so it is split into ADCL and ADCH, which the CPU must read one after the other. A new conversion could finish **between** the two reads and overwrite them, giving a low byte from one conversion and a high byte from another.

To prevent this the ATmega32 uses a **lock**:

- When **ADCL is read**, ADC access to the data registers is **blocked**: ADCL and ADCH will not change until ADCH is read.
- When **ADCH is read**, access is **re-enabled**.
- If a conversion completes while the registers are blocked, its result is **lost** (not written).

So the correct order is **ADCL first, then ADCH**: the read of ADCL freezes the pair, and the ADCH read gets the high byte of the **same** conversion and then releases the lock.

If ADCH were read first, (1) the two bytes might come from different conversions, and (2) the ADCL read would then lock the registers and leave them locked until the next ADCH read, so new results would be lost and the program would keep reading stale values. (If only 8 bits are needed, set ADLAR = 1 and read only ADCH.)
