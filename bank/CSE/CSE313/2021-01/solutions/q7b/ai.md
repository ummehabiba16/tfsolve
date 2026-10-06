---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Guaranteed scheduling: promise each of n users 1/n of the CPU; run the process with the lowest ratio of CPU time used to CPU time entitled; fair but needs bookkeeping."
sources: ["Tanenbaum MOS 4e, sec. 2.4.5 (guaranteed scheduling)"]
---
**Goal.** Give users a *real promise* about performance rather than just trying to be fair: if $n$ processes (users) are logged in, each one is guaranteed about **$1/n$ of the CPU** power.

**Metric.** The OS keeps track of how much CPU time each process has actually had since it was created, and computes how much it is entitled to: (time since creation)/$n$. The ratio is

$$\text{ratio}=\frac{\text{CPU time actually consumed}}{\text{CPU time entitled}}$$

A ratio of 0.5 means the process has had only half of what it should; 2.0 means twice as much. The scheduler **runs the process with the lowest ratio** until its ratio has risen above that of its closest competitor.

**Pros**

- It delivers a true, measurable **fairness guarantee** ($1/n$ each).
- No process is starved; simple to explain to users.

**Cons**

- It needs **bookkeeping** of the CPU time of every process and a computation of ratios; finding the minimum costs time at every scheduling decision.
- It does not take **priorities or process importance** into account.
- A process that sleeps for a long time builds up a huge entitlement and can then **monopolise the CPU** when it wakes (this can be limited by bounding the history).
