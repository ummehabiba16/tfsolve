---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Convoy effect: in FCFS short I/O-bound processes queue behind a long CPU-bound one, leaving devices idle and lengthening mean waiting time."
sources: ["Tanenbaum MOS 4e, sec. 2.4.2; Silberschatz, convoy effect"]
---
**Convoy effect** in First-Come First-Served scheduling: a long CPU-bound process holds the CPU, and **many short (I/O-bound) processes pile up in the ready queue behind it**, like a line of cars behind a slow truck.

- While the CPU-bound process runs (its burst may be very long), the I/O-bound processes cannot even start their next short bursts, so the **I/O devices are idle**.
- When the CPU-bound process finally blocks for I/O, the short processes run quickly one after the other, issue their I/O and block; the CPU is now idle until they return, and the cycle repeats.

Result: poor utilisation of CPU and devices and a long **average waiting time**.

**Example.** One CPU-bound job of 100 ms arrives first, followed by three jobs of 2 ms. FCFS: waiting times $0, 100, 102, 104$, mean $=76.5$ ms. If the short jobs ran first: $0, 2, 4, 6$, mean $=3$ ms. Shortest-job-first or preemptive scheduling (RR, priorities) avoids the convoy.
