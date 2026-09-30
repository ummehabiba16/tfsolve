---
marks: 10
topics: [optimal-batch-order]
kind: numerical
source: {page: 13}
params:
  type: batch_jobs
  run_times: [9, 3, 5, X]
  arrival: all_at_t0
  preemptive: false
  objective: min_avg_turnaround
---
Four jobs have arrived at the same time in a batch system. Their expected run times are 9, 3, 5, and X. In what order should they be run to obtain optimal average turnaround time? (Hint: The jobs are non-preemptive)
