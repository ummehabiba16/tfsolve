---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) TCNT1 starts at 0xFFF2 and TOV1 is set when it rolls over to 0: 0x10000 - 0xFFF2 = 14 ticks of 1/8 MHz = 0.125 us, so 1.75 us. (ii) TCCR1B = 0 selects 'no clock source': Timer1 stops. (iii) Writing 1 to TOV1 in TIFR clears the overflow flag, ready for the next delay."
sources: ["EHP Timer_Part_1 slides 19-24 (normal mode, clock select, TIFR/TOV1)"]
---
**(i) Delay of line 10**

Line 10 waits until **TOV1** is set, which happens when TCNT1 overflows from 0xFFFF to 0x0000. TCNT1 was loaded with 0xFFF2, so the number of counts to overflow is

$$0x10000 - 0xFFF2 = 0xE = 14\ \text{counts}$$

With no prescaling at 8 MHz, each count takes $1/8\ \text{MHz} = 0.125\ \mu s$:

$$t = 14 \times 0.125\ \mu s = \mathbf{1.75}\ \mu s$$

**(ii) Line 11: `TCCR1B = 0;`** sets CS12:CS10 = 000, "no clock source". **Timer1 stops** counting (TCNT1 keeps its value) until the next loop iteration starts it again.

**(iii) Line 12: `TIFR = mask;`** writes a **1 to TOV1**, which **clears the overflow flag** (flags in TIFR are cleared by writing 1). Without this, TOV1 would stay set and the next `while(!(TIFR & mask))` would end immediately, so there would be no delay in later iterations.
