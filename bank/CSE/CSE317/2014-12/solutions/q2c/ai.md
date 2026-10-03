---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "DFS problems: not complete (infinite paths, loops in tree search), not optimal (it returns the first, possibly deep, solution), time O(b^m) can be huge if m >> d. IDS runs depth-limited DFS with limits 0, 1, 2, ...: complete and optimal for unit costs, like BFS, while keeping DFS's O(bd) memory; re-expansion costs only a constant factor."
sources: ["AIMA 3e sec. 3.4.3-3.4.5"]
---
**Problems of depth-first search.**

1. **Not complete:** in infinite state spaces, or with loops (tree search), it can follow one infinitely deep path forever and never find a shallow goal.
2. **Not optimal:** it returns the first goal found along the leftmost deep branch, which may be much deeper and costlier than the best one.
3. **Time** $O(b^m)$, where $m$ (the maximum depth) can be much larger than the solution depth $d$, or infinite.

(Its advantage: memory is only $O(bm)$.)

**How iterative deepening search (IDS) fixes them.** IDS runs depth-limited DFS with limit $\ell=0,1,2,\dots$ until a goal is found.

- **Complete:** no path is followed below the current limit, so it cannot get lost in an infinite branch. The limit eventually reaches $d$.
- **Optimal** for equal step costs: the shallowest goal is found first, as in BFS.
- **Memory** stays $O(bd)$, as in DFS.
- **Time** $O(b^d)$: the repeated expansion of the upper levels is only a small constant-factor overhead (for $b=10$, about 11% more nodes than BFS).
