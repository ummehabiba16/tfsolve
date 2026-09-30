---
marks: 18
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 13}
params:
  type: scheduling_workload
  time_unit: sec
  priority_convention: lowest_number_highest
  processes:
  - {pid: P1, priority: 1, burst: 60, arrival: 0}
  - {pid: P2, priority: 1, burst: 25, arrival: 30}
  - {pid: P3, priority: 2, burst: 80, arrival: 50}
  - {pid: P4, priority: 3, burst: 20, arrival: 70}
  algorithms:
  - {name: SRTN}
  - name: priority
    class_policies:
      all: {policy: RR, quantum: 20}
    separate_fifo_queues: true
    higher_priority_preempts_running: null
  asks: [gantt, avg_turnaround]
---
Consider the following workload. Draw the Gantt chart and calculate the average turnaround time for each of the following scheduling algorithms: (1) Shortest Remaining Time Next; (2) Priority Scheduling. Within the same priority class, schedule according to Round Robin with quantum 20 sec. Each priority class maintains separate FIFO queue.

| Process | Priority (lowest number = highest) | Duration (sec) | Arrival (sec) |
|:--|:-:|:-:|:-:|
| P1 | 1 | 60 | 0 |
| P2 | 1 | 25 | 30 |
| P3 | 2 | 80 | 50 |
| P4 | 3 | 20 | 70 |
