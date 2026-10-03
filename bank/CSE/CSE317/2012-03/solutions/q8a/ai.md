---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Grid with moves Right and Down only, G at the bottom-left. BFS (Right first): S, 1, 4, 2, 5, 8, 3, 6, 9, G (path S-4-8-G). DFS (Right first): S, 1, 2, 3, 7, 11, 14, 6, 10, 13, 5, 9, 12, 4, 8, G (it explores the whole right part before going down the left column). DFS (Down first): S, 4, 8, G."
sources: ["AIMA 3e sec. 3.4.1 and 3.4.3 (BFS, DFS)"]
---
**Graph** (Figure 8a): a $4\times4$ grid with directed edges **Right** and **Down**:

```text
 S  -> 1  -> 2  -> 3
 |     |     |     |
 4  -> 5  -> 6  -> 7
 |     |     |     |
 8  -> 9  -> 10 -> 11
 |     |     |     |
 G  -> 12 -> 13 -> 14
```

$G$ is reachable only through the left column: $S\to4\to8\to G$. The goal test is done when a node is expanded (popped), and visited nodes are not re-added.

**(i) Breadth-first search, Right before Down** (FIFO queue):

| Expanded | Queue after |
|:--|:--|
| S | 1, 4 |
| 1 | 4, 2, 5 |
| 4 | 2, 5, 8 |
| 2 | 5, 8, 3, 6 |
| 5 | 8, 3, 6, 9 |
| 8 | 3, 6, 9, G |
| 3 | 6, 9, G, 7 |
| 6 | 9, G, 7, 10 |
| 9 | G, 7, 10, 12 |
| **G** | goal |

Order: **S, 1, 4, 2, 5, 8, 3, 6, 9, G** (10 nodes). Path S, 4, 8, G.

**(ii) Depth-first search, Right before Down** (LIFO stack, Right child explored first):

Order: **S, 1, 2, 3, 7, 11, 14, 6, 10, 13, 5, 9, 12, 4, 8, G** (16 nodes). It goes right along the top row, then down the right column to 14 (a dead end). It backtracks through 6, 10, 13, then 5, 9, 12, and only finally reaches 4, 8, G.

**(iii) Depth-first search, Down before Right:**

Order: **S, 4, 8, G** (4 nodes): it goes straight down the left column to the goal.

So DFS can be very fast or very slow depending on the order of successors, while BFS is independent of luck but explores level by level.
