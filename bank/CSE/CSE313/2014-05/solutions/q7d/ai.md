---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "SJF and SRTN both give P3, P1, P5, P2, P4 and average turnaround 134 s; RR (q=30) gives 224 s."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2-2.4.3 (SJF, SRTN, round-robin)"]
---
Workload (priority is not needed here): P1: burst 40, arrival 50; P2: 70, arrival 10; P3: 50, arrival 0; P4: 100, arrival 0; P5: 50, arrival 70. Ties between processes arriving together are broken by process number. (Schedules computed with a short script.)

**(i) Shortest Job First** (non-preemptive): at time 0 the ready jobs are P3 (50) and P4 (100), so P3 runs; at 50 the ready jobs are P4 (100), P2 (70) and P1 (40): P1 runs; at 90: P5 (50, arrived at 70), P2, P4: P5; then P2; then P4.

```gantt
# SJF
P3 0 50
P1 50 90
P5 90 140
P2 140 210
P4 210 310
```

| Process | P1 | P2 | P3 | P4 | P5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| Completion | 90 | 210 | 50 | 310 | 140 |
| Turnaround | 40 | 200 | 50 | 310 | 70 |

Average $=670/5=\mathbf{134}$ s.

**(ii) Shortest Remaining Time Next.** At each arrival (P2 at 10, P1 at 50, P5 at 70) the new process has a longer burst than the remaining time of the running one (P2 70 $>$ 40 left of P3; P1 40 $>$ 0 left, as P3 finishes at 50; P5 50 $>$ 20 left of P1), so there is **no preemption** and the schedule is the same as SJF:

```gantt
# SRTN
P3 0 50
P1 50 90
P5 90 140
P2 140 210
P4 210 310
```

Average turnaround $=\mathbf{134}$ s.

**(iii) Round robin, quantum 30 s:**

```gantt
# RR, q = 30
P3 0 30
P4 30 60
P2 60 90
P3 90 110
P1 110 140
P4 140 170
P5 170 200
P2 200 230
P1 230 240
P4 240 270
P5 270 290
P2 290 300
P4 300 310
```

| Process | P1 | P2 | P3 | P4 | P5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| Completion | 240 | 300 | 110 | 310 | 290 |
| Turnaround | 190 | 290 | 110 | 310 | 220 |

Average $=1120/5=\mathbf{224}$ s.
