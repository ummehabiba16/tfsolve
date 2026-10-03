---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "LC = Manhattan distance + 2 x (number of tiles that must be removed from each row or column to resolve linear conflicts). Manhattan = 31; row 1 holds 3, 2, 1 (all in their goal row, fully reversed): 2 tiles must move out, +4; no other conflicts. LC = 31 + 4 = 35 (goal 1..15 with the blank at the bottom right)."
sources: ["Hansson, Mayer & Yung 1992 (linear conflict heuristic)", "AIMA 3e sec. 3.6 (heuristic functions)"]
---
**Linear conflict.** Two tiles $t_j$ and $t_k$ are in *linear conflict* if they are in the same line (row or column), their goal positions are both in that line, and they are in the wrong order relative to each other. One of them must leave the line and come back, which costs at least 2 moves beyond the Manhattan distance. So

$$h_{LC}(n)=MD(n)+2\times\sum_{\text{lines }L}lc(L),$$

where $lc(L)$ = the minimum number of tiles that must be removed from line $L$ to resolve all its conflicts. $h_{LC}$ is admissible and dominates Manhattan distance.

**Pseudocode.**

```text
function LINEAR-CONFLICT(state) returns h
    h <- MANHATTAN(state)
    for each line L in rows(state) + columns(state):
        T <- tiles in L whose goal position is also in L
        lc <- 0
        while some pair of tiles in T is in conflict:
            for each tile t in T: C(t) <- number of tiles in T conflicting with t
            t* <- tile with maximum C(t)          # remove the worst offender
            T <- T - {t*};  lc <- lc + 1
        h <- h + 2 * lc
    return h
```

(Exactly: $lc(L)=|T|-$ the length of the longest subsequence of $T$ already in goal order.)

**Value for the given state** (goal: 1-15 in order, with the blank at the bottom right).

Manhattan distances, (row, col) to goal (row, col):

| Tile | 3 | 2 | 1 | 10 | 9 | 7 | 13 | 8 | 5 | 11 | 15 | 6 | 12 | 14 | 4 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| MD | 2 | 0 | 2 | 2 | 2 | 0 | 5 | 4 | 2 | 0 | 2 | 3 | 3 | 1 | 3 |

$$MD=2+0+2+2+2+0+5+4+2+0+2+3+3+1+3=31.$$

Linear conflicts:

- **Row 1** holds 3, 2, 1, all of whose goals are in row 1, in completely reversed order (goal columns 3, 2, 1). Each pair conflicts. Removing 3 still leaves (2, 1) in conflict, so **2 tiles** must leave the row: $lc=2$, adding $+4$.
- Rows 2-4: each contains at most one tile whose goal is in that row (7 in row 2, 11 in row 3, 14 in row 4), so there are no conflicts.
- Columns: column 2 has only tile 2, column 3 has 7 and 11 in the correct order, column 4 has only tile 4. No conflicts.

$$h_{LC}=31+2\times2=\mathbf{35}.$$

*Note:* if the goal puts the blank first (B, 1, 2, ... 15), the value changes; the standard goal with 1 at the top left is assumed. Checked by a script, which computed $MD=31$ and $lc=2$.
