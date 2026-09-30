---
author: ai
via: chat
status: unverified
summary: CPU-bound = long CPU bursts, rare I/O; I/O-bound = short CPU bursts with frequent I/O. Putting a CPU-bound job ahead of I/O-bound jobs in FCFS causes the convoy effect.
sources: ['Scheduling slides 5-7, 19-27', 'Tanenbaum, MOS 4e, sec. 2.4']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
- CPU-bound process: long CPU bursts, infrequent I/O (e.g. video encoding); limited by CPU speed.
- I/O-bound process: short CPU bursts followed by I/O waits (e.g. a shell); limited by device speed. Its short CPU bursts should be served quickly to overlap CPU and I/O.

Convoy effect (FCFS): put one CPU-bound job ahead of several I/O-bound jobs. The CPU-bound job holds the CPU a long time while the I/O-bound jobs queue behind it and the devices idle. When it finishes, the short jobs run briefly and all move to I/O together, now idling the CPU. The mismatch throttles throughput.
