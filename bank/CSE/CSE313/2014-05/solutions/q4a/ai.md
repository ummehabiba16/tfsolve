---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "wakeup removes every process sleeping on the address from the sleep hash queue, marks it ready to run and puts it on the run queue (waking the swapper if it is swapped out); the process table and sleep hash queues are the data structures."
sources: ["Bach, ch. 6 (algorithm wakeup; process table, sleep hash queues)"]
---
**What happens** (algorithm `wakeup`, called by an interrupt handler or by a process releasing a resource, with the sleep address as argument):

1. The kernel **raises the processor level** to block interrupts (interrupt handlers also call `wakeup`).
2. It finds the **sleep hash queue** for the address (sleeping processes are kept on hash queues keyed by the sleep address).
3. For **each process asleep on that address**: remove it from the hash queue, set its state in the **process table** to **ready to run**, put it on the scheduler's **run queue**, and clear its sleep-address field.
4. If the process is **not loaded in memory** (swapped out), **wake up the swapper** (process 0) to bring it in; otherwise, if it is **more eligible to run** than the current process, set the scheduler flag so that the scheduler runs when the current process returns to user mode.
5. Restore the processor level.

**Data structures:** the **process table entry** (state, priority, sleep address), the **sleep hash queues** and the **run queue**; the buffer cache and the u area are untouched. The woken process does not run at once; when it runs it **re-checks** the condition it slept for, since another process may have taken the resource first.
