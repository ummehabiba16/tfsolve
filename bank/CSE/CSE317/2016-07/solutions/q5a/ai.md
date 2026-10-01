---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Left to right: MIN1 = 13 (third MAX child cut after 15, pruning -5 and -12); MIN2 is cut after its first MAX child = 7 <= alpha 13 (its other two MAX children pruned); MIN3 is cut after its first MAX child = 3 (other two pruned). Root = 13; MAX takes the left move."
sources: ["AIMA 3e sec. 5.3 (Alpha-beta pruning)"]
---
Label the MIN nodes $B$ (left), $C$ (middle), $D$ (right); their MAX children $B_1,B_2,B_3$, $C_1,C_2,C_3$, $D_1,D_2,D_3$. Leaves (left to right):

| MIN node | MAX child 1 | MAX child 2 | MAX child 3 |
|:--|:-:|:-:|:-:|
| B | $B_1$: -16, 1, 18 | $B_2$: 13, 10, -2 | $B_3$: 15, -5, -12 |
| C | $C_1$: -11, -17, 7 | $C_2$: 2, 1, 0 | $C_3$: -11, -12, 5 |
| D | $D_1$: -2, -14, 3 | $D_2$: -9, -4, -7 | $D_3$: 13, -13, 19 |

**Trace** (each node shows $[\alpha,\beta]$ when entered and its final value $v$):

| Node | $[\alpha,\beta]$ in | Leaves seen | Result |
|:--|:-:|:--|:--|
| Root (MAX) | $[-\infty,+\infty]$ | | |
| B (MIN) | $[-\infty,+\infty]$ | | |
| $B_1$ (MAX) | $[-\infty,+\infty]$ | -16, 1, 18 | $v=18$; B: $\beta=18$ |
| $B_2$ (MAX) | $[-\infty,18]$ | 13 ($\alpha=13$), 10, -2 | $v=13$; B: $\beta=13$ |
| $B_3$ (MAX) | $[-\infty,13]$ | 15 $\ge\beta=13$: **cut** | $v\ge15$; **-5, -12 pruned** |
| B | | | $v=13$; Root: $\alpha=13$ |
| C (MIN) | $[13,+\infty]$ | | |
| $C_1$ (MAX) | $[13,+\infty]$ | -11, -17, 7 | $v=7$ |
| C | | $7\le\alpha=13$: **cut** | $v\le7$; **$C_2$ (2, 1, 0) and $C_3$ (-11, -12, 5) pruned** |
| D (MIN) | $[13,+\infty]$ | | |
| $D_1$ (MAX) | $[13,+\infty]$ | -2, -14, 3 | $v=3$ |
| D | | $3\le\alpha=13$: **cut** | $v\le3$; **$D_2$ (-9, -4, -7) and $D_3$ (13, -13, 19) pruned** |
| Root | | | $v=\max(13,\le7,\le3)=$ **13** |

**Pruned branches (strike through these edges):**

- under $B_3$: the edges to leaves -5 and -12;

- under C: the edges to $C_2$ and $C_3$ (and their 6 leaves);

- under D: the edges to $D_2$ and $D_3$ (and their 6 leaves).

14 of the 27 leaves are never examined.

**Values at nodes:** $B_1=18$, $B_2=13$, $B_3\ge15$, $B=13$; $C_1=7$, $C\le7$; $D_1=3$, $D\le3$; root $=13$.

**MAX's move at the root:** the **left** branch (to B), with value 13. (Check with full minimax: B = min(18, 13, 15) = 13, C = min(7, 2, 5) = 2, D = min(3, -4, 19) = -4, root = 13.)
