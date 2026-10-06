---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "SJF: order P2, P3, P1, P4 with average turnaround 53.25; RR (q=8): average turnaround 77.25."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2-2.4.3 (SJF, round-robin)"]
---
All four processes arrive at time 0; durations: P1 = 30, P2 = 10, P3 = 19, P4 = 56 (total 115).

**i. Shortest Job First** (order of increasing duration: P2, P3, P1, P4):

```gantt
# SJF
P2 0 10
P3 10 29
P1 29 59
P4 59 115
```

| Process | P1 | P2 | P3 | P4 |
|:--|:-:|:-:|:-:|:-:|
| Turnaround | 59 | 10 | 29 | 115 |

$$\text{average turnaround}=\frac{59+10+29+115}{4}=\frac{213}{4}=\mathbf{53.25}$$

**ii. Round Robin, quantum 8** (queue order P1, P2, P3, P4):

```gantt
# Round robin, q = 8
P1 0 8
P2 8 16
P3 16 24
P4 24 32
P1 32 40
P2 40 42
P3 42 50
P4 50 58
P1 58 66
P3 66 69
P4 69 77
P1 77 83
P4 83 115
```

(P4 is alone from time 83 and runs on, shown as one bar.)

| Process | P1 | P2 | P3 | P4 |
|:--|:-:|:-:|:-:|:-:|
| Completion = turnaround | 83 | 42 | 69 | 115 |

$$\text{average turnaround}=\frac{83+42+69+115}{4}=\frac{309}{4}=\mathbf{77.25}$$

SJF gives the lowest possible average turnaround; RR is fairer for response but longer in turnaround. (Computed with a short script.)
