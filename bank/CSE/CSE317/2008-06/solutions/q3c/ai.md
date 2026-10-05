---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Yes, in terms of nodes generated: if BFS applies the goal test when a node is expanded, it generates the whole level d+1 (about b^{d+1} nodes) before finding a goal at depth d, while IDS never goes below depth d (about b^d b/(b-1) nodes); e.g. b = 10, d = 5: BFS generates about 11,111,100 nodes, IDS 123,450. With the goal test at generation, BFS (111,110) generates slightly fewer."
sources: ["AIMA 3e sec. 3.4.1 and 3.4.5 (BFS and IDS node counts)"]
---
**Yes, it can**, depending on when BFS applies the goal test.

- **IDS** generates nodes only down to depth $d$, the shallowest goal depth:

$$N(IDS)=d\,b+(d-1)\,b^2+\dots+1\cdot b^d=O(b^d).$$

- **BFS with the goal test applied when a node is expanded** (selected): before it selects the goal at depth $d$, it must expand the other level-$d$ nodes in front of it, generating their children at depth $d+1$. In the worst case it generates almost the whole of level $d+1$:

$$N(BFS_{late})=b+b^2+\dots+b^d+(b^{d+1}-b)=O(b^{d+1}).$$

*Example:* $b=10$, $d=5$, goal at the right end of level 5:

| Algorithm | Nodes generated |
|:--|:-:|
| BFS (goal test on expansion) | about 11,111,100 |
| IDS | 123,450 |
| BFS (goal test on generation) | 111,110 |

So **IDS generates fewer nodes than BFS when BFS tests for the goal late**, because IDS never generates nodes deeper than $d$, while BFS generates almost a whole extra level. With the goal test at generation time, BFS generates slightly fewer nodes than IDS (about 11% fewer for $b=10$).

