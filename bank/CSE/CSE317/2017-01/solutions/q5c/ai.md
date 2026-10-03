---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Greedy search (greedy best-first with f = h, or greedy local search / hill climbing) is fast, uses little memory and is often good enough; but it is not optimal, it is incomplete (tree version: loops, dead ends; local version: local maxima, ridges, plateaux), and the worst case is O(b^m), depending entirely on h."
sources: ["AIMA 3e sec. 3.5.1 (greedy best-first search), sec. 4.1.1 (hill climbing)"]
---
"Greedy search" means making the choice that looks best right now: greedy best-first search, $f(n)=h(n)$, or greedy local search (hill climbing).

**Advantages.**

- **Fast:** with a good heuristic it heads straight for the goal and expands very few nodes. In Romania, greedy best-first search with straight-line distance finds Arad to Bucharest expanding only the nodes on the path.
- **Little memory:** hill climbing keeps only the current state, $O(1)$, and can handle huge or infinite (continuous) state spaces.
- **Simple and often good enough** in practice; it gives quick, reasonable solutions.

**Pitfalls.**

- **Not optimal:** it ignores the cost already paid, $g(n)$. Arad-Sibiu-Fagaras-Bucharest (450) is found instead of the optimal route via Rimnicu Vilcea and Pitesti (418).
- **Incomplete:** the tree-search version can loop forever, e.g. Iasi to Fagaras goes Iasi-Neamt-Iasi-Neamt..., or follow a dead end. Hill climbing gets stuck at **local maxima**, **ridges** and **plateaux** and never reaches the global optimum.
- **Heuristic-dependent:** the worst-case time and space are $O(b^m)$ ($m$ = maximum depth). A misleading $h$ leads it far astray, and there is no backtracking (hill climbing).

Remedies: A\* (add $g(n)$ for optimality), random restarts, sideways moves, simulated annealing, and beam search.
