---
author: ai
via: chat
status: unverified
summary: 'Advantages: the kernel can run another thread when one blocks, and can spread threads over CPUs. Disadvantages: every thread operation is a system call (higher overhead) and uses more kernel memory.'
sources: [Process/Thread slides 36-38, 'Tanenbaum, MOS 4e, sec. 2.2.4']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
- Advantages: the kernel knows all threads, so if one blocks (I/O, page fault) it runs another thread of the same process; threads can be scheduled across multiple CPUs for true parallelism; no non-blocking tricks are needed.

- Disadvantages: every thread operation (create, exit, switch, synchronise) is a system call, so higher overhead and slower switches than user-level threads; more kernel memory (a control block per thread); scheduling policy is fixed by the kernel (less flexible).
