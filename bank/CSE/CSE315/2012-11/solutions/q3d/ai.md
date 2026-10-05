---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "ADCL first, then ADCH. Reading ADCL blocks the ADC from updating both registers until ADCH is read, so the two bytes come from the same conversion; reading ADCH re-enables updates. Otherwise a conversion ending between the reads could mix bytes, and an ADCL read left without a following ADCH read would lock out (lose) new results."
sources: ["EHP 6. AVR ADC slides 26-28 (read ADCL before ADCH)"]
---
**ADCL must be read first, then ADCH.**

- The 10-bit result occupies two registers, so the CPU needs two reads, and a new conversion could finish between them.
- When **ADCL is read**, the ADC's access to the data registers is **blocked**: ADCL and ADCH keep their values until **ADCH is read**. A conversion completing in between is lost (not written).
- Reading **ADCH** re-enables the ADC's access.

So reading ADCL then ADCH guarantees that **both bytes belong to the same conversion**. If ADCH were read first, the high byte could come from one conversion and the low byte from the next, and the final ADCL read would lock the registers until the next ADCH read, losing new results. (If 8-bit precision is enough, set ADLAR = 1 and read only ADCH.)
