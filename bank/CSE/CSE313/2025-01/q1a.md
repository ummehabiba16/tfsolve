---
marks: 15
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 8}
note: Preemption across priority classes is not stated in this version of the question (unlike 2023-24 Q2(a)).
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
      all:
        policy: RR
        quantum_schedule:
        - {first_n_quanta: 5, quantum: 20}
        - {thereafter: true, quantum: 30}
    separate_fifo_queues: true
    higher_priority_preempts_running: null
  asks: [gantt, avg_turnaround]
---
Consider the following workload. Construct the Gantt chart and calculate the average turnaround time for Priority Scheduling algorithm. Within the same priority class, schedule according to Round Robin with quantum size q. For the first 5 quantums, quantum size q = 20 secs; and for the rest of the quantums, quantum size q = 30 secs. Note that each priority class maintains separate FIFO queue.

| Process | Priority (lowest number = highest) | Duration (sec) | Arrival (sec) |
|:--|:-:|:-:|:-:|
| P1 | 1 | 30 | 0 |
| P2 | 2 | 40 | 30 |
| P3 | 2 | 65 | 50 |
| P4 | 1 | 70 | 70 |
