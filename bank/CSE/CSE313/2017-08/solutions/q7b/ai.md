---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "SRTN needs the remaining time in advance (only an estimate), starves long jobs, and needs bookkeeping and extra context switches."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2 (shortest remaining time next)"]
---
**Shortest Remaining Time Next (SRTN)** is the preemptive version of SJF: the process with the least remaining run time always gets the CPU, and a new process with a shorter remaining time preempts the running one. Its limitations:

1. **Requires knowing the run times** (remaining burst times) in advance, which is usually impossible; they can only be estimated (e.g. by exponential averaging of earlier bursts), and bad estimates degrade the schedule.
2. **Starvation:** long jobs may be postponed indefinitely if a stream of short jobs keeps arriving.
3. **Overhead:** it must keep track of the remaining time of every process and compare on every arrival; frequent **preemptions** mean many **context switches**.
4. It is **unfair** (long jobs suffer) and does not take priorities or deadlines into account.
5. It is only optimal for mean turnaround when all job information is available.
