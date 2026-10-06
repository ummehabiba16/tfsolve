---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Non-preemptive: the CPU is kept until the process finishes or blocks (FCFS, non-preemptive SJF); preemptive: the OS can take the CPU away (RR, SRTN, preemptive priority)."
sources: ["Tanenbaum MOS 4e, sec. 2.4.1 (preemptive and non-preemptive scheduling)"]
---
- **Non-preemptive scheduling:** once the CPU has been allocated to a process, it keeps the CPU until it **terminates or blocks voluntarily** (I/O, waiting) or releases it. No timer interrupt is used to take it away. *Examples:* First-Come First-Served (FCFS), non-preemptive Shortest Job First (SJF), non-preemptive priority scheduling.
- **Preemptive scheduling:** the OS can **forcibly suspend** a running process (by a clock interrupt, or because a higher-priority/shorter process arrives) and give the CPU to another one. It needs a hardware timer and careful handling of shared data. *Examples:* Round Robin, Shortest Remaining Time Next (SRTN), preemptive priority scheduling, multilevel feedback queues.
