---
author: ai
via: chat
status: unverified
summary: 'SRTN: average turnaround = $280/4 = 70$ s. Priority (RR $q=20$ within a class): average = $365/4 = 91.25$ s.'
sources: [Scheduling slides 28-45, 'Tanenbaum, MOS 4e, sec. 2.4.2']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
Workload: P1(prio 1, 60, 0), P2(prio 1, 25, 30), P3(prio 2, 80, 50), P4(prio 3, 20, 70).

(1) Shortest Remaining Time Next (preemptive, priorities ignored):

```gantt
# SRTN
P1 0 30
P2 30 55
P1 55 85
P4 85 105
P3 105 185
```

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P1 | 85 | 0 | 85 |
| P2 | 55 | 30 | 25 |
| P3 | 185 | 50 | 135 |
| P4 | 105 | 70 | 35 |

Average $= (85+25+135+35)/4 = 70$ s.

(2) Priority scheduling, RR ($q=20$) within the same priority class, separate FIFO queues (lower number = higher priority; a job keeps the CPU until its quantum ends):

```gantt
# Priority + RR
P1 0 40
P2 40 60
P1 60 80
P2 80 85
P3 85 165
P4 165 185
```

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P1 | 80 | 0 | 80 |
| P2 | 85 | 30 | 55 |
| P3 | 165 | 50 | 115 |
| P4 | 185 | 70 | 115 |

Average $= (80+55+115+115)/4 = 91.25$ s.

**Explanation.**

SRTN: at $t=30$ P2 (rem 25) beats P1 (rem 30) and runs to completion at 55; P1 then resumes (rem 30) and finishes before the newly arrived P4 (P1 rem 15 < P4 20 at $t=70$), then P4, then P3.
