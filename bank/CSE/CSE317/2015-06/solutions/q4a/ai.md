---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A* is optimal when h is admissible (tree search) or consistent (graph search). Example: with h(B) = 5 > h*(B) = 2, A* first reaches the goal by the worse path A-C-G (cost 4) instead of A-B-G (cost 3)."
sources: ["AIMA 3e sec. 3.5.2 (conditions for optimality: admissibility and consistency)"]
---
**Conditions for optimality.**

1. **Admissibility** (needed for tree search): $h(n)\le h^*(n)$ for every $n$. The heuristic never overestimates the true cost to reach the goal, so $f(n)=g(n)+h(n)$ never overestimates the cost of the best solution through $n$.
2. **Consistency (monotonicity)** (needed for graph search): $h(n)\le c(n,a,n')+h(n')$ for every successor $n'$, a triangle inequality. Consistency implies admissibility, and makes $f$ non-decreasing along every path.

**Why this is necessary: an example where $h$ overestimates.** Graph: $A\to B$ (cost 1), $B\to G$ (cost 2), $A\to C$ (cost 2), $C\to G$ (cost 2). The optimal path is $A$-$B$-$G$ with cost **3**. Let $h(B)=5$ (overestimate, since $h^*(B)=2$), $h(C)=1$ and $h(G)=0$.

- Expand $A$: $f(B)=1+5=6$, $f(C)=2+1=3$.
- Expand $C$ (lowest $f$): $f(G)=4+0=4$.
- The lowest $f$ is now $G$ (4 < 6), so A\* returns $A$-$C$-$G$ with cost **4**. **Not optimal.**

With an admissible $h(B)\le2$, $f(B)\le3<4$, so $B$ is expanded first and the optimal $G$ (cost 3) is found.

**Proof sketch for admissible $h$.** If a suboptimal goal $G_2$ is in the frontier, $f(G_2)=g(G_2)>C^*$, while some node $n$ on an optimal path has $f(n)\le C^*$. So $n$ is always expanded before $G_2$, and the optimal goal is selected first.
