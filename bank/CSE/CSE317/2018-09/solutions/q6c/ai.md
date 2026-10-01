---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy best-first (f = h) expands A(51), C(32), F(14), J(32), M(0): route A-C-F-J-M, cost 121. It is not optimal: A* found A-L-K-M with cost 109."
sources: ["AIMA 3e sec. 3.5.1"]
---
Greedy best-first search expands the frontier node with the smallest $h(n)$ (straight-line distance to M), ignoring the path cost so far. Expanded towns are not re-visited.

| Step | Expand (h) | Children added (h) | Frontier (sorted by h) |
|:-:|:--|:--|:--|
| 1 | A (51) | B (50), C (32), L (56) | C 32, B 50, L 56 |
| 2 | C (32) | F (14) (L already on frontier) | F 14, B 50, L 56 |
| 3 | F (14) | J (32), K (41) | J 32, K 41, B 50, L 56 |
| 4 | J (32) | I (50), M (0) | M 0, K 41, B 50, I 50, L 56 |
| 5 | M (0) | goal | |

**Route:** A $\to$ C $\to$ F $\to$ J $\to$ M, cost $20+29+40+32=$ **121**.

**Is it optimal?** No. A* in Q6(a) found A $\to$ L $\to$ K $\to$ M with cost **109** < 121. Greedy search is attracted by C and F because they look close to M (small $h$), but it ignores that reaching them and continuing via J is expensive; it never considers the cost already spent. (The question prints "optional", meaning "optimal".)
