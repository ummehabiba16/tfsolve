---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CTC mode with OCR1A as TOP (WGM = 0100) and both OC1A/OC1B toggling (COM = 01): with 1 MHz, no prescaler, OCR1A = 39999 and OCR1B = 29999 give 12.5 Hz, 50% duty, OC1A lagging OC1B by 45 degrees."
sources: ["EHP Timer_Part_2 slides 22-30 (CTC modes; OCR1A = 15625, OCR1B = 7812 toggle example)", "EHP Timer_Part_2 slides 31-38, 47 (fast PWM / phase correct)"]
---
**Which mode?** Use **CTC mode (WGM13:10 = 0100, TOP = OCR1A) with both OC1A and OC1B in toggle mode** (COM1A1:0 = COM1B1:0 = 01), as in the slide example with OCR1A = 15625 and OCR1B = 7812.

- In toggle mode each pin changes once per timer cycle, so each wave has **50% duty**, and its period is 2 timer cycles: $T = 2\,(TOP+1)$ ticks.
- Both waves have the **same frequency**, because both toggle once per cycle of the same counter.
- OC1B toggles when TCNT1 = OCR1B and OC1A when TCNT1 = OCR1A = TOP. The time between the two toggles sets the **phase difference**, which can be anything from 0 to 180 degrees.
- Fast PWM is not suitable: both outputs are set at BOTTOM at the same instant, so the waves cannot be shifted. Phase correct PWM is symmetric about BOTTOM/TOP, and two 50% waves would be in phase or 180 degrees apart.

**Values** (assumption: system clock 1 MHz, no prescaler, so 1 tick = 1 µs)

- Period of each wave $= 1/12.5 = 80$ ms $= 80000$ ticks, so one timer cycle (half period) is 40000 ticks: **OCR1A = TOP = 40000 $-$ 1 = 39999** (fits in 16 bits).
- 45 degrees $= 1/8$ of 80000 ticks $= 10000$ ticks. OC1B must toggle 10000 ticks before OC1A: **OCR1B = 39999 $-$ 10000 = 29999**. OC1A then **lags** OC1B by 45 degrees.

| Register | Value | Meaning |
|:--|:--|:--|
| TCCR1A | 0b01010000 | COM1A1:0 = 01 toggle, COM1B1:0 = 01 toggle, WGM11:10 = 00 |
| TCCR1B | 0b00001001 | WGM13:12 = 01 (CTC, TOP = OCR1A), CS12:10 = 001 (no prescaler) |
| OCR1A | 39999 | TOP: half period 40 ms |
| OCR1B | 29999 | toggles 10 ms (45 degrees) earlier |
| DDRD | PD5, PD4 = 1 | OC1A (PD5) and OC1B (PD4) as outputs |

```text
TCNT1 39999 |    /|    /|    /|    /|        (40 ms per ramp)
      29999 |  */ | */  | */  | */  |        * = OCR1B match
          0 | /   |/    |/    |/    |
OC1B        |__+     +-----+     +-----     toggles at 29999
            |  |_____|     |_____|
OC1A        |_____+     +-----+     +--     toggles at 39999 (TOP)
            |     |_____|     |_____|
               <-> 10 ms = 1/8 of 80 ms
```
