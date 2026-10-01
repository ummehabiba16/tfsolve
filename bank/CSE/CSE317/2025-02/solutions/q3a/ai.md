---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "BFS: 1,2,...,11. DLS (limit 3): 1,2,4,8,9,5,10,11. IDS: [1]; [1,2,3]; [1,2,4,5,3,6,7]; [1,2,4,8,9,5,10,11]. Bidirectional works very well: the predecessor of k is floor(k/2), so backward branching factor is 1 (forward 2); in fact backward search alone gives 11,5,2,1."
sources: ["AIMA 3e Exercise 3.15 and sec. 3.4"]
---
The state space is a binary tree: node $k$ has children $2k$ and $2k+1$; children are generated left ($2k$) first.

```text
                 1
           /           \
         2               3
       /   \           /   \
      4     5         6     7
     / \   / \       / \   / \
    8   9 10  11   12  13 14  15
```

**(i) Order of visits** (goal 11, stop when 11 is visited):

- **Breadth-first search**: level by level: $1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11$.

- **Depth-limited search, limit 3** (root at depth 0): $1, 2, 4, 8, 9, 5, 10, 11$.

- **Iterative deepening search**:

| Limit | Nodes visited |
|:-:|:--|
| 0 | 1 |
| 1 | 1, 2, 3 |
| 2 | 1, 2, 4, 5, 3, 6, 7 |
| 3 | 1, 2, 4, 8, 9, 5, 10, 11 |

**(ii) Bidirectional search.** It works very well. In the forward direction the branching factor is **2** (children $2k$, $2k+1$). In the backward direction each state $k>1$ has exactly one predecessor, $\lfloor k/2 \rfloor$, so the branching factor is **1**.

Searching backwards from 11 gives $11 \to 5 \to 2 \to 1$ immediately; the frontiers meet after about $d/2$ steps, with cost $O(2^{d/2})$ forward and $O(d)$ backward. In fact, since the backward direction has no branching, backward search alone solves the problem in $d$ steps: the path is $1\to2\to5\to11$ (read the binary representation of 11 = 1011: after the leading 1, 0 = left, 1 = right).
