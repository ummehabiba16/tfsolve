---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Eight processes: the root creates children with i = 0, 1, 2; the child created at i = k itself creates children with i = k+1,...,2 (binomial tree)."
sources: ["OSTEP ch. 5 (fork); Tanenbaum MOS 4e, sec. 2.1.2"]
---
`i` is a **global** variable, but after each `fork` every process has **its own copy** (separate address space). At `fork` the child gets the parent's current value of `i`, then both increment it and continue the loop. Hence a child created in iteration $i=k$ **starts with $i=k$**, continues the loop with $k+1,\dots,2$ and creates children of its own.

![Process tree](figures/forktree.png)

- Iteration $i=0$: Root forks **A** ($i=0$). Now two processes, both with $i=1$ after `i++`.
- Iteration $i=1$: Root forks **B** ($i=1$), A forks **AA** ($i=1$). Four processes, all with $i=2$.
- Iteration $i=2$: Root forks **C** ($i=2$), A forks **AB** ($i=2$), B forks **BA** ($i=2$), AA forks **AAA** ($i=2$). Eight processes; all have $i=3$ and end.

Total: $2^3=8$ processes (7 created by `fork`).
