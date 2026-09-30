---
author: ai
via: chat
status: unverified
summary: Under the stated quantum schedule the average turnaround $= 385/4 = 96.25$ s (assumptions noted).
sources: [Scheduling slides 37-45, 'Tanenbaum, MOS 4e, sec. 2.4']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Assumptions (the paper leaves these open): both classes use RR; a single global quantum counter gives $q=20$ for the first 5 dispatches and $q=30$ afterwards; at each quantum boundary the highest-priority ready class is chosen (priority 1 = $\{P1,P4\}$, priority 2 = $\{P2,P3\}$); a running process keeps the CPU until its quantum ends.

```gantt
# Gantt chart
P1 0 30
P2 30 50
P3 50 70
P4 70 140
P2 140 160
P3 160 205
```

1. P1 runs 0$\to$20 then 20$\to$30 (completes; P2 arrives at 30).
2. P2 (only prio-2 ready) runs 30$\to$50 (rem 20); P3 arrives at 50.
3. P3 runs 50$\to$70 (rem 45); P4 (prio 1) arrives at 70 and is now highest priority.
4. P4 runs 70$\to$140 (quanta 20+30+... ; alone in class 1, so it runs to completion).
5. Back to class 2: P2 runs 140$\to$160 (completes), then P3 runs 160$\to$205 (completes).

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P1 | 30 | 0 | 30 |
| P4 | 140 | 70 | 70 |
| P2 | 160 | 30 | 130 |
| P3 | 205 | 50 | 155 |

Average $= (30+70+130+155)/4 = 96.25$ s.

**Explanation.**

The result depends on the quantum-counting convention. If the '5 quanta at q=20' is counted per class rather than globally, or if a higher-priority arrival preempts mid-quantum, the boundaries shift; the method (priority between classes, RR within a class) is unchanged.
