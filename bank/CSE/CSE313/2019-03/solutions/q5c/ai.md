---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FCFS: average turnaround 8.9 s, average response 4.9 s; RR (q=2): average turnaround 10.3 s, average response 2.1 s."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2-2.4.3; OSTEP ch. 7"]
---
**Assumptions.** Switching time $=0$. In round robin a process that arrives during a quantum is placed in the ready queue **before** the process whose quantum has just expired. *Response time* = first time on the CPU $-$ arrival; *turnaround* = completion $-$ arrival.

**i. FCFS** (arrival order A, B, C, D, E):

```gantt
# FCFS
A 0 3
B 3 9
C 9 13
D 13 18
E 18 20
```

| Process | Arrival | Burst | Start | Finish | Turnaround | Response |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 0 | 3 | 0 | 3 | 3 | 0 |
| B | 1.8 | 6 | 3 | 9 | 7.2 | 1.2 |
| C | 3.2 | 4 | 9 | 13 | 9.8 | 5.8 |
| D | 5.6 | 5 | 13 | 18 | 12.4 | 7.4 |
| E | 7.9 | 2 | 18 | 20 | 12.1 | 10.1 |

Average turnaround $=44.5/5=\mathbf{8.9}$ s; average response $=24.5/5=\mathbf{4.9}$ s.

**ii. Round robin, quantum 2 s:**

```gantt
# Round robin, q = 2
A 0 2
B 2 4
A 4 5
C 5 7
B 7 9
D 9 11
C 11 13
E 13 15
B 15 17
D 17 19
D 19 20
```

| Process | Arrival | Finish | Turnaround | First run | Response |
|:-:|:-:|:-:|:-:|:-:|:-:|
| A | 0 | 5 | 5 | 0 | 0 |
| B | 1.8 | 17 | 15.2 | 2 | 0.2 |
| C | 3.2 | 13 | 9.8 | 5 | 1.8 |
| D | 5.6 | 20 | 14.4 | 9 | 3.4 |
| E | 7.9 | 15 | 7.1 | 13 | 5.1 |

Average turnaround $=51.5/5=\mathbf{10.3}$ s; average response $=10.5/5=\mathbf{2.1}$ s.

RR gives a much better (shorter) response time but a longer average turnaround than FCFS. (Both schedules were produced by a short simulation script.)
