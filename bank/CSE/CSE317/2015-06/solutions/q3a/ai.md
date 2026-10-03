---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) A binary tree with 2n and 2n+1 as children of n, nodes 1-25 (depth 0-4). (ii) BFS visits 1-19 in order (19 nodes); DFS (left child first) visits 1, 2, 4, 8, 16, 17, 9, 18, 19; DLS with limit 4 gives the same 9 nodes; IDS does limits 0-4: 1 | 1,2,3 | 1,2,4,5,3,6,7 | 1,2,4,8,9,5,10,11,3,6,12,13,7,14,15 | 1,2,4,8,16,17,9,18,19 (35 nodes). (iii) DFS / DLS(4) are fastest here (9 nodes). (iv) Bidirectional: forward branching factor 2, backward branching factor 1 (the parent of n is floor(n/2)), so backward search alone (19, 9, 4, 2, 1) is enough."
sources: ["AIMA 3e sec. 3.4 and Exercise 3.15"]
---
**(i) State space for states 1 to 25.** Node $n$ has children $2n$ and $2n+1$ (those above 25 are not drawn):

```text
depth 0:                                 1
                         /                               \
depth 1:                2                                 3
                  /          \                      /           \
depth 2:         4             5                   6              7
               /   \         /   \               /   \          /    \
depth 3:      8     9      10     11           12     13       14     15
             / \   / \     / \    / \          / \
depth 4:   16 17  18 19  20 21  22 23        24 25
```

**(ii) Order of visiting with goal 19** (children in increasing order; the goal test is applied when a node is visited). Node 19 is at depth 4, on the path $1\to2\to4\to9\to19$.

| Strategy | Nodes visited, in order | Count |
|:--|:--|:-:|
| Breadth-first | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, **19** | 19 |
| Depth-first | 1, 2, 4, 8, 16, 17, 9, 18, **19** | 9 |
| Depth-limited, limit 4 | 1, 2, 4, 8, 16, 17, 9, 18, **19** | 9 |
| Iterative deepening | limit 0: 1. Limit 1: 1, 2, 3. Limit 2: 1, 2, 4, 5, 3, 6, 7. Limit 3: 1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 12, 13, 7, 14, 15. Limit 4: 1, 2, 4, 8, 16, 17, 9, 18, **19** | 1+3+7+15+9 = 35 |

**(iii) Least time.** Here, **depth-first search** (and depth-limited search with limit 4) finds 19 after visiting only **9 nodes**, against BFS's 19 and IDS's 35. This is because 19 lies in the left half of the tree. (DFS would be much worse if the goal were on the right, or if the tree were infinite.)

**(iv) Bidirectional search.** Search forward from 1 and backward from 19 until the frontiers meet.

- Forward successors: $2n$ and $2n+1$, so the **branching factor is 2**.
- Backward (predecessor of $n$): only $\lfloor n/2\rfloor$, so the **branching factor is 1**.

Backward search alone, $19\to9\to4\to2\to1$, reaches the start in 4 steps with no branching. So bidirectional search, or simply backward search, works very well here. The meeting point is at depth about 2 (e.g. forward $\{2,3\}$, backward $\{19,9,4\}$), with $O(b^{d/2})$ work forward.
