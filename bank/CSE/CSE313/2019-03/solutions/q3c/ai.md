---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Mutual exclusion, hold and wait, no preemption, circular wait; prevent deadlock by attacking circular wait with a global resource order, proved by considering the highest-numbered resource held."
sources: ["Tanenbaum MOS 4e, sec. 6.2.1 and 6.6.4 (attacking the circular wait condition)"]
---
**Four conditions for a resource deadlock:**

1. **Mutual exclusion:** each resource is held by at most one process or is free.
2. **Hold and wait:** processes holding resources can request more.
3. **No preemption:** granted resources cannot be forcibly taken away.
4. **Circular wait:** a circular chain of processes, each waiting for a resource held by the next.

**Most feasible prevention: attack the circular wait condition.** (Mutual exclusion cannot usually be removed, holding all resources at once wastes resources and often is impossible, and preemption of e.g. printers is not realistic.) Give all resources a **global number** and require that processes request resources **only in increasing numerical order** (a process holding resource $i$ may later request only $j>i$).

**Proof of correctness.** Suppose, for contradiction, that a deadlock occurs, i.e. there is a cycle $P_1\to P_2\to\dots\to P_k\to P_1$ in which each $P_i$ holds a resource $r_i$ and waits for $r_{i+1}$ held by $P_{i+1}$. Because of the rule, $P_i$ holds $r_i$ and requests $r_{i+1}$ only if $\text{number}(r_{i+1})>\text{number}(r_i)$. Going round the cycle we get $\text{number}(r_1)<\text{number}(r_2)<\dots<\text{number}(r_k)<\text{number}(r_1)$, which is impossible. Hence no cycle can exist.

Equivalently: at any instant, one of the held resources has the **highest** number; its holder never asks for an already assigned resource (it can only ask for higher-numbered ones, which are free), so it can finish and release, then the holder of the next-highest can finish, and so on; all processes can finish, so there is no deadlock.
