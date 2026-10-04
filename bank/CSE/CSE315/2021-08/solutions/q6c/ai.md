---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "CTC, TOP = OCR1A = 32768, 1 us tick: TCNT1 ramps 0-32768 every 32.769 ms. OC1B toggles when TCNT1 = 7812 (t = 7.8 ms, then every 32.769 ms) and OC1A at TOP (t = 32.8 ms, ...). Both are 50% square waves with period 65.54 ms (15.26 Hz); OC1B leads OC1A by 24.96 ms."
sources: ["EHP Timer_Part_2 slides 27-30 (CTC mode, toggle on compare match, OCR1A/OCR1B example waveform)"]
---
**Setup.** CTC (WGM = 0100): TCNT1 counts 0, 1, ..., 32768 and is cleared on the match with OCR1A, so one timer cycle is $32768 + 1 = 32769$ ticks $= 32.769$ ms (1 µs per tick, no prescaler). OC1A and OC1B **toggle** on their compare matches; both start low.

- **OC1B** toggles when TCNT1 = 7812: at $t = 7.812$ ms, then every 32.769 ms (40.58 ms, 73.35 ms, ...).
- **OC1A** toggles when TCNT1 = 32768 (TOP): at $t = 32.768$ ms, then every 32.769 ms (65.54 ms, 98.31 ms, ...).

```text
 32768|               *               *               *               *
      |            ***             ***             ***             ***
      |          **              **              **              **
      |       ***             ***             ***             ***
      |    ***             ***             ***             ***
  7812|  **              **              **              **
     0|**              **              **              **              *
OC1B 1|    ----------------                ----------------
     0|----                ----------------                -------------
OC1A 1|                ----------------                ----------------
     0|----------------                ----------------                -
       0   7.8         32.8            65.5            98.3            131  t (ms)
```

**Result.** Each output toggles once per timer cycle, so both are **square waves with 50% duty cycle**, period $2 \times 32.769 = 65.538$ ms and frequency

$$f = \frac{f_{clk}}{2N(1 + OCR1A)} = \frac{10^6}{2 \times 1 \times 32769} = 15.26\ \text{Hz}$$

OCR1B only shifts the phase: OC1B toggles $(32768 - 7812)\ \mu s = 24.956$ ms **before** OC1A in every cycle.
