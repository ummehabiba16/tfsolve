---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Edges A-C, A-B, B-C, B-D, C-D, C-E, C-F, D-F, E-F; colours tried R, G, B. (i) Simple DFS (alphabetical, backtracking): A = R, B = G, C = B, D = R, E = R, F = G (F = R rejected), with no backtracking needed. (ii) Forward checking + degree heuristic: C = R (degree 5), B = G, F = G, A = B, D = B, E = B. (iii) Forward checking + MRV (ties alphabetical): A = R, B = G, C = B (only B left), D = R (forced), F = G (forced), E = R."
sources: ["AIMA 3e sec. 6.3 (backtracking search, forward checking, MRV and degree heuristics)"]
---
**Constraint graph** (fig. for Q. 8(b)): A-C, A-B, B-C, B-D, C-D, C-E, C-F, D-F, E-F. Adjacent regions must differ. Colours are tried in the order R, G, B.

```text
  A ---- C ---- E
  |    / |  \   |
  |  /   |    \ |
  B ---- D ---- F
```

**(i) Simple DFS (backtracking), variables in alphabetical order.** Each assignment is checked only against the already-assigned neighbours:

| Step | Variable | Tried | Result |
|:-:|:-:|:--|:-:|
| 1 | A | R | **A = R** |
| 2 | B | R (conflict with A), G | **B = G** |
| 3 | C | R (A), G (B), B | **C = B** |
| 4 | D | R | **D = R** (neighbours B = G, C = B) |
| 5 | E | R | **E = R** (neighbour C = B) |
| 6 | F | R (conflict with D, E), G | **F = G** |

Solution: A = R, B = G, C = B, D = R, E = R, F = G. The search never had to backtrack.

**(ii) Forward-checking DFS with the degree heuristic** (most constraints on unassigned variables first; ties broken alphabetically). The degrees are C 5, B 3, D 3, F 3, A 2, E 2.

| Step | Assign | Remaining domains after forward checking |
|:-:|:--|:--|
| 1 | **C = R** (degree 5) | A: GB, B: GB, D: GB, E: GB, F: GB |
| 2 | **B = G** (2 unassigned neighbours; tie with D and F) | A: B, D: B, E: GB, F: GB |
| 3 | **F = G** (2 unassigned neighbours: D, E) | A: B, D: B, E: B |
| 4 | **A = B** | D: B, E: B |
| 5 | **D = B** | E: B |
| 6 | **E = B** | |

Solution: C = R, B = G, F = G, A = B, D = B, E = B. No backtracking.

**(iii) Forward-checking DFS with MRV** (fewest remaining values first; ties broken alphabetically):

| Step | Assign (domain size) | Remaining domains after forward checking |
|:-:|:--|:--|
| 1 | **A = R** (all have 3; first alphabetically) | B: GB, C: GB, D: RGB, E: RGB, F: RGB |
| 2 | **B = G** (2 values) | C: B, D: RB, E: RGB, F: RGB |
| 3 | **C = B** (1 value) | D: R, E: RG, F: RG |
| 4 | **D = R** (1 value) | E: RG, F: G |
| 5 | **F = G** (1 value) | E: R |
| 6 | **E = R** (1 value) | |

Solution: A = R, B = G, C = B, D = R, F = G, E = R. No backtracking.

(All three traces were checked with a script. On this graph none of the methods needs to backtrack. Forward checking and the heuristics avoid even the conflicts that simple DFS meets.)

*Note:* the end of the question ("show only ...") is blacked out on the scan, so each algorithm's sequence of assignments and domain reductions is shown.
