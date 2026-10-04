---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "_delay_ms() is a busy-wait loop, so any ISR that runs during it adds its time and the delay becomes longer than requested (e.g. _delay_ms(1) with a 200 us ISR lasts 1.2 ms); the CPU is also blocked meanwhile."
sources: ["EHP Timer_Part_1 slides 4-5 (problem of delay_ms)"]
---
**Problem: the delay becomes longer (inaccurate) when interrupts occur.** `_delay_ms()` is a software busy-wait loop that counts CPU cycles. If an ISR fires during the delay, the ISR runs first and the loop then continues, so the ISR's time is **added** to the delay.

*Example:* `_delay_ms(1)` interrupted by an ISR that takes 200 µs gives a real delay of 1.2 ms.

The CPU is also kept busy doing nothing for the whole delay. Hardware timers avoid both problems.
