---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "_delay_ms() is a software busy-wait: any ISR that runs during it adds its own time, so the delay becomes longer than requested (e.g. _delay_ms(1) + 200 us ISR = 1.2 ms), and the CPU can do nothing else meanwhile."
sources: ["EHP Timer_Part_1 slides 4-5 (software delay, problem of delay_ms)"]
---
**Major drawback: the delay is not accurate when interrupts occur.** `_delay_ms()` is a software busy-wait loop that counts CPU cycles. If an interrupt fires during the delay, the ISR is executed first and then the loop continues, so the ISR's execution time is **added** to the delay.

*Example:* `_delay_ms(1)` interrupted by an ISR that takes 200 µs gives an actual delay of $1 + 0.2 = 1.2$ ms.

(It also keeps the CPU busy doing nothing for the whole delay.) A hardware timer (overflow or CTC interrupt) avoids both problems.
