---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Graph S-A 3, S-B 4, S-C 10, A-B 2, A-G 14, B-C 5, B-G 10, C-G 4; h(S) = 10, A 7, B 7, C 2, G 0. IDA*: bounds 10, 11, 12, 13; it finds S-B-C-G (cost 13) in the 4th iteration. RBFS: S, A (fail, f -> 12), B, C (fail: 13 > 12), back to A (12), C (12 -> 14), then B (f 13) and C (13), reaching G (13): the path S-B-C-G, cost 13 (optimal)."
sources: ["AIMA 3e sec. 3.5.3 (IDA*, RBFS)"]
---
**Graph** (undirected): $S$-$A$ 3, $S$-$B$ 4, $S$-$C$ 10, $A$-$B$ 2, $A$-$G$ 14, $B$-$C$ 5, $B$-$G$ 10, $C$-$G$ 4. Heuristic: $h(S)=10$, $h(A)=7$, $h(B)=7$, $h(C)=2$, $h(G)=0$. Nodes already on the current path are not revisited, and successors are taken in alphabetical order.

**Iterative deepening A\*.** Each iteration is a DFS that prunes nodes with $f=g+h$ greater than the bound. The next bound is the smallest pruned $f$.

| Iter. | Bound | Nodes visited ($f$), in order | Next bound |
|:-:|:-:|:--|:-:|
| 1 | 10 | S(10), A(3+7=10), B(5+7=12)x, G(17)x, B(4+7=11)x, C(10+2=12)x | 11 |
| 2 | 11 | S(10), A(10), B(12)x, G(17)x, B(11), A(6+7=13)x, C(9+2=11), G(13)x, G(14)x, C(12)x | 12 |
| 3 | 12 | S(10), A(10), B(12), C(10+2=12), G(14)x, G(15)x, G(17)x, B(11), A(13)x, C(11), G(13)x, G(14)x, C(12), B(22)x, G(14)x | 13 |
| 4 | 13 | S(10), A(10), B(12), C(12), G(14)x, G(15)x, G(17)x, B(11), A(13), G(20)x, C(11), **G(13)** | found |

(x = pruned because $f>$ bound.) **IDA\* returns S, B, C, G with cost 4 + 5 + 4 = 13.**

**Recursive best-first search.** Backed-up $f$-values are shown after "becomes".

| Call | Children ($f$) | Result |
|:--|:--|:--|
| RBFS(S, limit $\infty$) | A 10, B 11, C 12 | best A, alternative B (11) |
| RBFS(A, limit 11) | B (5+7=12), G (17) | best 12 > 11: fail, $f(A)$ becomes 12 |
| RBFS(B, limit 12) | A 13, C (9+2=11), G 14 | best C (11), alternative 13, limit 12 |
| RBFS(C, limit 12) | G (13+0=13) | 13 > 12: fail, $f(C)$ becomes 13; then B's best is 13 > 12: fail, $f(B)$ becomes 13 |
| RBFS(A, limit 12) | B 12 | B, then C (12), whose best child G 14 > 12: fail; $f(A)$ becomes 14 |
| RBFS(C, limit 13) | G (10+4=14) | 14 > 13: fail, $f(C)$ becomes 14 |
| RBFS(B, limit 14) | A 13, C 13 | A: its child G 20 > 13, fail; C (13): child **G (13)** within limit |
| RBFS(G) | | **goal: S, B, C, G, cost 13** |

Both algorithms find the **optimal path S, B, C, G (cost 13)**, using only linear memory, at the cost of re-expanding nodes. (Checked by a script.)
