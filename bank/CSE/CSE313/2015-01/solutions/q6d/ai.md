---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Safe state: there is a sequence in which every process can run to completion even if all demand their maximum; unsafe: no such sequence (deadlock is possible, not certain)."
sources: ["Tanenbaum MOS 4e, sec. 6.5.1 (safe and unsafe states)"]
---
(In this chapter the term is used for *resource allocation*; the question's "process scheduling" refers to the order in which the processes are allowed to run to completion.)

- A state is **safe** if it is *not deadlocked* and there exists some **scheduling order (a safe sequence)** in which every process can be run to completion even if all of them request their maximum number of resources at once: the available resources can satisfy the first process, which then releases its resources, enabling the next, and so on.
- A state is **unsafe** if no such sequence exists. An unsafe state is **not necessarily a deadlock**: the processes may happen to complete (if some do not ask for the maximum), but the OS can no longer guarantee that all of them will; the *possibility* of deadlock exists. A deadlocked state is always unsafe.

The difference is that from a safe state the system can **guarantee** that deadlock will be avoided, while from an unsafe state it cannot.
