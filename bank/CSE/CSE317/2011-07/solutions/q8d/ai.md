---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Minimax values: node 5 = 1 and node 2 = 1; node 15 = -4, node 8 = 10, node 18 = 2, node 9 = 20, node 3 = 10; node 11 = -6, node 4 = -6; root = 10. Alpha-beta prunes node 23 (under 15, once -4 <= alpha = 1), nodes 18 and 19 together with their subtrees (under 9, once 20 >= beta = 10), and node 11 with 20 and 21 (under 4, once -5 <= alpha = 10). The root's minimax value is 10."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning)"]
---
**Tree** (Figure 8(d); upward triangles are MAX, downward are MIN). MAX root 1 has MIN children 2, 3, 4.

- 2: MAX 5 (MIN leaves 12 = $-5$, 13 = 1), MAX leaf 6 = 2, MAX leaf 7 = 3.
- 3: MAX 8 (MIN 14 = $-3$; MIN 15 with MAX leaves 22 = $-4$ and 23 = 10; MIN 16 = 10), and MAX 9 (MIN 17 = 20; MIN 18 with MAX leaves 24 = 2 and 25 = 3; MIN 19 = $-10$).
- 4: MAX leaf 10 = $-5$, and MAX 11 (MIN leaves 20 = $-6$, 21 = $-7$).

**Alpha-beta trace** ($[\alpha,\beta]$):

1. Node 1 $[-\infty,\infty]$, then node 2, then node 5: leaves 12 = $-5$ and 13 = 1, so node 5 = 1. Node 2 has $\beta=1$. Leaves 6 = 2 and 7 = 3 do not lower it, so **node 2 = 1**. Root $\alpha=1$.
2. Node 3 $[1,\infty]$, then node 8 $[1,\infty]$: leaf 14 gives $-3$. Node 15 $[1,\infty]$: leaf 22 gives $-4\le\alpha=1$, so **prune 23**; node 15 = $-4$. Leaf 16 = 10, so **node 8 = 10**. Node 3 has $\beta=10$.
3. Node 9 $[1,10]$: leaf 17 gives $20\ge\beta=10$, so **prune 18 (with 24, 25) and 19**. Node 9 = 20. **Node 3** $=\min(10,20)=$ **10**. Root $\alpha=10$.
4. Node 4 $[10,\infty]$: leaf 10 gives $-5\le\alpha=10$, so **prune 11 (with 20, 21)**. Node 4 = $-5$, a bound; its true minimax value is $-6$.
5. **Root** $=\max(1,10,-5)=$ **10**. MAX moves to node 3.

**Minimax value of the root: 10.**

**Pruned nodes:** 23; 18, 24, 25, 19; 11, 20, 21.

Visited order: 1, 2, 5, 12, 13, 6, 7, 3, 8, 14, 15, 22, 16, 9, 17, 4, 10. (Checked with a script; plain minimax gives the same root value, 10.)
