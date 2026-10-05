---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Yes: ADCL must be read first. Reading ADCL locks both registers until ADCH is read, so both bytes come from the same conversion. Reading ADCH first lets a new conversion change ADCL in between (mixed result), and the later ADCL read locks the registers so following results are lost until ADCH is read again."
sources: ["EHP 6. AVR ADC slides 26-28 (read ADCL before ADCH)"]
---
**Yes, the order matters: read ADCL first, then ADCH.**

- The 10-bit result is split over two 8-bit registers, so two separate reads are needed. A new conversion could finish **between** them (e.g. in free-running mode) and the two bytes would belong to **different conversions**.
- To prevent this the ATmega32 **locks** the data registers when **ADCL is read**: the ADC cannot update ADCL/ADCH until **ADCH is read**, which unlocks them. A conversion that completes while they are locked is lost.
- So reading **ADCL then ADCH** always gives a matching pair from one conversion.
- If ADCH is read first: the high byte may come from an older conversion than the low byte, and the ADCL read then locks the registers, which stay locked until the next ADCH read. New results are discarded meanwhile, so the program keeps reading stale values.

(Reading the 16-bit `ADC` register in C makes the compiler read ADCL first. If only 8 bits are needed, set ADLAR = 1 and read only ADCH.)
