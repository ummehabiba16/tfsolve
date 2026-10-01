---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* keeps every generated node in memory (frontier plus explored set) and the number of nodes with f < C* grows exponentially with the heuristic's error, so memory (several GB) fills in minutes while running time is still acceptable; hence memory-bounded variants IDA*, RBFS, SMA*."
sources: ["AIMA 3e sec. 3.5.2-3.5.3"]
---
A* must keep **all generated nodes** in memory: the frontier (priority queue) to choose the lowest-$f$ node, and the explored set to avoid repeated states. It expands every node with $f(n)<C^*$, and the number of such nodes is in general **exponential** in the solution depth: with absolute heuristic error $\Delta=h^*-h$, the number of nodes is about $O(b^{\Delta})$, and for the effective branching factor $b^*$, $O((b^*)^d)$. So space complexity equals time complexity: $O(b^d)$ in the worst case.

Time and memory grow at the same rate, but the resources are very different:

- A computer generates millions of nodes per second. If each node needs about 100 bytes, $10^7$ nodes/s fill 1 GB of RAM in about a second, and any realistic memory within minutes.

- At that point the search may need only a few more minutes of CPU time to finish, but it cannot continue, because there is nowhere to store new nodes.

Example: A* on random 15-puzzle instances (about $10^{13}$ states) exhausts memory long before an acceptable time limit; Korf's IDA*, which uses $O(bd)$ memory, solved them.

Hence "A* runs out of space long before it runs out of time", which motivates **memory-bounded heuristic search**: IDA* (iterative deepening on $f$), RBFS (recursive best-first, linear space) and SMA* (uses all available memory and drops the worst nodes when full).
