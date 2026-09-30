---
author: ai
via: chat
status: unverified
summary: Non-preemptive SJF runs the shortest job to completion; preemptive SJF (SRTN) preempts the running job whenever a newly arrived job has a shorter remaining time.
sources: [Scheduling slides 28-34, 'Tanenbaum, MOS 4e, sec. 2.4.2']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Example. P1 (burst 10, arrival 0), P2 (burst 2, arrival 2).

- Non-preemptive SJF: P1 is already running at $t=0$, runs 0$\to$10, then P2 10$\to$12. Turnarounds 10 and 10, average 10.
- Preemptive SJF / SRTN: at $t=2$, P2 (rem 2) < P1 (rem 8), so P2 preempts and runs 2$\to$4, then P1 4$\to$12. Turnarounds P1=12, P2=2, average 7.
