---
marks: 15
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 2}
note: Printed as 'Considerations the following workload'.
params:
  type: scheduling_workload
  time_unit: sec
  priority_convention: lowest_number_highest
  processes:
  - {pid: P1, priority: 1, burst: 30, arrival: 0}
  - {pid: P2, priority: 2, burst: 40, arrival: 30}
  - {pid: P3, priority: 2, burst: 65, arrival: 50}
  - {pid: P4, priority: 1, burst: 70, arrival: 70}
  algorithms:
  - name: priority
    class_policies:
      '1': {policy: RR, quantum: 30}
      '2': {policy: FCFS}
    separate_fifo_queues: true
    higher_priority_preempts_running: false
  asks: [gantt, avg_turnaround]
---
Consider the following workload. Construct the Gantt chart and calculate the average turnaround time for Priority Scheduling algorithm. Within the priority class 1, schedule according to Round Robin (RR) with quantum size 30. For the priority class 2, schedule according to First-Come First-Served (FCFS) algorithm. Note that each priority class maintains separate FIFO queue. Also note that, once a process starts executing, it continues until it completes (in FCFS) or it finishes the current quantum (in RR), even if a higher-priority process becomes ready.

| Process | Priority (lowest number = highest) | Duration (sec) | Arrival (sec) |
|:--|:-:|:-:|:-:|
| P1 | 1 | 30 | 0 |
| P2 | 2 | 40 | 30 |
| P3 | 2 | 65 | 50 |
| P4 | 1 | 70 | 70 |
