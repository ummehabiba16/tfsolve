---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Round robin: Q=1 average turnaround 11.1 s, Q=2 10.3 s, Q=4 10.3 s (schedules as in the Gantt charts)."
sources: ["Tanenbaum MOS 4e, sec. 2.4.3 (round-robin scheduling)"]
---
Assumptions: switching time 0; a process that arrives while another runs joins the ready queue **before** the preempted process; consecutive slices of the same process are drawn as one bar. (Schedules computed with a short script.)

**(i) $Q=1$**

```gantt
# Q = 1
A 0 2
B 2 3
A 3 4
B 4 5
C 5 6
B 6 7
D 7 8
C 8 9
B 9 10
E 10 11
D 11 12
C 12 13
B 13 14
E 14 15
D 15 16
C 16 17
B 17 18
D 18 20
```

Completion times: A 4, E 15, C 17, B 18, D 20; turnaround (completion $-$ arrival): A 4, B 16.2, C 13.8, D 14.4, E 7.1; average $=55.5/5=11.1$ s.

**(ii) $Q=2$**

```gantt
# Q = 2
A 0 2
B 2 4
A 4 5
C 5 7
B 7 9
D 9 11
C 11 13
E 13 15
B 15 17
D 17 20
```

Completion times: A 5, C 13, E 15, B 17, D 20; average turnaround $=51.5/5=10.3$ s.

**(iii) $Q=4$**

```gantt
# Q = 4
A 0 3
B 3 7
C 7 11
D 11 15
B 15 17
E 17 19
D 19 20
```

Completion times: A 3, C 11, B 17, E 19, D 20; average turnaround $=51.5/5=10.3$ s.

A smaller quantum gives a better response time but more switching (here 0 cost), while a very large quantum behaves like FCFS.
