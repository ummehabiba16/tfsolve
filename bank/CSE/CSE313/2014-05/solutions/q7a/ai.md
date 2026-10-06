---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Agree: in real-time systems a result delivered after its deadline is useless (and may be harmful), so timeliness is part of correctness."
sources: ["Tanenbaum MOS 4e, sec. 2.4.1 (scheduling goals, real-time systems)"]
---
**Yes, I agree.** In a **real-time system** the correctness of a result depends not only on its value but also on **the time at which it is produced**: every task has a **deadline**. A correct value that arrives after the deadline is **worthless** or even **harmful**, so it is "just as bad as not having it at all".

- **Hard real-time** systems (airbag controller, pacemaker, flight control, anti-lock brakes, industrial robots): missing a deadline is a **failure with catastrophic consequences**; the airbag must inflate within milliseconds of the crash, a late correct answer is useless.
- **Soft real-time** systems (video/audio playback, VoIP): a late result is **degraded** (a frame that arrives late is dropped, audio glitches); occasional misses are tolerable, but a result that is too late has no value.

That is why real-time operating systems stress **predictable, bounded response times** and deadline-driven scheduling (rate-monotonic, earliest deadline first) rather than average-case speed.
