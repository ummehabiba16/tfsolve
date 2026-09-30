---
author: ai
via: chat
status: unverified
summary: A process requesting a resource held only by processes already in a deadlock cycle is also blocked forever, though it is not itself on the cycle.
sources: ['Deadlocks slides 7, 10-13', 'Tanenbaum, MOS 4e, sec. 6.4.2']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Take a cycle $P_1\to R_1\to P_2\to R_2\to P_1$ ($P_1,P_2$ deadlocked, single-instance resources). Add $P_3$ that requests $R_1$, held by $P_1$. $P_3$ is not on the cycle, but $R_1$ will never be released, so $P_3$ waits forever. The deadlocked set therefore includes $P_3$ even though it lies outside the circular chain.
