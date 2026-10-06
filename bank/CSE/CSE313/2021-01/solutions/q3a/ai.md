---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Mutual exclusion, hold and wait, no preemption, circular wait; they are necessary but not sufficient (deadlock needs an unlucky interleaving)."
sources: ["Tanenbaum MOS 4e, sec. 6.2 (introduction to deadlocks, Coffman conditions)"]
---
**The four necessary conditions** for a resource deadlock (Coffman et al.):

1. **Mutual exclusion:** each resource is either assigned to exactly one process or is available.
2. **Hold and wait:** a process holding a resource may request additional resources.
3. **No preemption:** a resource cannot be forcibly taken from the process holding it; only the holder can release it.
4. **Circular wait:** there is a circular chain of two or more processes, each waiting for a resource held by the next one in the chain.

**They are not sufficient.** Example: two processes and two resources $R$ and $S$ that satisfy conditions 1-3, where $P_1$ executes `lock(R); lock(S); ...; unlock(S); unlock(R)` and $P_2$ executes `lock(S); lock(R); ...; unlock(R); unlock(S)`. A deadlock requires the *unlucky interleaving* in which $P_1$ gets $R$ and $P_2$ gets $S$ before either asks for its second resource. If the scheduler happens to run $P_1$ to completion before $P_2$ starts (or the processes simply do not overlap), no circular wait ever forms and **no deadlock occurs**, although the system *could* deadlock. So the four conditions describe when deadlock is *possible*; whether it actually happens depends on the order of requests and on scheduling.
