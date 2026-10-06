---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "3 queues; top slice 10 ms; bottom slice 55 ms; priority boost every 500 ms; boosting prevents starvation and handles jobs that change behaviour."
sources: ["OSTEP ch. 8 (MLFQ, the priority boost)"]
---
Reading the close-up: the jobs alternate as A $0\text{-}10$, B $10\text{-}20$, A $20\text{-}40$, B $40\text{-}60$, A $60\text{-}115$, B $115\text{-}170$, A $170\text{-}225$: each job first gets a short slice, then a longer one, then the longest one.

**i.** There are **3 queues**: the slice length takes three distinct values (10, 20, 55 ms), each job moving down one level whenever it uses its whole slice.

**ii.** The top (highest priority) queue has a time slice of **10 ms**.

**iii.** The bottom (lowest priority) queue has a time slice of about **55 ms** (A runs 60-115, B 115-170, A 170-225); the middle queue has 20 ms.

**iv.** Processes are moved back to the top queue about every **500 ms**: the pattern "repeats" at 500 ms, when both A and B again run for 10 ms each.

**v.** The periodic **priority boost** (Rule 5 of OSTEP's MLFQ) solves two problems:

- **Starvation:** if there are many interactive jobs, CPU-bound jobs at the bottom queue would never get the CPU; the boost guarantees progress.
- **Change of behaviour:** a job that was CPU-bound and later becomes interactive would otherwise stay at a low priority; after the boost it can again be treated as interactive.
