---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Hardware timers count clock pulses independently of the CPU, so their timing does not depend on instruction timing, compiler optimisation or ISRs; software delay loops do (e.g. _delay_ms stretched by ISRs) and also keep the CPU busy."
sources: ["EHP Timer_Part_1 slides 3-5 (software technique vs hardware; problem with _delay_ms)"]
---
- A **hardware timer** increments its counter directly from the (prescaled) system clock, **independently of the program**. The elapsed time is just $\text{count}\times\text{tick period}$, whatever the CPU is doing.
- A **software delay** counts loop iterations. Its timing depends on the number of cycles each instruction takes, on compiler optimisation, and on anything that interrupts it: if an ISR runs during `_delay_ms(1)` and takes 200 µs, the delay becomes 1.2 ms.
- The software method also keeps the **CPU busy**, while a timer lets the CPU do other work and signals by interrupt.
