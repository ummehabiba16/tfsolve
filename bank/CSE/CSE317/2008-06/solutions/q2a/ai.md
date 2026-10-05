---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "With an admissible h (tree search) or a consistent h (graph search): if a suboptimal goal G2 is in the frontier, f(G2) = g(G2) > C*, while a frontier node n on an optimal path has f(n) <= C* (h never overestimates), so A* expands n before G2 and an optimal goal is selected first."
sources: ["AIMA 3e sec. 3.5.2"]
---
**Claim.** A\* (tree search) is optimal if $h$ is admissible, $h(n)\le h^*(n)$.

**Proof.** Let $C^*$ be the cost of an optimal solution. Suppose some suboptimal goal $G_2$ is generated and is in the frontier, so $g(G_2)>C^*$. Since $h(G_2)=0$:

$$f(G_2)=g(G_2)+h(G_2)=g(G_2)>C^*.$$

Consider an optimal solution path. Until its goal has been expanded, some node $n$ on it is in the frontier, because the frontier separates the expanded nodes from the rest. For that $n$:

$$f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*,$$

since $h$ never overestimates and $g(n)$ is the optimal cost to $n$ on that path. So $f(n)\le C^*<f(G_2)$, and A\*, which always expands the frontier node of smallest $f$, expands $n$ before $G_2$. Repeating this along the path, the **optimal goal is selected for expansion before any suboptimal goal**. A\* therefore returns an optimal solution. $\blacksquare$

(For graph search, a **consistent** $h$ makes $f$ non-decreasing along paths, so nodes are expanded in non-decreasing $f$ order, and the first goal expanded is optimal.)
