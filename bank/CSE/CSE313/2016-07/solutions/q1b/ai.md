---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "No: even without bugs or malice the OS must multiplex the processor (time slices) and disk space (blocks allocated on demand with limits) for efficiency, fairness and responsiveness."
sources: ["Anderson and Dahlin, OSPP, ch. 1 (resource allocation: efficiency and fairness)"]
---
Without a need for fault isolation the OS is still the **resource manager**: it must decide *who gets what and when* so that the resources are used **efficiently** and **fairly** and the system stays **responsive**.

**(i) Processor time.** The OS should **not** give the whole processor to each application until it no longer needs it. Even if all programs are well behaved, a long-running computation would make all others wait, and a program that waits for the user or the disk would leave the CPU idle. So the OS **time-slices** the processor (a scheduler: round robin with short quanta, more CPU for some, or switching when a program blocks on I/O): this keeps the CPU busy, gives short jobs and interactive programs fast response, and shares the processor fairly among the users.

**(ii) Disk space.** The first user to ask should **not** get all the free space: that would be unfair to the others (and they could not even start). The OS allocates disk space in **small blocks on demand**, as files grow, and may apply **quotas/limits per user** and policies for fairness; it can also reclaim space, avoid fragmentation, and keep files of the same user close together for performance.

(Efficiency and fairness are **policy** questions that remain even if protection is not needed.)
