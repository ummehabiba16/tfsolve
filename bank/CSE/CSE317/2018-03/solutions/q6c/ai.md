---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "f(n) = (2-w)g(n) + w h(n) is proportional to g(n) + (w/(2-w)) h(n); for 0 <= w <= 1, w/(2-w) <= 1, so the scaled heuristic is still admissible and the search is optimal. w = 0: f = 2g, uniform-cost search; w = 1: f = g + h, A*; w = 2: f = 2h, greedy best-first search."
sources: ["AIMA 3e Exercise 3.30 (heuristic path algorithm)", "AIMA 3e sec. 3.5"]
---
**Optimality.** For $0\le w<2$ (so that $2-w>0$), dividing by $2-w$ does not change the order of expansion:

$$f(n)=(2-w)\Big[g(n)+\frac{w}{2-w}\,h(n)\Big]\ \propto\ g(n)+h'(n),\qquad h'(n)=\frac{w}{2-w}\,h(n).$$

So the algorithm is **A\* with heuristic $h'$**. A\* is optimal if $h'$ is admissible. Since $h$ is admissible, $h'(n)\le h^*(n)$ whenever

$$\frac{w}{2-w}\le1\iff w\le2-w\iff w\le1.$$

**The algorithm is guaranteed optimal for $0\le w\le1$.** For $1<w\le2$ the heuristic is inflated ($h'$ may overestimate), so optimality is lost, although the search is often faster.

**Special cases.**

- **(i) $w=0$:** $f(n)=2g(n)$, ordered by $g$, so it is **uniform-cost search**.
- **(ii) $w=1$:** $f(n)=g(n)+h(n)$, so it is **A\* search** (optimal).
- **(iii) $w=2$:** $f(n)=2h(n)$, ordered by $h$ only, so it is **greedy best-first search** (not optimal).
