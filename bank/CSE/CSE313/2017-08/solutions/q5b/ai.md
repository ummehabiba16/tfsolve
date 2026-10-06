---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A multithreaded sum splits the 2^64 additions among threads whose partial sums are added at the end: with p cores the time falls by about p (plus small overhead); on one core there is no gain."
sources: ["Tanenbaum MOS 4e, sec. 2.2 (threads); Amdahl's law"]
---
**Task.** Sum all $2^{64}$ possible 64-bit integers, i.e. perform $2^{64}\approx1.8\times10^{19}$ additions.

**Single-threaded:** one loop does all additions; at $10^9$ additions per second it takes about $1.8\times10^{10}$ s, i.e. **about 585 years**.

**Multithreaded design:** split the range into $p$ equal sub-ranges, one thread per sub-range, each computing a **private partial sum**; at the end the partial sums are added (the main thread does `join` and adds $p$ numbers). Because the partial sums are private there is **no need for locking** inside the loops.

**Effect on the time.**

- On a **multiprocessor/multicore** machine with $p$ cores the threads really run in parallel, so the time is about $T/p$ plus the tiny cost of creating the threads and combining the results: a near-linear **speed-up** (about $p\times$, limited by $p$ cores and memory/overhead); the serial part is negligible (Amdahl's law).
- On a **single CPU** the threads take turns, so there is **no speed-up** (the total work is the same; the context switches add a little overhead, making it slightly slower).
- If the threads updated one shared sum, locking would serialise them and destroy the gain; hence private partial sums.
