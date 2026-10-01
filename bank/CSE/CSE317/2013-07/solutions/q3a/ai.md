---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Root value 8. E = 8; at F, N = 9 >= beta 8 so O is pruned; B = 8, alpha = 8; at C, G = 2 <= alpha so H (R, S) and I (T, U) are pruned; at D, J = 6 <= alpha so K (Y, Z) is pruned. MAX moves to B."
sources: ["AIMA 3e sec. 5.3"]
---
Tree (from the figure): A is MAX; B, C, D are MIN; E-K are MAX; L-Z are leaves. Children are visited left to right; $[\alpha,\beta]$ starts at $[-\infty,+\infty]$.

**Steps.**

1. A (MAX) $\to$ B (MIN) $\to$ E (MAX), all $[-\infty,+\infty]$.

2. E: L = 4 $\Rightarrow v=4,\ \alpha=4$; M = 8 $\Rightarrow v=8$. **E = 8**.

3. B: $v=8$, $\beta=8$. Visit F (MAX) with $[-\infty,8]$.

4. F: N = 9 $\Rightarrow v=9\ge\beta=8$: **cut-off, O is pruned**. F returns 9.

5. B = $\min(8,9)=$ **8**. A: $v=8$, $\alpha=8$.

6. C (MIN) with $[8,+\infty]$ $\to$ G (MAX) with $[8,+\infty]$: P = 2, Q = -2 $\Rightarrow$ **G = 2**.

7. C: $v=2\le\alpha=8$: **cut-off, H (leaves R, S) and I (leaves T, U) are pruned**. C returns 2.

8. D (MIN) with $[8,+\infty]$ $\to$ J (MAX) with $[8,+\infty]$: V = 3, W = 6, X = 5 $\Rightarrow$ **J = 6**.

9. D: $v=6\le\alpha=8$: **cut-off, K (leaves Y, Z) is pruned**. D returns 6.

10. A = $\max(8,2,6)=$ **8**.

| Node | Value | Pruned below it |
|:--|:-:|:--|
| E | 8 | none |
| F | $\ge9$ | O |
| B | 8 | none |
| G | 2 | none |
| C | $\le2$ | H (R, S), I (T, U) |
| J | 6 | none |
| D | $\le6$ | K (Y, Z) |
| A | **8** | |

**Value of the root: 8**; MAX's best move is to B. Pruned branches: F-O; C-H and C-I; D-K (7 of the 15 leaves are not examined: O, R, S, T, U, Y, Z).

(Check by full minimax: E = 8, F = 9, B = 8; G = 2, H = 9, I = 8, C = 2; J = 6, K = 7, D = 6; A = 8.)
