---
author: ai
via: chat
status: unverified
summary: A process requesting a resource held only by processes already in a deadlock cycle is also blocked forever, though not itself on the cycle.
sources: ['Deadlocks slides 7, 10-13', 'Tanenbaum, MOS 4e, sec. 6.4.2']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
Take a cycle $P_1\to R_1\to P_2\to R_2\to P_1$ ($P_1,P_2$ deadlocked). Add $P_3$ requesting $R_1$ (single instance), held by $P_1$. $P_3$ is off the cycle, but $R_1$ is never released, so $P_3$ waits forever, part of the deadlocked set without being in the circular chain.
