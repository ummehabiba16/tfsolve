---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "DFS can go down an infinite or very deep branch (incomplete, not optimal); depth-limited search fixes this with a limit l but fails if l < d (incomplete) and may find a non-shallowest goal if l > d. IDS tries l = 0, 1, 2, ..., so it finds the shallowest goal (complete; optimal for unit costs) with DFS's O(bd) memory, at a small re-expansion overhead (O(b^d) time)."
sources: ["AIMA 3e sec. 3.4.4-3.4.5"]
---
**Pitfalls.**

- **Depth-first search:** follows one branch as deep as possible. In infinite (or very deep) state spaces it can descend forever and never find a shallow goal, so it is **incomplete**. It may also return a deep, non-optimal solution.
- **Depth-limited search** with limit $\ell$ avoids infinite descent. But if $\ell<d$ (the shallowest goal depth, usually unknown) it **fails** (incomplete), and if $\ell>d$ it may return a goal deeper than the best one (**non-optimal**).

**How iterative deepening search (IDS) addresses them.** IDS runs depth-limited search repeatedly with **$\ell=0,1,2,\dots$** until a goal is found.

- No limit has to be guessed. The first limit at which a goal appears is exactly $d$, so the **shallowest** goal is found. IDS is **complete** (finite branching factor) and **optimal** for equal step costs.
- Each iteration is a depth-first search, so the memory stays **$O(bd)$**.
- The re-expansion of shallow levels costs little: the total number of nodes generated is $db+(d-1)b^2+\dots+b^d=O(b^d)$, about 11% more than BFS for $b=10$.
