---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Tree search: if h is admissible, when a suboptimal goal G2 is on the frontier every node n on an optimal path has f(n) <= C* < f(G2), so n is expanded before G2. Graph search: if h is consistent, f is non-decreasing along paths, so nodes are expanded in non-decreasing f and the first goal expanded is optimal."
sources: ["AIMA 3e sec. 3.5.2 (Conditions for optimality)"]
---
Let $C^*$ be the cost of an optimal solution, $g(n)$ the path cost to $n$, $h(n)$ the heuristic and $f(n)=g(n)+h(n)$. Step costs are positive.

**Definitions.** $h$ is *admissible* if $h(n)\le h^*(n)$ for all $n$ (never overestimates). $h$ is *consistent* if $h(n)\le c(n,a,n')+h(n')$ for every successor $n'$, and $h(goal)=0$.

**1. A* tree search is optimal if $h$ is admissible.**

Suppose a suboptimal goal $G_2$ is on the frontier, with $g(G_2)>C^*$. Since $h(G_2)=0$,

$$f(G_2)=g(G_2)>C^*$$

Let $n$ be a frontier node on an optimal path to the optimal goal $G$ (such a node always exists until $G$ is expanded). Admissibility gives

$$f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*$$

Hence $f(n)\le C^*<f(G_2)$, so A* expands $n$ before $G_2$. Repeating the argument, every node on the optimal path is expanded before $G_2$; therefore $G$ is selected before $G_2$ and A* returns an optimal solution.

**2. A* graph search is optimal if $h$ is consistent.**

(a) *$f$ is non-decreasing along any path.* If $n'$ is a successor of $n$:

$$f(n')=g(n)+c(n,a,n')+h(n')\ge g(n)+h(n)=f(n)$$

(b) *When A* selects a node $n$ for expansion, the optimal path to $n$ has been found.* Otherwise there would be a node $n''$ on the frontier lying on the optimal path to $n$ (graph separation property); by (a), $f(n'')\le f(n)$ along that path, and $f(n'')<f(n)$ because the path through $n''$ is cheaper, so $n''$ would have been selected first. Contradiction.

From (a) and (b), A* expands nodes in non-decreasing order of $f$. The first goal node selected has $h=0$, so $f=g$ is the true cost, and every later goal has $f\ge$ this value. Therefore the first goal expanded is optimal.

(Consistency implies admissibility: by induction on the number of steps to the goal, $h(n)\le c(n,a,n')+h(n')\le c(n,a,n')+h^*(n')=h^*(n)$.) A* with these conditions is also complete (finite branching, step cost $\ge\epsilon$) and optimally efficient.
