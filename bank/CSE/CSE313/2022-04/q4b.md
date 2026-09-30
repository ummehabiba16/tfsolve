---
marks: 24
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 26}
note: The question does not state whether a lower or higher number means higher priority (priority_convention = null). 'approval times' is printed on the paper (presumably arrival times).
params:
  type: scheduling_workload
  time_unit: sec
  priority_convention: null
  processes:
  - {pid: P1, priority: 3, burst: 70, arrival: 40}
  - {pid: P2, priority: 1, burst: 40, arrival: 0}
  - {pid: P3, priority: 1, burst: 100, arrival: 10}
  - {pid: P4, priority: 2, burst: 50, arrival: 70}
  algorithms:
  - {name: SJF, preemptive: false}
  - {name: RR, quantum: 30, queue_order: arrival}
  - name: priority
    class_policies:
      all: {policy: RR, quantum: 30}
    separate_fifo_queues: null
  asks: [gantt, avg_turnaround]
---
Consider the following workload. Draw the Gantt chart and calculate the average turnaround time for each of the following scheduling algorithms.

(i) Non-preemptive Shortest Job First

(ii) Round Robin with quantum 30 sec. Consider the processes enter FIFO queue according to their approval times.

(iii) Priority Scheduling. Within the same priority class, schedule according to the scheduling algorithm mentioned in (ii).

| Process | Priority | Duration (sec) | Arrival (sec) |
|:--|:-:|:-:|:-:|
| P1 | 3 | 70 | 40 |
| P2 | 1 | 40 | 0 |
| P3 | 1 | 100 | 10 |
| P4 | 2 | 50 | 70 |
