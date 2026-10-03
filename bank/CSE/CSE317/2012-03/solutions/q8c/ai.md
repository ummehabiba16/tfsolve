---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Completeness: the algorithm is guaranteed to find a solution whenever one exists (and to report failure otherwise). Optimality: the solution it returns has the lowest path cost among all solutions."
sources: ["AIMA 3e sec. 3.3.2 (measuring problem-solving performance)"]
---
**Completeness.** A search algorithm is **complete** if it is **guaranteed to find a solution whenever one exists** (and, ideally, reports failure when none exists).

- BFS is complete if the branching factor is finite. DFS is not complete in infinite state spaces, or with loops (tree search), because it can descend forever.

**Optimality.** A search algorithm is **optimal** if the solution it returns has the **lowest path cost** among all solutions.

- Uniform-cost search, and A\* with an admissible (or consistent) heuristic, are optimal. BFS is optimal only when all step costs are equal. DFS and greedy best-first search are not optimal.

(Together with time and space complexity, these are AIMA's four criteria for evaluating search strategies.)
