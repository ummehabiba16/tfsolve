---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Round robin with quantum 30 s: schedule P3 P4 P2 P3 P1 P4 P5 P2 P1 P4 P5 P2 P4; average turnaround 220 s."
sources: ["Tanenbaum MOS 4e, sec. 2.4.3 (round-robin scheduling)"]
---
Workload: P1 (arrival 50, 40 s), P2 (20, 70 s), P3 (0, 50 s), P4 (10, 100 s), P5 (70, 50 s). **Assumptions:** quantum 30 s, context-switch time 0, a newly arrived process is put at the tail of the ready queue **before** the process whose quantum has just expired (computed with a short script).

```gantt
# Round robin, q = 30
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

Queue notes: at $t=30$ the queue is $P4, P2$ then $P3$; at 60 $P2, P3, P1$ (P1 arrived at 50), then $P4$; and so on.

| Process | Arrival | Burst | Completion | Turnaround |
|:-:|:-:|:-:|:-:|:-:|
| P1 | 50 | 40 | 240 | 190 |
| P2 | 20 | 70 | 300 | 280 |
| P3 | 0 | 50 | 110 | 110 |
| P4 | 10 | 100 | 310 | 300 |
| P5 | 70 | 50 | 290 | 220 |

$$\text{average turnaround}=\frac{190+280+110+300+220}{5}=\frac{1100}{5}=\mathbf{220}\text{ s}$$
