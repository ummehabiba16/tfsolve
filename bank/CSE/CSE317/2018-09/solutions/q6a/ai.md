---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* (graph search, h = straight-line distance) expands A(51), C(52), F(63), B(92), D(93), L(104), K(109), M(109); route A-L-K-M, cost 109."
sources: ["AIMA 3e sec. 3.5.2"]
---
Notation: each node is written $n\,(g + h = f)$. Road lengths from the map; $h$ = straight-line distance to M. Previously expanded towns are not re-visited; if a cheaper path to a town on the frontier is found, it replaces the old one.

| Step | Expand | New frontier entries (g + h = f) | Frontier after the step (sorted by f) |
|:-:|:--|:--|:--|
| 1 | A (0 + 51 = 51) | B (42+50=92), C (20+32=52), L (48+56=104) | C 52, B 92, L 104 |
| 2 | C (20 + 32 = 52) | F (49+14=63); L via C (60+56=116) worse, ignored | F 63, B 92, L 104 |
| 3 | F (49 + 14 = 63) | K (91+41=132), J (89+32=121) | B 92, L 104, J 121, K 132 |
| 4 | B (42 + 50 = 92) | D (65+28=93) | D 93, L 104, J 121, K 132 |
| 5 | D (65 + 28 = 93) | E (107+42=149) | L 104, J 121, K 132, E 149 |
| 6 | L (48 + 56 = 104) | K via L (68+41=109) replaces K 132 | K 109, J 121, E 149 |
| 7 | K (68 + 41 = 109) | M (109+0=109) | M 109, J 121, E 149 |
| 8 | M (109 + 0 = 109) | goal reached | |

**Order of expansion:** A, C, F, B, D, L, K, M.

**Search tree** (cost at each node as $g+h=f$; nodes marked x were generated but not expanded):

```text
A (0+51=51)
+-- B (42+50=92)
|   +-- D (65+28=93)
|       +-- E (107+42=149) x
+-- C (20+32=52)
|   +-- F (49+14=63)
|       +-- J (89+32=121)  x
|       +-- K (91+41=132)  x (replaced by the cheaper K below)
+-- L (48+56=104)
    +-- K (68+41=109)
        +-- M (109+0=109)  GOAL
```

**Route found:** A $\to$ L $\to$ K $\to$ M, cost $48+20+41=$ **109**.

This is optimal: the heuristic never overestimates (e.g. $h(L)=56\le61$, $h(F)=14\le72$), so A* returns the cheapest route. The alternative routes are A-C-F-J-M (121) and A-C-F-K-M (132).
