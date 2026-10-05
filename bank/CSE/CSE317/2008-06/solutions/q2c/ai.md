---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Graph search, ties broken alphabetically. (i) IDDFS: limit 0: S; limit 1: S A B; limit 2: S A B D B A C E; limit 3: S A B C E D E G (goal, path S-A-D-G). (ii) UCS: S B A C H D E F G (cost 8). (iii) A*: S B A C D E F G (path S-A-D-G, cost 8). (iv) Greedy best-first: S B E F D G (path S-B-E-D-G, cost 11, not optimal)."
sources: ["AIMA 3e sec. 3.4-3.5 (uninformed and informed search)"]
---
**Graph** (bidirectional arcs): S-A 3, S-B 2, A-B 4, A-D 3, B-E 4, B-C 1, C-H 2, D-E 3, D-G 2, E-F 1. Heuristic: $h(S)=7$, $h(A)=5$, $h(B)=4$, $h(C)=5$, $h(D)=2$, $h(E)=2$, $h(F)=1$, $h(G)=0$, $h(H)=4$.

Conventions: graph search (a state already popped is not popped again; a cheaper path to a state on OPEN replaces the older one); ties are popped in alphabetical order; the goal test is applied when a state is popped.

**(i) Iterative deepening DFS** (alphabetical successors; states already on the current path are not revisited):

| Limit | States popped (in order) |
|:-:|:--|
| 0 | S |
| 1 | S, A, B |
| 2 | S, A, B, D, B, A, C, E |
| 3 | S, A, B, C, E, D, E, **G** |

The goal is found at depth 3: S, A, D, G (cost 8).

**(ii) Uniform-cost search** (OPEN ordered by $g$):

| Pop | $g$ | Added to OPEN |
|:--|:-:|:--|
| S | 0 | A(3), B(2) |
| B | 2 | C(3), E(6) |
| A | 3 | D(6) (A's tie with C broken alphabetically) |
| C | 3 | H(5) |
| H | 5 | |
| D | 6 | G(8) (D's tie with E broken alphabetically) |
| E | 6 | F(7) |
| F | 7 | |
| **G** | 8 | goal |

**Popped:** S, B, A, C, H, D, E, F, G. Path S, A, D, G, cost **8** (optimal).

**(iii) A\*** (OPEN ordered by $f=g+h$):

| Pop | $f=g+h$ | Added |
|:--|:-:|:--|
| S | 0+7=7 | A(3+5=8), B(2+4=6) |
| B | 6 | C(3+5=8), E(6+2=8) |
| A | 8 | D(6+2=8) |
| C | 8 | H(5+4=9) |
| D | 8 | G(8+0=8) |
| E | 8 | F(7+1=8) |
| F | 8 | |
| **G** | 8 | goal |

**Popped:** S, B, A, C, D, E, F, G (ties at $f=8$ broken alphabetically). Path S, A, D, G, cost **8** (optimal, since $h$ is admissible).

**(iv) Greedy best-first search** (OPEN ordered by $h$):

| Pop | $h$ | Added |
|:--|:-:|:--|
| S | 7 | A(5), B(4) |
| B | 4 | C(5), E(2) |
| E | 2 | D(2), F(1) |
| F | 1 | |
| D | 2 | G(0) |
| **G** | 0 | goal |

**Popped:** S, B, E, F, D, G. Path S, B, E, D, G, cost **11**: **not optimal**, but few nodes were expanded.

(All four orders were checked with a script.)
