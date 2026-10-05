---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Admissible heuristic: h(n) <= h*(n) (never overestimates the true cost to the goal). A* tree search is optimal: if a suboptimal goal G2 is in the frontier, f(G2) = g(G2) > C*, while some node n on an optimal path has f(n) = g(n) + h(n) <= g(n) + h*(n) = C*, so n is always expanded before G2, and the optimal goal is selected first."
sources: ["AIMA 3e sec. 3.5.2 (optimality of A*)"]
---
**Admissible heuristic.** $h$ is admissible if it **never overestimates** the true cost of reaching a goal from $n$:

$$0\le h(n)\le h^*(n)\quad\text{for every }n\ (\text{so }h(G)=0).$$

Then $f(n)=g(n)+h(n)$ never overestimates the cost of the best solution through $n$. Example: straight-line distance in route finding.

**Theorem.** A\* with TREE-SEARCH (which allows revisiting states) is optimal if $h$ is admissible.

**Proof.** Let $C^*$ be the optimal solution cost, and suppose a **suboptimal** goal node $G_2$ is in the frontier, so $g(G_2)>C^*$. Since $h(G_2)=0$:

$$f(G_2)=g(G_2)>C^*.$$

As long as no optimal goal has been expanded, there is a frontier node $n$ on an optimal solution path (the root is on it, and the frontier always contains a descendant of it along that path). For this $n$:

$$f(n)=g(n)+h(n)\le g(n)+h^*(n)=C^*.$$

Hence $f(n)\le C^*<f(G_2)$, so A\* expands $n$ before $G_2$. Repeating the argument along the optimal path, an **optimal goal is selected before $G_2$**, and A\* never returns the suboptimal goal. A\* tree search with an admissible heuristic is therefore optimal. (Step costs must be $\ge\epsilon>0$ and the branching factor finite, for completeness.)
