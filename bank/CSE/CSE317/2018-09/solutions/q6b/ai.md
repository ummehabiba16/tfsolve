---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* is optimal if h is admissible (tree search) or consistent (graph search), with finite branching and positive step costs. Pruning: nodes with f > C* = 109 (J, E and towns beyond them: G, H, I) are never expanded. Contours: A* expands in bands of increasing f (51, 52, 63, 92, 93, 104, 109) and stops at the contour f = C*."
sources: ["AIMA 3e sec. 3.5.2 (Figure 3.25, contours)"]
---
**Conditions for optimality of A*.**

1. **Admissible heuristic**: $h(n)\le h^*(n)$ for every $n$ (never overestimates); sufficient for A* tree search.

2. **Consistent (monotone) heuristic**: $h(n)\le c(n,a,n')+h(n')$ for every successor $n'$; required for A* graph search (which does not re-open closed nodes). Consistency implies admissibility. Straight-line distance is consistent by the triangle inequality.

3. Also (for completeness): finite branching factor and every step cost $\ge\epsilon>0$.

**Pruning in Q6(a).** A* expands every node with $f(n)<C^*$ and no node with $f(n)>C^*$, where $C^*=109$. In Q6(a):

- J ($f=121$) and E ($f=149$) were generated but never expanded, and the old path to K ($f=132$) was dropped.

- Therefore G, H, I (reached only through E or J) were never even generated: the whole subtree below them is **pruned** without being examined, while A* is still guaranteed optimal. This is what makes A* efficient: eliminating possibilities without looking at them.

**Cost contours.** Since $f$ is non-decreasing along any path (consistent $h$), A* expands nodes in bands (contours) of increasing $f$, like contour lines on a map. Inside the contour $f\le c$ are all nodes with $f\le c$. In Q6(a) A* expanded nodes in the order $f$ = 51 (A), 52 (C), 63 (F), 92 (B), 93 (D), 104 (L), 109 (K, M): it first explores the contour around A in the direction of M, then widens to B, D and L. The search stops at the contour $f=C^*=109$. With a good heuristic the contours stretch toward the goal (narrow bands around the optimal path); with $h=0$ (uniform-cost search) they would be circles around A and many more towns (E, G, J, ...) would be expanded.
