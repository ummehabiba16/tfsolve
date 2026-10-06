---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Average waiting time: SJF 72 s, SRTF 72 s, RR (q=30) 162 s."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2-2.4.3"]
---
Workload: P1 (burst 40, arrival 50, priority 4), P2 (70, 10, 3), P3 (50, 0, 1), P4 (100, 0, 5), P5 (50, 70, 2). Waiting time $=$ turnaround $-$ burst $=$ completion $-$ arrival $-$ burst (computed with a script; priorities are not used by these algorithms).

**(i) Non-preemptive SJF**

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
| Waiting | 0 | 130 | 0 | 210 | 20 |

Average waiting time $=360/5=\mathbf{72}$ s.

**(ii) Shortest Remaining Time First.** No arrival preempts the running process (P2 at 10: burst 70 $>$ 40 left of P3; P1 at 50 as P3 ends; P5 at 70: 50 $>$ 20 left of P1), so the schedule and the waiting times are the same as for SJF: average $=\mathbf{72}$ s.

**(iii) Round robin, quantum 30 s**

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
| Waiting | 150 | 220 | 60 | 210 | 170 |

Average waiting time $=810/5=\mathbf{162}$ s.
