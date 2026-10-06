---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FCFS order P1, P3, P4, P2: average turnaround 23.25, throughput 4 jobs in 36 time units = 0.111 per unit."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2 (first-come first-served)"]
---
Arrival order: P1 (0), P3 (2), P4 (4), P2 (5). FCFS serves in arrival order:

```gantt
# FCFS
P1 0 10
P3 10 26
P4 26 32
P2 32 36
```

| Process | Arrival | Duration | Start | Finish | Turnaround |
|:-:|:-:|:-:|:-:|:-:|:-:|
| P1 | 0 | 10 | 0 | 10 | 10 |
| P3 | 2 | 16 | 10 | 26 | 24 |
| P4 | 4 | 6 | 26 | 32 | 28 |
| P2 | 5 | 4 | 32 | 36 | 31 |

$$\text{average turnaround}=\frac{10+24+28+31}{4}=\frac{93}{4}=\mathbf{23.25}$$

$$\text{throughput}=\frac{4\text{ processes}}{36\text{ time units}}=\mathbf{0.111}\text{ processes per time unit}$$
