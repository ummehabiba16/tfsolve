---
author: ai
via: chat
status: unverified
summary: One long CPU-bound job at the head of the FCFS queue makes short I/O-bound jobs wait and bunch up, idling the I/O devices, a convoy.
sources: [Scheduling slides 19-27, 'Tanenbaum, MOS 4e, sec. 2.4.2']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Example: jobs arrive as one CPU-bound job $C$ (needs 100 ms CPU) followed by three I/O-bound jobs, each needing 1 ms CPU then I/O. Under FCFS, $C$ holds the CPU for 100 ms while the three short jobs wait; when $C$ finally yields they all run briefly and rush to I/O together. While $C$ ran the I/O devices sat idle, and while the short jobs do I/O the CPU sits idle, throughput collapses.
