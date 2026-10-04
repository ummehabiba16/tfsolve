---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "_delay_ms() is a busy-wait loop: if an ISR runs during it, the ISR time is added and the delay becomes longer than asked (e.g. _delay_ms(1) + 200 us ISR = 1.2 ms); it also keeps the CPU busy doing nothing."
sources: ["EHP Timer_Part_1 slide 5 (problem of delay_ms)", "EHP Timer_Part_1 slide 4 (software vs hardware timing)"]
---
`_delay_ms()` makes a delay **in software**: it runs a counted busy-wait loop whose length is computed from `F_CPU`. Its problems:

1. **The delay is not accurate when interrupts occur.** The loop counts CPU cycles, not real time. If an interrupt fires during the delay, the ISR is serviced first and then the loop continues where it stopped, so the ISR time is **added** to the delay.

   *Example:* we call `_delay_ms(1)` and, during it, an ISR that takes 200 µs to service runs. The loop still has to finish all its cycles, so the actual delay is $1 + 0.2 = 1.2$ ms, 20% longer than intended. With several interrupts the error is larger and unpredictable.

2. **The CPU is busy for the whole delay.** It cannot do any useful work while it waits.

The solution is to use a **hardware timer** (e.g. Timer 1 overflow or CTC interrupt): the timer counts independently of the CPU, so ISRs do not change the delay, and the CPU is free in the meantime.
