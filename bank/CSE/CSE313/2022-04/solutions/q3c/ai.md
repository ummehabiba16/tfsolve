---
author: ai
via: chat
status: unverified
summary: 'No deadlock: the graph has no cycle. Resource 2 is free and wanted by A, C, D, but contention for a free resource is not deadlock.'
sources: [Deadlocks slides 16-19, 'Tanenbaum, MOS 4e, sec. 6.4.1']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
Edges, assignment: $1\to A,\ 3\to A,\ 4\to B,\ 5\to E$. Request: $A\to 2,\ B\to 3,\ B\to 5,\ C\to 2,\ D\to 2,\ E\to 1$. Resource 2 is held by no one.

Detection from B (depth-first with visited list $L$):

1. $L=\{B\}$. B$\to$3, held by A $\Rightarrow$ visit A. $L=\{B,A\}$.
2. A$\to$2; resource 2 is free (no holder) $\Rightarrow$ dead end; back up, remove A.
3. B$\to$5, held by E $\Rightarrow$ visit E. $L=\{B,E\}$.
4. E$\to$1, held by A $\Rightarrow$ visit A; A$\to$2 free $\Rightarrow$ dead end; back up.
5. No unvisited edges remain $\Rightarrow$ no cycle from B.

No cycle $\Rightarrow$ no deadlock. Processes A, C, D all want resource 2; since 2 is free it can be granted to one of them, that is resource contention, not deadlock.
