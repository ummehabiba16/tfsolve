---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With consistent h, f = g + h is non-decreasing along every path, and when A* selects a node its optimal path has been found; so nodes are expanded in non-decreasing f, and the first goal expanded (f = g, h = 0) is optimal. Admissibility alone gives optimality of tree search: a suboptimal goal G2 has f(G2) > C* >= f(n) for a frontier node n on the optimal path."
sources: ["AIMA 3e sec. 3.5.2"]
---
Definitions: $f(n)=g(n)+h(n)$; $h$ **admissible**: $h(n)\le h^*(n)$; $h$ **consistent**: $h(n)\le c(n,a,n')+h(n')$, $h(\text{goal})=0$. $C^*$ = optimal solution cost.

**Step 1 (consistent $\Rightarrow$ $f$ non-decreasing along paths).** For a successor $n'$ of $n$:

$$f(n')=g(n)+c(n,a,n')+h(n')$$

$$\ge g(n)+h(n)=f(n)$$

**Step 2 (A* selects every node via an optimal path).** Suppose A* selects $n$ for expansion but a cheaper path to $n$ exists. Some node $n''$ on that cheaper path is on the frontier. Since $f$ is non-decreasing along that path and the path is cheaper, $f(n'')<f(n)$, so $n''$ would have been selected first. Contradiction.

**Step 3 (conclusion).** By steps 1 and 2, A* expands nodes in non-decreasing order of $f$, each with its optimal $g$. When the first goal $G$ is selected, $h(G)=0$, so $f(G)=g(G)$, the cost of the path found. Every goal selected later has $f\ge f(G)$, i.e. cost $\ge g(G)$. Therefore the first goal selected is optimal: $g(G)=C^*$.

**Using admissibility (tree search).** Let $G_2$ be a suboptimal goal on the frontier: $f(G_2)=g(G_2)>C^*$. Let $n$ be a frontier node on an optimal path. Admissibility gives $f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*$. Thus $f(n)\le C^*<f(G_2)$, so $n$ (and then every node on the optimal path, and the optimal goal) is expanded before $G_2$. $\blacksquare$

(Consistency implies admissibility, so a consistent heuristic satisfies both arguments.)
