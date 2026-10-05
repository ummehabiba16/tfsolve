---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Admissible heuristics can be invented from (1) relaxed problems (fewer restrictions on the actions: the relaxed optimal cost is admissible, e.g. Manhattan distance or misplaced tiles for the 8-puzzle), (2) subproblems and pattern databases (the exact cost of solving part of the problem, e.g. tiles 1-4), (3) learning from experience (but the learned h may not be admissible), and (4) combining heuristics with max(h1, ..., hm), which stays admissible and dominates each."
sources: ["AIMA 3e sec. 3.6.2-3.6.4 (generating admissible heuristics)"]
---
1. **Relaxed problems.** Remove restrictions from the actions. The optimal cost of the **relaxed** problem is never more than that of the real problem (every real solution is also a relaxed solution), so it is **admissible**, and also consistent.
*8-puzzle:* the rule "a tile can move from A to B if A is adjacent to B and B is blank". Relaxing it to "move to any adjacent square" gives the **Manhattan distance** $h_2$; relaxing it to "move anywhere" gives the number of **misplaced tiles** $h_1$.

2. **Subproblems and pattern databases.** The exact cost of solving a **subproblem** is a lower bound on the full problem. For example, the cost of getting tiles 1, 2, 3, 4 into place while ignoring the others. Precompute and store these costs for all configurations (a pattern database). Disjoint pattern databases can even be **added** together.

3. **Learning from experience.** Solve many instances, then learn $h(n)$ from features of states (e.g. a linear combination $c_1x_1(n)+c_2x_2(n)$) with machine learning. This gives good estimates, but they are not guaranteed to be admissible.

4. **Combining heuristics.** If $h_1,\dots,h_m$ are admissible, $h(n)=\max\{h_1(n),\dots,h_m(n)\}$ is admissible (and consistent if they are) and dominates each of them.
