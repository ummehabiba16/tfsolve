---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Four criteria: completeness (finds a solution if one exists), optimality (finds the least-cost solution), time complexity (nodes generated) and space complexity (nodes stored), measured with b, d, m (and C*, epsilon); also search cost vs total cost."
sources: ["AIMA 3e sec. 3.3.2 (Measuring problem-solving performance)"]
---
A search algorithm is evaluated on four criteria:

1. **Completeness**: is the algorithm guaranteed to find a solution when there is one (and report failure when there is none)?

2. **Optimality**: does it find the optimal solution, i.e. the one with the lowest path cost?

3. **Time complexity**: how long it takes, measured as the number of nodes generated (or expanded).

4. **Space complexity**: how much memory it needs, measured as the maximum number of nodes stored in memory.

Complexity is expressed in terms of:

- $b$: branching factor (maximum number of successors of a node),

- $d$: depth of the shallowest goal node,

- $m$: maximum length of any path in the state space,

- for cost-based searches, $C^*$ (optimal solution cost) and $\epsilon$ (minimum step cost).

Example: BFS is complete, optimal for unit costs, $O(b^d)$ time and space; DFS is incomplete, not optimal, $O(b^m)$ time, $O(bm)$ space.

**Effectiveness.** We can also consider the **search cost** (time and memory used to find the solution) and the **total cost** = search cost + path cost of the solution found. An agent may trade a slightly worse solution for much less search time (e.g. greedy or weighted A*).
