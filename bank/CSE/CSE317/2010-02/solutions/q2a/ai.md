---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Alpha-beta keeps alpha (MAX's best so far) and beta (MIN's best so far) and prunes a node's remaining children as soon as its value is known to be outside [alpha, beta], giving the same decision as minimax. No improvement with the worst ordering: e.g. MAX root with MIN children (2, 3) and (5, 4): after the first MIN = 2, alpha = 2, but the second MIN's first leaf 5 > 2 gives no cutoff and the leaf 4 > 2 must also be examined, so all 4 leaves are visited."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning, move ordering)"]
---
**Principle of alpha-beta pruning.** Minimax search with two bounds carried down the depth-first search:

- $\alpha$ = the best (highest) value found so far for **MAX** along the current path;
- $\beta$ = the best (lowest) value found so far for **MIN**.

At a MIN node, once its value $v\le\alpha$, MAX will never let play reach it, so its remaining children are **pruned**. At a MAX node, once $v\ge\beta$, MIN will avoid it, so its remaining children are pruned. The result is **the same minimax value and decision**, without examining branches that cannot affect it. With perfect ordering it examines $O(b^{m/2})$ nodes instead of $O(b^m)$.

**When alpha-beta does not improve the search cost.** Pruning depends on move ordering. If the best moves are always examined **last**, no cutoff ever happens, and every node is visited, the same as minimax.

*Example:* MAX root with two MIN children: $m_1$ = (2, 3) and $m_2$ = (5, 4).

- $m_1=\min(2,3)=2$, so the root has $\alpha=2$.
- At $m_2$: leaf 5 gives $v=5>\alpha$, no cutoff. Leaf 4 gives $v=4>\alpha$, still no cutoff. $m_2=4$.
- Root $=\max(2,4)=4$. **All 4 leaves were examined: no saving.**

With $m_2$'s leaves ordered (1, ...) or (2, ...), the first leaf $\le\alpha$ would cut off the rest. With a better root ordering (examine $m_2$ first), the cutoff can happen in $m_1$.
