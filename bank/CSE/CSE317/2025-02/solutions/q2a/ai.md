---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A single chain (branching factor 1) with the only goal at depth n: DFS reaches it in n+1 node visits, while IDS repeats the chain for every limit 0..n, visiting 1+2+...+(n+1) = O(n^2) nodes."
sources: ["AIMA 3e sec. 3.4.5 (Iterative deepening) and Exercise 3.18"]
---
IDS repeats depth-limited search with limits $0,1,2,\dots$, so it re-generates the upper levels many times. This is cheap when the tree is bushy (most nodes are at the bottom), but costly when the tree is a long thin path.

**State space.** States $1,2,\dots,n$ in a single chain: state $k$ has exactly one successor $k+1$ (branching factor $b=1$), start state 1, the only goal is state $n$ (depth $n-1$).

- **DFS** goes straight down: visits $1,2,\dots,n$, i.e. $n$ nodes: $O(n)$.

- **IDS**: limit $0$ visits 1 node, limit 1 visits 2 nodes, $\dots$, limit $n-1$ visits $n$ nodes. Total

$$1+2+\cdots+n = \frac{n(n+1)}{2} = O(n^2)$$

So IDS is a factor of about $n/2$ worse.

The same happens in any space whose branching factor is close to 1, e.g. a tree where each node has one child except a few short dead-end branches, or a deep goal at the end of the left-most path that DFS happens to explore first. In contrast, for $b\ge2$ IDS costs only about $b/(b-1)$ times BFS/DFS of the last level.
