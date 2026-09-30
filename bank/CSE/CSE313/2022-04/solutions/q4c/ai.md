---
author: ai
via: chat
status: unverified
summary: 'Batch goals: maximise throughput, minimise turnaround time, and maximise CPU utilisation.'
sources: [Scheduling slides 12-14, 'Tanenbaum, MOS 4e, sec. 2.4']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
- Throughput: maximise the number of jobs completed per unit time.
- Turnaround time: minimise the time from submission to completion.
- CPU utilisation: keep the CPU as busy as possible.

(Batch systems favour non-preemptive or long-quantum algorithms, since there are no impatient interactive users.)
