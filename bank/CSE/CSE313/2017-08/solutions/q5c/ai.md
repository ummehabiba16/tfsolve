---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Busy waiting = repeatedly testing a condition in a loop; it wastes CPU time, can cause priority inversion and starvation, and is acceptable only for very short waits."
sources: ["Tanenbaum MOS 4e, sec. 2.3.3 (mutual exclusion with busy waiting)"]
---
**Busy waiting** (spinning): a process that cannot proceed continuously **tests a variable (or lock) in a loop** until another process changes it, e.g. `while (turn != 0) ;`. It remains *running* (consuming the CPU) while waiting.

**Problems of busy waiting**

1. **Wastes CPU time:** the processor does no useful work while spinning, especially when the wait is long.
2. **Priority inversion:** if a high-priority process spins waiting for a low-priority process that holds the resource, on a single CPU the low-priority process may never get the CPU to release it, so the high-priority process loops forever.
3. **Starvation/unfairness:** nothing guarantees which spinning process wins the lock.
4. It also produces memory/bus traffic on multiprocessors.

It is therefore appropriate only for **very short waits** (e.g. a spin lock inside the kernel on a multiprocessor); otherwise a blocking primitive (semaphore, mutex with `sleep`/`wakeup`) should be used.
