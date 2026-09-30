---
author: ai
via: chat
status: unverified
summary: 'SJF: average turnaround = $450/4 = 112.5$ s. RR ($q=30$): average = $700/4 = 175$ s. Priority (RR within a class): average = $540/4 = 135$ s.'
sources: [Scheduling slides 15-45, 'Tanenbaum, MOS 4e, sec. 2.4.2']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
Workload: P1(prio 3, 70, 40), P2(prio 1, 40, 0), P3(prio 1, 100, 10), P4(prio 2, 50, 70). Priority direction is not stated; assume lower number = higher priority.

(i) Non-preemptive SJF (shortest available burst first):

```gantt
# SJF
P2 0 40
P1 40 110
P4 110 160
P3 160 260
```

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P2 | 40 | 0 | 40 |
| P1 | 110 | 40 | 70 |
| P4 | 160 | 70 | 90 |
| P3 | 260 | 10 | 250 |

Average $= (40+70+90+250)/4 = 112.5$ s.

(ii) Round Robin, $q=30$, queue in arrival order:

```gantt
# RR (q=30)
P2 0 30
P3 30 60
P2 60 70
P1 70 100
P3 100 130
P4 130 160
P1 160 190
P3 190 220
P4 220 240
P1 240 250
P3 250 260
```

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P2 | 70 | 0 | 70 |
| P4 | 240 | 70 | 170 |
| P1 | 250 | 40 | 210 |
| P3 | 260 | 10 | 250 |

Average $= (70+170+210+250)/4 = 175$ s.

(iii) Priority scheduling, RR ($q=30$) within a class (from (ii)); class 1 = $\{P2,P3\}$, class 2 = $\{P4\}$, class 3 = $\{P1\}$:

```gantt
# Priority + RR
P2 0 30
P3 30 60
P2 60 70
P3 70 140
P4 140 190
P1 190 260
```

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P2 | 70 | 0 | 70 |
| P3 | 140 | 10 | 130 |
| P4 | 190 | 70 | 120 |
| P1 | 260 | 40 | 220 |

Average $= (70+130+120+220)/4 = 135$ s.

**Explanation.**

RR queue convention: on a quantum expiry the arriving job(s) are enqueued before the preempted job is re-appended. A different convention shifts some later slices but not the total makespan (260 s = sum of bursts). The priority-direction assumption (lower = higher) follows the other years' papers.
