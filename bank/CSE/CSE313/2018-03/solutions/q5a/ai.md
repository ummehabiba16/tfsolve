---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Multiprogramming keeps several programs in memory so the CPU runs another while one waits for I/O; on a single CPU it raises utilisation (1 - p^n) provided processes are not all CPU-bound."
sources: ["Tanenbaum MOS 4e, sec. 2.1.1 (modeling multiprogramming)"]
---
**Multiprogramming** means keeping **several processes in memory at the same time**, so that when the running process blocks (for I/O, for example) the CPU is switched to another ready process, instead of idling.

**On a single CPU, does it improve efficiency?** **Yes**, although only one process executes at any instant (there is no true parallelism). A process spends a fraction $p$ of its time waiting for I/O; with $n$ processes in memory the probability that all are waiting is $p^n$, so

$$\text{CPU utilisation}=1-p^{\,n}$$

Example: with $p=0.8$ (heavily I/O-bound) a single process gives $20\%$ utilisation, but 5 processes give $1-0.8^5\approx67\%$ and 10 processes about $89\%$. CPU utilisation and **throughput** rise because the CPU time that would be idle during I/O is used by other processes.

**Limits.** If the processes are all CPU-bound ($p\approx0$) multiprogramming gives no gain and adds context-switch overhead; and it needs enough memory to hold the processes (otherwise thrashing).
