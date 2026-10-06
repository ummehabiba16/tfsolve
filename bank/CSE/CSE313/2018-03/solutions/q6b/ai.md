---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Throughput = jobs completed per unit time; turnaround time = completion minus submission; example: jobs 3, 5, 2 s in FCFS give throughput 0.3 job/s and mean turnaround 7 s."
sources: ["Tanenbaum MOS 4e, sec. 2.4.1 (scheduling goals: throughput, turnaround time)"]
---
- **Throughput:** the number of processes (jobs) **completed per unit time**, e.g. jobs per hour. It measures how much work the system gets done.
- **Turnaround time:** the **time from submission (arrival) of a job until its completion**: the sum of the waiting time in the queue, the CPU time and the I/O time.

**Example.** Three jobs of 3 s, 5 s and 2 s arrive at time 0 and run FCFS in this order: they finish at 3, 8 and 10 s.

- Throughput $=3$ jobs $/\ 10$ s $=0.3$ job/s.
- Turnaround times: $3$, $8$, $10$ s, mean $=21/3=7$ s. (Running the 2 s job first would reduce the mean turnaround to $(2+5+10)/3\approx5.7$ s.)
