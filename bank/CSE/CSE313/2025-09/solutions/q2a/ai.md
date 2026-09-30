---
author: ai
via: chat
status: unverified
summary: Average turnaround = $295/4 = 73.75$ s.
sources: [Scheduling slides 37-45, 'Tanenbaum, MOS 4e, sec. 2.4']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Priority 1 = $\{P1,P4\}$ (RR, $q=30$); priority 2 = $\{P2,P3\}$ (FCFS). A running process is never interrupted before its quantum (RR) or its job (FCFS) ends.

```gantt
# Gantt chart
P1 0 30
P2 30 70
P4 70 140
P3 140 205
```

1. $t=0$: only P1 ready $\Rightarrow$ P1 runs 30, finishes at 30.
2. $t=30$: only P2 ready (prio 2) $\Rightarrow$ FCFS, runs to completion 30$\to$70 (P4 arrives at 70 but does not preempt).
3. $t=70$: P4 (prio 1) is chosen over P3 and is the only prio-1 job, so RR runs it 70$\to$140.
4. $t=140$: P3 (prio 2) runs 140$\to$205.

| Process | Finish | Arrival | Turnaround |
|:--|:-:|:-:|:-:|
| P1 | 30 | 0 | 30 |
| P2 | 70 | 30 | 40 |
| P4 | 140 | 70 | 70 |
| P3 | 205 | 50 | 155 |

Average turnaround $= (30+40+70+155)/4 = 73.75$ s.
