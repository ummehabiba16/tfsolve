---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Quantum = time slice of round robin; too large degrades to FCFS (poor response), too small wastes time in context switches."
sources: ["Tanenbaum MOS 4e, sec. 2.4.3 (round-robin scheduling)"]
---
**Quantum:** the fixed maximum length of CPU time a process may run in round-robin scheduling before it is preempted and put at the end of the ready queue.

- **Quantum too small:** processes are switched too often; each **context switch** costs time (e.g. 1 ms), so a large fraction of CPU time is wasted (with a 4 ms quantum and 1 ms switch, 20% of the CPU is overhead). Throughput suffers.
- **Quantum too large:** round robin degenerates into **first-come first-served**: short interactive requests wait behind long CPU-bound processes, so the **response time** becomes poor.

A compromise (typically 20-50 ms; a rule of thumb: about 80% of CPU bursts shorter than the quantum) gives good response with small overhead.
