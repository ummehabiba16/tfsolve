---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "If all processes are blocked, the system is not idle and CPU utilisation falls to zero (or a long timeout expires) a deadlock is suspected; used as a cheap trigger for detection."
sources: ["Tanenbaum MOS 4e, sec. 6.4 (deadlock detection: when to look)"]
---
**Idea.** When processes are deadlocked, they are all **blocked and consume no CPU time**. So the OS can use the **CPU utilisation** as a cheap trigger for running the (expensive) detection algorithm instead of running it on every resource request or at fixed intervals.

**How it works.**

1. The OS monitors CPU utilisation (or the time since a process last made progress).
2. If the utilisation **drops to (nearly) zero** and stays there for a period although there are processes that should be running (they are blocked, not terminated and not waiting for a timer or external event), a deadlock is suspected.
3. Only then the OS runs the detection algorithm (e.g. cycle detection in the resource graph, or the matrix algorithm) to confirm which processes are deadlocked, and starts recovery.

**Limitation.** It is only a heuristic: a low CPU usage can also be caused by heavy I/O, and a partial deadlock (some processes deadlocked while others run normally) does not reduce the utilisation to zero.
