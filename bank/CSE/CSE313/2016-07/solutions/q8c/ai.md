---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FIFO and SJF beat RR when jobs are of similar length and need to run to completion (RR makes them all finish late and adds context switches); space sharing beats time sharing for parallel applications because their threads need to run together without being preempted."
sources: ["Anderson and Dahlin, OSPP, ch. 7 (scheduling: FIFO, SJF, RR; multiprocessor scheduling, space sharing)"]
---
**Scenario where FIFO and SJF are better than RR.** When the jobs are **similar in length and all arrive together** and only the completion time matters (e.g. 10 batch jobs of 10 time units each). 

- FIFO/SJF run the jobs one after another: completions at $10,20,\dots,100$, **average completion time $55$**.
- RR with a small quantum interleaves them so that **all jobs finish near the end** (about $91\text{-}100$), average $\approx95$, **and** it adds context-switch overhead and cache misses.

RR is better only when the jobs differ a lot in length (a short job is not stuck behind a long one) or when response time matters; for equal-size jobs and throughput/completion time, FIFO/SJF win.

**Space sharing vs time sharing for parallel applications.** The threads of a parallel application **synchronise frequently** (locks, barriers). With **time sharing**, a thread may be preempted while the others spin or wait for it (at a barrier or lock), wasting their time; context switches also destroy cache state. With **space sharing** the machine's processors are **partitioned** among applications, each gets **dedicated CPUs** for its threads: all threads run **simultaneously**, nobody waits for a descheduled thread, there are no context switches, and the caches stay warm. (Time sharing needs gang scheduling to approach this.)
