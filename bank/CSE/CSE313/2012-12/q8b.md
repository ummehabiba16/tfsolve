---
marks: 15
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 69}
params:
  type: scheduling_workload
  time_unit: sec
  priority_convention: lowest_number_highest
  processes:
  - {pid: P1, priority: 4, burst: 40, arrival: 50}
  - {pid: P2, priority: 3, burst: 70, arrival: 10}
  - {pid: P3, priority: 1, burst: 50, arrival: 0}
  - {pid: P4, priority: 5, burst: 100, arrival: 0}
  - {pid: P5, priority: 2, burst: 50, arrival: 70}
  algorithms:
  - {name: SJF, preemptive: false}
  - {name: SRTN}
  - {name: RR, quantum: 30, queue_order: arrival}
  asks: [gantt, avg_waiting_time]
---
Consider the following workload: (5x3=15)

| Process | Priority (Lowest number has the highest priority) | Burst Time (sec) | Arrival Time (sec) |
|:-:|:-:|:-:|:-:|
| P1 | 4 | 40 | 50 |
| P2 | 3 | 70 | 10 |
| P3 | 1 | 50 | 0 |
| P4 | 5 | 100 | 0 |
| P5 | 2 | 50 | 70 |

Draw the Time scale diagram and calculate the average **waiting** time for the following scheduling algorithms:

(i) Non-preemptive Shortest Job First

(ii) Shortest Remaining Time First

(iii) Round Robin with quantum 30 sec.
