---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Alpha-beta prunes only if good moves are examined first: with perfect ordering it examines O(b^{m/2}) nodes (it can search twice as deep), with random ordering about O(b^{3m/4}), with the worst ordering O(b^m) (no pruning). A killer move is a move that caused a cutoff elsewhere at the same depth (often a strong threat); trying killer moves first is a dynamic move-ordering heuristic."
sources: ["AIMA 3e sec. 5.3.1 (move ordering)"]
---
**Why move ordering matters.** The effectiveness of alpha-beta pruning depends heavily on the order in which successors are examined. A cutoff happens only when a move is found that is already good enough to refute the opponent's line:

- **perfect ordering** (best moves first): only $O(b^{m/2})$ nodes are examined. The effective branching factor drops from $b$ to $\sqrt b$, so in the same time alpha-beta searches about **twice as deep** as minimax;
- **random ordering:** about $O(b^{3m/4})$ nodes for moderate $b$;
- **worst ordering** (worst moves first): no pruning at all, $O(b^m)$, the same as minimax.

*Example:* at a MIN node where MAX already has $\alpha=3$, if the first reply examined has value 2, the remaining replies are pruned immediately. If the value-2 reply is examined last, nothing is pruned.

Ordering heuristics include: captures first, then threats, forward moves, backward moves; the best moves from the previous iteration of iterative deepening; and transposition tables.

**Killer move.** A move that caused a cutoff (proved best) in a sibling position **at the same depth** of the tree. Such a move is often a strong threat that is good in many positions, for example a capture or a mating threat. The **killer-move heuristic** stores these moves and tries them first in other nodes at that depth. It is a cheap, dynamic way to approach perfect ordering and gets more cutoffs.
