---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A relaxed problem removes restrictions on the actions; the optimal cost of the relaxed problem is an admissible and consistent heuristic for the original. 8-puzzle: tile moves anywhere gives misplaced tiles h1; tile moves to any adjacent square gives Manhattan distance h2. Route finding: straight-line distance (relaxing 'only along roads')."
sources: ["AIMA 3e sec. 3.6.2 (Generating admissible heuristics from relaxed problems)"]
---
A **relaxed problem** is a problem with fewer restrictions on the actions than the original. Adding edges to the state space can only make shortest paths shorter, so **the optimal solution cost of a relaxed problem is an admissible heuristic** for the original problem. It is also consistent, because it is an exact cost in the relaxed space. If the relaxed problem is easy to solve (often without search), we get a cheap, good heuristic.

**Example: 8-puzzle.** Original rule: *a tile can move from square A to square B if A is adjacent to B and B is blank.* Relaxations:

1. *A tile can move from A to B if A is adjacent to B* (ignore "B is blank"): each tile needs exactly its Manhattan distance moves, so $h_2$ = **sum of Manhattan distances**.

2. *A tile can move from A to B if B is blank* (ignore adjacency): gives Gaschnig's heuristic.

3. *A tile can move from A to B* (no restrictions): each misplaced tile needs one move, $h_1$ = **number of misplaced tiles**.

For the AIMA start state, $h_1=8$, $h_2=18$, true cost 26. Since $h_2\ge h_1$ everywhere, $h_2$ dominates and A* expands fewer nodes with it (at depth 24: about 1,600 nodes vs 39,000 with $h_1$).

**Example: route finding.** Original: travel only along roads. Relaxed: travel in a straight line, giving the straight-line distance heuristic.

**Example: TSP.** Relax "the tour visits every city exactly once in a cycle" to "connect all cities with a tree": the minimum spanning tree cost is an admissible heuristic.

If several admissible relaxed heuristics are available, $h(n)=\max(h_1(n),\dots,h_m(n))$ is admissible and dominates them all.
