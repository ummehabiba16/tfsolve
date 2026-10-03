---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Tree search with admissible h: if a suboptimal goal G2 is in the frontier, f(G2) = g(G2) > C*, while some node n on an optimal path has f(n) = g(n) + h(n) <= C*; so n (and eventually the optimal goal) is expanded before G2. Graph search with consistent h: f is non-decreasing along paths, so nodes are expanded in non-decreasing f order and the first goal expanded is optimal."
sources: ["AIMA 3e sec. 3.5.2 (optimality of A*)"]
---
**Setting.** A\* expands the node with the lowest $f(n)=g(n)+h(n)$. Let $C^*$ be the cost of the optimal solution. Assume step costs $\ge\epsilon>0$ and a finite branching factor.

**Proof 1: tree search, admissible $h$** ($h(n)\le h^*(n)$ for all $n$).

Suppose a **suboptimal** goal $G_2$ is in the frontier, so $g(G_2)>C^*$. Because $h(G_2)=0$:

$$f(G_2)=g(G_2)+h(G_2)=g(G_2)>C^*.$$

As long as the optimal goal has not been expanded, some node $n$ on an optimal path is in the frontier, since the frontier always separates the explored region from the rest. For $n$, admissibility gives

$$f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*.$$

So $f(n)\le C^*<f(G_2)$, and A\* expands $n$ before $G_2$. Repeating the argument along the optimal path, the optimal goal is selected for expansion before $G_2$. Hence **A\* returns an optimal solution**.

**Proof 2: graph search, consistent $h$** ($h(n)\le c(n,a,n')+h(n')$).

1. *$f$ is non-decreasing along any path:* $f(n')=g(n)+c(n,a,n')+h(n')\ge g(n)+h(n)=f(n)$.
2. *When A\* selects $n$ for expansion, the optimal path to $n$ has been found.* Otherwise, by the separation property, some node $n''$ on the optimal path to $n$ would still be in the frontier, with $f(n'')\le f(n)$ by step 1, and it would be selected first.
3. So the nodes are expanded in non-decreasing order of $f$. The first goal node selected has $h=0$, so $f=g$ = its true cost, and every other goal has $f\ge$ this value. **It is optimal.**

(Also, A\* expands all nodes with $f(n)<C^*$, and none with $f(n)>C^*$: it is optimally efficient.)
