---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Learn h from solved instances: describe states by features (e.g. x1 = misplaced tiles, x2 = adjacent tile pairs not adjacent in the goal) and fit h(n) = c1 x1(n) + c2 x2(n) to the actual solution costs (regression, or a neural network). A relaxed problem has fewer restrictions on the actions; its optimal cost is an admissible heuristic for the original (e.g. Manhattan distance)."
sources: ["AIMA 3e sec. 3.6.2-3.6.4 (Relaxed problems, Learning heuristics from experience)"]
---
**Learning heuristics from experience.** The heuristic $h(n)$ should estimate the cost of a solution from $n$. "Experience" means solving many problem instances and recording, for each state $n$ on a solution path, its true cost to the goal $h^*(n)$. These (state, cost) pairs are training examples; an inductive learning algorithm builds a function that predicts the cost for new states.

Learning works best from **features** of a state rather than the raw state.

**Example: 8-puzzle (sliding puzzle).**

1. Generate (e.g.) 100 random 8-puzzle configurations and solve them optimally (with IDA*), recording the actual cost from every state on each solution path.

2. Describe each state by features, e.g.

- $x_1(n)$ = number of misplaced tiles,

- $x_2(n)$ = number of pairs of adjacent tiles that are not adjacent in the goal state.

3. Fit a model, e.g. a linear combination

$$h(n)=c_1x_1(n)+c_2x_2(n)$$

choosing the constants by least-squares regression to the recorded costs. For instance, if states with $x_1=5$ typically have cost about 14, the learned $c_1$ reflects that. Neural networks, decision trees or reinforcement learning can be used instead.

The learned heuristic is usually accurate and fast to compute, but it is **not guaranteed to be admissible** (it may overestimate), so A* with it may lose optimality.

**Relaxed problem.** A problem with **fewer restrictions on the actions** than the original. Its state-space graph is a supergraph of the original (extra edges), so the cost of an optimal solution to the relaxed problem is an **admissible** (and consistent) heuristic for the original.

8-puzzle rule: "a tile can move from square A to square B if A is horizontally or vertically adjacent to B **and** B is blank." Relaxations:

- remove both conditions: a tile can move anywhere $\to$ $h_1$ = number of misplaced tiles;

- remove "B is blank": a tile can move to any adjacent square $\to$ $h_2$ = sum of Manhattan distances;

- remove "A adjacent to B": a tile can move into the blank from anywhere $\to$ Gaschnig's heuristic.
