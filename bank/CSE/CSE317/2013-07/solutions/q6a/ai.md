---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A* (h = given straight-line distances, tree search without returning to the parent) expands A(56), E(41), C(47), K(50), L(50), M(50); route A-K-L-M with cost 50. It is optimal (the cheapest route on the map is 50), although the heuristic is not admissible (h(A)=56, h(F)=30, h(G)=14 overestimate), so optimality was not guaranteed."
sources: ["AIMA 3e sec. 3.5.2"]
---
Road lengths (from the map): A-B 30, A-E 12, A-K 20, C-D 5, C-E 5, D-F 5, K-F 17, F-B 19, F-L 10, K-L 15, L-M 15, B-H 11, H-J 6, G-J 8, G-I 5, I-M 8. Each node is written $n\,(g+h=f)$.

**(i) Search tree and order of expansion.**

| Step | Expand | Children generated (g + h = f) | Frontier (by f) |
|:-:|:--|:--|:--|
| 1 | A (0+56=56) | B (30+22=52), E (12+29=41), K (20+30=50) | E 41, K 50, B 52 |
| 2 | E (12+29=41) | C (17+30=47) | C 47, K 50, B 52 |
| 3 | C (17+30=47) | D (22+29=51) | K 50, D 51, B 52 |
| 4 | K (20+30=50) | F (37+30=67), L (35+15=50) | L 50, D 51, B 52, F 67 |
| 5 | L (35+15=50) | F (45+30=75), M (50+0=50) | M 50, D 51, B 52, F 67, F 75 |
| 6 | M (50+0=50) | goal | |

```text
A (0+56=56)                         expanded 1st
+-- B (30+22=52)
+-- E (12+29=41)                    expanded 2nd
|   +-- C (17+30=47)                expanded 3rd
|       +-- D (22+29=51)
+-- K (20+30=50)                    expanded 4th
    +-- F (37+30=67)
    +-- L (35+15=50)                expanded 5th
        +-- F (45+30=75)
        +-- M (50+0=50)  GOAL       expanded 6th
```

Order of expansion: **A, E, C, K, L, M**. (The parent is never re-generated, as required.)

**(ii) Route and cost.** A $\to$ K $\to$ L $\to$ M, cost $20+15+15=$ **50**.

**(iii) Is it optimal?** Yes, the route is optimal: all other routes cost more, e.g. A-E-C-D-F-L-M $=12+5+5+5+10+15=52$, A-K-F-L-M $=20+17+10+15=62$, A-B-F-L-M $=30+19+10+15=74$, A-B-H-J-G-I-M $=30+11+6+8+5+8=68$.

However, A* was **not guaranteed** to find it, because the given heuristic is **not admissible**: it overestimates at some towns, e.g. $h(A)=56$ but the true cost from A is 50; $h(F)=30$ but F-L-M costs 25; $h(G)=14$ but G-I-M costs 13. A* is guaranteed optimal only with an admissible (tree search) or consistent (graph search) heuristic; here it happens to return the optimal route because the overestimates did not push the optimal path's nodes behind a suboptimal goal.
