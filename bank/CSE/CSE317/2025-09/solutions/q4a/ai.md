---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* expands nodes by f(n)=g(n)+h(n): with h=0 it is uniform-cost search, with g ignored it is greedy best-first; it is complete with finite branching and positive step costs, and optimal if h is admissible (tree search) or consistent (graph search)."
sources: ["AIMA 3e sec. 3.5.1-3.5.2 (Greedy best-first, A*)"]
---
**Balance between UCS and greedy best-first.**

- Uniform-cost search orders the frontier by $g(n)$, the cost so far: optimal but uninformed, expands in all directions.

- Greedy best-first search orders by $h(n)$, the estimated cost to the goal: fast and goal-directed, but neither optimal nor complete (can follow a misleading heuristic).

- A* orders by $f(n) = g(n) + h(n)$ = estimated cost of the cheapest solution **through** $n$. It combines the past cost (like UCS) with the estimated remaining cost (like greedy). If $h\equiv0$, A* is UCS; if we weight $g$ by 0, it becomes greedy.

**Role of the heuristic.** $h(n)$ guides the search toward the goal: the more accurate it is (while still admissible), the fewer nodes A* expands. With $h=h^*$ (perfect), A* expands only nodes on an optimal path. If $h_2(n)\ge h_1(n)$ for all $n$ (both admissible), $h_2$ *dominates* and A* with $h_2$ never expands more nodes.

**Conditions for optimality and completeness.**

1. *Admissible* heuristic: $h(n)\le h^*(n)$ (never overestimates). A* **tree search** is then optimal.

2. *Consistent* (monotone) heuristic: $h(n)\le c(n,a,n')+h(n')$ for every successor $n'$. Then $f$ is non-decreasing along every path, and A* **graph search** is optimal (the first time a node is expanded, its cheapest path has been found). Consistency implies admissibility.

3. *Completeness*: finite branching factor and every step cost $\ge \epsilon > 0$ (so there are finitely many nodes with $f\le C^*$).

**Example (Romania, Arad to Bucharest, $h$ = straight-line distance).** Greedy best-first goes Arad $\to$ Sibiu $\to$ Fagaras $\to$ Bucharest, cost 450, because Fagaras looks closest. A* expands Arad ($f=366$), Sibiu ($393$), Rimnicu Vilcea ($413$), Fagaras ($415$), Pitesti ($417$), then reaches Bucharest via Pitesti with $f=418$ before the Fagaras route ($f=450$), so it returns the optimal path Arad-Sibiu-Rimnicu Vilcea-Pitesti-Bucharest, cost 418. Straight-line distance is admissible and consistent (triangle inequality), so this is guaranteed.
