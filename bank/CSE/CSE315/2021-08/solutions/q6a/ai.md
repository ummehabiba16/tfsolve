---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Ticks between E1 and E2 = 2 x 65536 + (8000 - 6700) = 132372; at 1 us per tick the period is 132372 us = 132.372 ms (f = 7.55 Hz)."
sources: ["EHP Timer_Part_1 slides 29-37 (elapsed time with overflow count; input capture period measurement)"]
---
TIMER1 runs at 1 MHz (no prescaling), so one tick = 1 µs and the 16-bit counter overflows every $2^{16} = 65536$ ticks.

Between E1 (TCNT1 = 6700) and E2 (TCNT1 = 8000) the timer overflowed **2** times:

$$\text{ticks} = 2 \times 65536 + (8000 - 6700) = 131072 + 1300 = 132372$$

$$T = 132372 \times 1\ \mu s = \mathbf{132.372\ ms} \qquad (f = 1/T \approx 7.55\ \text{Hz})$$

*Check:* from E1 to the first overflow is $65536 - 6700 = 58836$ ticks, a full cycle to the second overflow is 65536, and then 8000 ticks to E2: $58836 + 65536 + 8000 = 132372$.
