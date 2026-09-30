---
author: ai
via: chat
status: unverified
summary: Run the jobs in non-decreasing order of run time (Shortest-Job-First); place X by its rank.
sources: [Scheduling slides 28-31, 'Tanenbaum, MOS 4e, sec. 2.4.2']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
For jobs that arrive together and are non-preemptive, average turnaround is minimised by Shortest-Job-First order. Sorting $\{9,3,5,X\}$:

- $X \le 3$:  X, 3, 5, 9
- $3 < X \le 5$:  3, X, 5, 9
- $5 < X \le 9$:  3, 5, X, 9
- $X > 9$:  3, 5, 9, X

**Explanation.**

SJF is optimal here because moving a shorter job earlier reduces the waiting time it contributes to every job scheduled after it.
