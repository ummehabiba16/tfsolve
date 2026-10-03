---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Subgoal independence assumes the cost of a conjunction of goals is the sum of the costs of solving each subgoal separately (optimistic if subgoals help each other, pessimistic or inadmissible if they interfere). State abstraction maps the large state space to a smaller one by ignoring some fluents: in air cargo, ignore all At fluents except those of one plane and one package per airport, or ignore cargo that is already where it must go; the abstract problem is much smaller and its cost is a heuristic."
sources: ["AIMA 3e sec. 10.2.3 (decomposition, subgoal independence, state abstraction) / AIMA 4e sec. 11.3.2"]
---
**Subgoal independence.** Decompose the goal $G=g_1\land\dots\land g_n$ and assume each subgoal can be solved **independently** of the others:

$$h(s)=\sum_i\text{Cost}(g_i)\quad\text{or}\quad\max_i\text{Cost}(g_i).$$

- If the subgoal plans *interfere* (one undoes what another needs), the sum is **optimistic**, but the plans cannot simply be concatenated.
- If they *help* each other (shared actions), the sum is **pessimistic** and so inadmissible. $\max$ is always admissible but weaker.
- The assumption makes heuristics cheap. It is the idea behind pattern databases (sum of disjoint subproblem costs).

**State abstraction in the air-cargo domain.** Relaxing actions alone does not shrink the number of states. For a problem with, say, 10 airports, 50 planes and 200 cargo items, there are about $10^{50}\times(50+10)^{200}\approx10^{405}$ states. **State abstraction** maps many ground states to one abstract state by **ignoring some fluents**. Examples:

- Ignore the location of every plane and cargo except one plane and one cargo item at each airport. This leaves about $10^{5+10}=10^{15}$ abstract states.
- Ignore $At$ fluents for cargo that is already at its destination and never needs to move.
- If all cargo goes from $A$ to $B$, treat cargo items as indistinguishable and count them.

A plan in the abstract space is much shorter and easier to find. Its cost is an (admissible, if it is a relaxation) heuristic for the real problem, or its steps become subgoals that are refined into a concrete plan. In this way state abstraction makes it **easier to find a solution plan**.
