---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**Thrashing** occurs when the total memory demand (working sets) of the currently-running processes exceeds available physical memory, so the system spends nearly all its time evicting and re-fetching pages via disk I/O rather than doing useful work.

**Why it's a problem:** as more processes are added (or memory pressure rises), CPU utilization initially increases with the degree of multiprogramming, but past a certain point (the "knee" of the curve) each additional process causes so much extra paging that overall throughput *collapses* -- the system looks extremely busy (disk constantly active) yet gets very little real work done, since almost every memory reference misses and triggers an expensive page fault.

**Solutions:**

- **Working-Set Model**: track each process's working set (the set of pages it has referenced in a recent time window) and only schedule/keep resident processes whose entire working set fits in memory (admission control based on working-set size).

- **Page-Fault-Frequency (PFF) algorithm**: monitor each process's page-fault rate; if it is too high, give the process more frames (it needs them); if too low, take some frames away and give them to a process that needs them more.

- **Reduce the degree of multiprogramming**: temporarily suspend/swap out entire processes so the remaining ones have enough memory to run without thrashing.

- **Local (per-process) replacement**: restrict a process to evicting only its own frames, so one thrashing process cannot steal frames from (and thereby drag down) other well-behaved processes.

- **Add more physical memory** (the most direct, if often impractical, hardware fix).
