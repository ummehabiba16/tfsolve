---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Condition: h admissible (tree search) or consistent (graph search). Proof: if a suboptimal goal G2 is in the frontier, f(G2) = g(G2) > C*, while a frontier node n on an optimal path has f(n) = g(n) + h(n) <= g(n) + h*(n) = C*; so n (and eventually the optimal goal) is expanded before G2."
sources: ["AIMA 3e sec. 3.5.2 (optimality of A*)"]
---
**Optimality condition.** A\* is optimal if $h$ is **admissible**, $h(n)\le h^*(n)$ for all $n$ (tree search), or **consistent**, $h(n)\le c(n,a,n')+h(n')$ (graph search).

**Proof** (tree search, admissible $h$). Let $C^*$ be the cost of an optimal solution. Assume a suboptimal goal node $G_2$ appears in the frontier, so $g(G_2)>C^*$. Since $h(G_2)=0$:

$$f(G_2)=g(G_2)+h(G_2)=g(G_2)>C^*.$$

Until an optimal goal is expanded, some node $n$ on an optimal solution path is in the frontier. Because $h$ is admissible:

$$f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*.$$

So $f(n)\le C^*<f(G_2)$. A\* always expands the lowest-$f$ node, so it expands $n$ before $G_2$. Applying the argument repeatedly along the optimal path, the **optimal goal is selected for expansion before $G_2$**. A\* therefore never returns a suboptimal solution, so it is optimal.

(For graph search with a consistent $h$: $f$ is non-decreasing along paths, and when a node is expanded its optimal path has been found. So nodes are expanded in non-decreasing $f$ order, and the first goal expanded is optimal.)
