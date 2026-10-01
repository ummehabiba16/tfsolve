---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Assuming square nodes are MAX and circles MIN: D = 6, so B <= 6; at E, J = 8 >= beta = 6 so K is pruned; B = 6, alpha = 6 at A; at C, F = max(2,1) = 2 <= alpha so G (with N and O) is pruned. Root value 6, MAX moves to B."
sources: ["AIMA 3e sec. 5.3"]
---
**Assumption.** The figure does not say which nodes are MAX and MIN; by the usual convention the square nodes (A, D, E, F, G) are **MAX** and the circles (B, C) are **MIN**. Children are visited left to right. Leaf values: H = 6, I = 5, J = 8, K = 10, L = 2, M = 1, N = 15, O = 18.

**Trace** ($[\alpha,\beta]$ passed down; start $[-\infty,+\infty]$):

1. A (MAX) $[-\infty,\infty]$ $\to$ B (MIN) $[-\infty,\infty]$ $\to$ D (MAX) $[-\infty,\infty]$.

2. D: H = 6 $\Rightarrow$ $v=6$, $\alpha=6$; I = 5 $\Rightarrow$ $v=6$. **D = 6**.

3. Back at B: $v=6$, $\beta=6$. Go to E (MAX) with $[-\infty,6]$.

4. E: J = 8 $\Rightarrow$ $v=8\ge\beta=6$: **cut-off, K is pruned**. E returns 8 (E $\ge 8$).

5. B = $\min(6,8)=$ **6**. Back at A: $v=6$, $\alpha=6$.

6. A $\to$ C (MIN) with $[6,\infty]$ $\to$ F (MAX) with $[6,\infty]$.

7. F: L = 2 $\Rightarrow$ $v=2$; M = 1 $\Rightarrow$ $v=2$. **F = 2**.

8. At C: $v=2\le\alpha=6$: **cut-off, G is pruned (with its leaves N and O)**. C returns 2.

9. A = $\max(6,2)=$ **6**.

**Resulting search tree** (pruned parts marked //):

```text
                 [A] = 6
          /                \
      (B) = 6            (C) <= 2
      /     \             /     :
  [D]=6   [E]>=8       [F]=2   [G]   pruned
  /  \     /  :         /  \    :  :
 6    5   8   K=10     2    1  N=15 O=18
              pruned           pruned

( : = pruned edge )
```

**Pruned:** leaf K (under E) and the whole subtree of G (N, O). Root value **6**; MAX's best move is to **B**. (Minimax without pruning gives the same value: D = 6, E = 10, B = 6; F = 2, G = 18, C = 2; A = 6.)
