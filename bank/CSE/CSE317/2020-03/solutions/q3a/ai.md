---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "DFS: may follow an infinite or very deep path (incomplete, not optimal), returns the first (possibly deep) solution. DLS fixes infinite paths with a limit l but is incomplete if l < d and non-optimal if l > d. IDS runs DLS with l = 0,1,2,... so it is complete and optimal (unit costs) with O(bd) memory and O(b^d) time."
sources: ["AIMA 3e sec. 3.4.3-3.4.5"]
---
**Bottlenecks of depth-first search.**

- **Not complete** in infinite state spaces or with loops (tree search): it can follow an infinite path and never return.

- **Not optimal**: returns the first goal found, which may be deep and expensive even if a shallow goal exists in another branch.

- Time $O(b^m)$, where $m$ (max depth) may be much larger than $d$, or infinite.

- (Its advantage: memory only $O(bm)$.)

**Bottlenecks of depth-limited search (DLS).** DLS is DFS with a depth limit $l$ (nodes at depth $l$ have no successors), which removes infinite paths. But:

- if $l<d$ (goal deeper than the limit), it is **incomplete**;

- if $l>d$, it is **not optimal** (may return a deep solution);

- we rarely know $d$ in advance to choose a good $l$.

**Iterative deepening search (IDS).** Run DLS with $l=0,1,2,\dots$ until a goal is found.

```text
function ITERATIVE-DEEPENING-SEARCH(problem):
    for depth = 0 to infinity:
        result <- DEPTH-LIMITED-SEARCH(problem, depth)
        if result != cutoff: return result
```

- It finds the shallowest goal (at limit $d$), so it is **complete** (finite $b$) and **optimal** for equal step costs, like BFS.

- It never goes deeper than the current limit, so no infinite paths, and memory is $O(bd)$, like DFS.

- Time: nodes at depth $k$ are generated $d-k+1$ times: $N=(d)b+(d-1)b^2+\dots+1\cdot b^d=O(b^d)$. For $b=10,d=5$: 123,450 vs 111,110 for BFS, only about 11% overhead.

**Example.** Binary tree with root A, children B, C; B's children D, E; C's children F (goal), G; and an infinite left branch below D. DFS goes A, B, D, ... down forever. DLS with $l=1$ visits A, B, C and fails (goal at depth 2). IDS: limit 0: A; limit 1: A, B, C; limit 2: A, B, D, E, C, F: goal found at the shallowest depth with only $O(bd)$ memory.
