---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Exhaustive search systematically examines the whole space and guarantees completeness/optimality but is exponential; heuristic search uses domain knowledge (a heuristic) to examine promising states first, accepting the risk of non-optimal or no solution (or, for admissible A*, more memory) in exchange for speed. Examples: straight-line distance, misplaced tiles, Manhattan distance, MRV."
sources: ["AIMA 3e sec. 3.4-3.6"]
---
**Exhaustive (blind) search** systematically explores the state space using only the problem definition (BFS, DFS, UCS, IDS). If it runs to completion it is complete, and BFS/UCS/IDS are optimal. But it is exponential ($O(b^d)$), so it is feasible only for small problems: the 15-puzzle has about $10^{13}$ states, chess about $10^{40}$.

**Heuristic search** uses problem-specific knowledge, a **heuristic** $h(n)$ estimating the cost from $n$ to a goal, to decide which state to examine next (greedy best-first, A*, hill climbing). It can find solutions to large problems in a tiny fraction of the time.

| | Exhaustive search | Heuristic search |
|:--|:--|:--|
| Knowledge used | problem definition only | plus domain heuristic |
| Guarantees | complete, optimal (BFS/UCS) | depends: may lose completeness/optimality |
| Cost | exponential, explores everything | much less in practice |
| Quality depends on | nothing but problem size | quality of the heuristic |

**Compromises accepted by a heuristic approach.**

1. **Optimality** may be lost: greedy best-first or hill climbing may return a suboptimal solution (A* keeps optimality only if $h$ is admissible/consistent; weighted A* trades it for speed).

2. **Completeness** may be lost: greedy search or hill climbing can loop or get stuck in local optima/dead ends.

3. **No worst-case guarantee**: a bad heuristic can still lead to exponential work.

4. **Cost of computing $h$**: each evaluation costs time; a more accurate heuristic may be more expensive.

5. Memory (A* still stores many nodes).

**Examples of heuristics.**

- Route finding: straight-line distance to the destination (admissible).

- 8-puzzle: $h_1$ = number of misplaced tiles, $h_2$ = sum of Manhattan distances of tiles from their goal squares ($h_2$ dominates $h_1$). For the start state in AIMA, $h_1=8$, $h_2=18$, true cost 26.

- TSP: nearest-neighbour rule, or the minimum spanning tree cost as a lower bound.

- CSP: minimum remaining values and least constraining value.

- Chess: material value evaluation function.
