---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A chain with branching factor 1 and the goal at depth n: DFS visits n+1 nodes (O(n)); IDS re-runs the chain for limits 0..n, visiting 1+2+...+(n+1) = O(n^2) nodes."
sources: ["AIMA 3e sec. 3.4.5 and Exercise 3.18"]
---
IDS is efficient only because, in a tree with branching factor $b\ge2$, most nodes are at the deepest level, so regenerating the shallow levels is cheap. It performs much worse than DFS when the tree is **narrow and deep**.

**Example.** States $s_0,s_1,\dots,s_n$ in a single chain: $s_i$ has exactly one successor $s_{i+1}$ ($b=1$); start $s_0$, only goal $s_n$.

- DFS: $s_0,s_1,\dots,s_n$: $n+1$ nodes, $O(n)$.

- IDS: limit 0: 1 node; limit 1: 2 nodes; ...; limit $n$: $n+1$ nodes. Total

$$\sum_{l=0}^{n}(l+1)=\frac{(n+1)(n+2)}{2}=O(n^2)$$

So IDS is about $n/2$ times slower. The same happens whenever DFS happens to find a deep goal on its first branch (e.g. goal at the end of the leftmost path of depth $d$ in a tree of branching $b$): DFS needs $d+1$ nodes, IDS needs $O(b^d)$.
