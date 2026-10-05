---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Minimax: E = 3, F = 8, G = 7, so B = 3; H = 1, I = 5, so C = 1; J = 8, K = 10, so D = 8; root A = 8. (ii) MAX should move to D. (iii) Alpha-beta (left to right) does not examine O, Q, the whole subtree I (T, U) and Y."
sources: ["AIMA 3e sec. 5.2-5.3 (minimax, alpha-beta pruning)"]
---
**Tree** (Figure 4(b)): MAX root A has MIN children B, C, D. Below them are MAX nodes E, F, G (under B), H, I (under C) and J, K (under D), with leaves L = 2, M = 3, N = 8, O = 5, P = 7, Q = 6, R = 0, S = 1, T = 5, U = 2, V = 8, W = 4, X = 10, Y = 2.

**(i) Minimax values.**

| MAX nodes | MIN nodes |
|:--|:--|
| E = max(2, 3) = 3; F = max(8, 5) = 8; G = max(7, 6) = 7 | B = min(3, 8, 7) = **3** |
| H = max(0, 1) = 1; I = max(5, 2) = 5 | C = min(1, 5) = **1** |
| J = max(8, 4) = 8; K = max(10, 2) = 10 | D = min(8, 10) = **8** |

**Root A = max(3, 1, 8) = 8.**

**(ii) MAX's move:** the move to **D**, worth 8.

**(iii) Nodes not examined with alpha-beta** (children left to right):

1. B: E = 3, so $\beta_B=3$. F: N = 8 $\ge\beta$ = 3, so **O is pruned**. G: P = 7 $\ge$ 3, so **Q is pruned**. B = 3, and the root has $\alpha=3$.
2. C $[3,\infty]$: H has R = 0 and S = 1, so H = 1 $\le\alpha$ = 3. **The whole subtree I (T, U) is pruned.** C = 1.
3. D $[3,\infty]$: J has V = 8 and W = 4, so J = 8 and $\beta_D=8$. K: X = 10 $\ge\beta$ = 8, so **Y is pruned**. D = 8.

**Not examined: O, Q, I (with T and U), and Y.** Visited order: A, B, E, L, M, F, N, G, P, C, H, R, S, D, J, V, W, K, X. (Checked with a script.)
