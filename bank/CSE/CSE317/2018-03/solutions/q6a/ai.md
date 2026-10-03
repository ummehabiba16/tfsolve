---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "IDS combines DFS's O(bd) memory with BFS's completeness and optimality (unit step costs), and its repeated expansion of shallow levels costs only a constant factor (about b/(b-1)). So with a large space and unknown depth it is the preferred uninformed method. Uninformed search uses only the problem definition (cannot tell which non-goal state is better); informed search uses problem-specific knowledge, a heuristic h(n) estimating the cost to the goal, to expand the most promising nodes first."
sources: ["AIMA 3e sec. 3.4.5 (iterative deepening), sec. 3.5 (informed search)"]
---
**Why iterative deepening search (IDS) is preferred.** IDS runs depth-limited DFS with limits $0,1,2,\dots$ until a goal is found.

- **Memory like DFS:** $O(bd)$, linear in the depth. BFS needs $O(b^d)$ memory, which is the real bottleneck when the space is large.
- **Complete like BFS** (when the branching factor is finite). DFS can go down an infinite or very deep branch and never return, and depth-limited search fails if the limit is below the solution depth $d$, which is unknown here.
- **Optimal** when all step costs are equal (it finds the shallowest goal).
- **Little time wasted:** the top levels are regenerated many times, but most nodes are on the bottom level. The total is

$$N(\text{IDS})=d\,b+(d-1)b^2+\dots+1\cdot b^d=O(b^d),$$

the same order as BFS. For $b=10$, $d=5$, IDS generates 123,450 nodes against BFS's 111,110: only about 11% more.

So, when the search space is large and the solution depth is unknown, IDS gets the advantages of BFS and DFS together.

**Informed versus uninformed search.**

- **Uninformed (blind)** search (BFS, UCS, DFS, IDS) uses only the problem definition: the initial state, actions, goal test and path cost. It can only generate successors and distinguish goals from non-goals; it has no idea which non-goal state is closer to a goal.
- **Informed (heuristic)** search (greedy best-first, A*, RBFS) also uses **problem-specific knowledge**, a heuristic function $h(n)$ estimating the cheapest cost from $n$ to a goal. It expands the most promising nodes first ($f(n)=h(n)$ or $g(n)+h(n)$), and usually finds solutions far more efficiently.
