---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Lottery scheduling: random draw among tickets, CPU share proportional to tickets; convoy effect: short I/O-bound processes stuck behind a long CPU-bound one under FCFS."
sources: ["Tanenbaum MOS 4e, sec. 2.4.5 (lottery scheduling) and 2.4.2"]
---
**(i) Lottery scheduling.** Processes are given **lottery tickets** for system resources such as CPU time. At each scheduling decision a ticket is drawn **at random** and the process holding it gets the CPU for the next time slice. A process holding a fraction $f$ of the tickets gets about $f$ of the CPU time in the long run. Properties: simple and **probabilistically fair**, very **responsive** (a new process gets tickets and takes part in the next draw), important processes get more tickets (priorities without starvation: every process holding a ticket will eventually win), and cooperating processes can **exchange tickets** (e.g. a client gives its tickets to the server it waits for).

**(ii) Convoy effect.** In FCFS a **long CPU-bound process** holding the CPU makes the many **short (I/O-bound) processes** queue behind it: while it computes, the I/O devices are idle; when it finally blocks, the short processes run quickly one after another, issue their I/O and the CPU becomes idle while they wait. The result is poor CPU and device utilisation and a large average waiting time (e.g. waiting times $0,100,102,104$ for a 100 ms job followed by three 2 ms jobs). Shortest-job-first or preemptive scheduling (RR) avoids it.
