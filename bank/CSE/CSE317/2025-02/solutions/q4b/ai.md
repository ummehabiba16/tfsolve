---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Values become utility vectors (u1, u2); at each node the player to move picks the child maximising its own component (minimax generalised). With no constraint on the two utilities no node can be pruned. If utilities differ by at most k the game is nearly cooperative: each player is almost maximising the same function, so alpha-beta-style pruning still does not apply; only bound-based pruning (known maximum utility) is possible."
sources: ["AIMA 3e sec. 5.2.2 (Optimal decisions in multiplayer games) and its exercise on non-zero-sum games", "AIMA 4e sec. 5.2"]
---
**Changes to minimax.** In a non-zero-sum game a single number no longer suffices: each terminal state has a **vector** of utilities $(u_A, u_B)$. The backed-up value of a node is the vector of the child chosen by the player to move, and that player chooses the child that **maximises its own component**:

```text
function VALUE(s):
    if TERMINAL(s): return (UA(s), UB(s))
    p <- PLAYER(s)
    return the VALUE(child) with the largest component p over all children of s
```

This is the multiplayer generalisation of minimax (MAX maximises $u_A$, the other player maximises $u_B$ instead of minimising $u_A$). Ties may need a rule (e.g. break in favour of / against the other player).

**Alpha-beta with no constraints on the two utilities.** No pruning is possible. Alpha-beta prunes a branch because the opponent's gain is our loss: once MIN can force a value below $\alpha$, MAX will avoid that node. Here the two utilities are independent: an unexplored leaf could have any $u_B$ value, which could make the other player choose it, and any $u_A$ value, which could make that choice the best for player A. So every leaf may change the decision and the full tree must be searched.

**Utilities differing by at most $k$ ($|u_A-u_B|\le k$, almost cooperative).** Now both players are trying to maximise almost the same function. The player B at a node is effectively also a maximiser of $u_A$ (up to $k$). Alpha-beta pruning relies on the players having *opposite* interests, so it still gives **no pruning**: the tree behaves like a single-agent maximisation tree, where in general every leaf must be examined because any unseen leaf could be better for both.

What *is* possible is bound-based pruning: if the utilities are known to be bounded above by $U$, a player who has found a move with its own utility equal to $U$ can stop examining its other moves, and since $|u_A-u_B|\le k$ the other player's utility for that move is known within $k$. With $k=0$ the game is fully cooperative: both just look for the leaf of maximum common utility.

(Contrast: if instead $|u_A+u_B|\le k$, the game is *almost zero-sum* and alpha-beta pruning is possible with a margin of $k$: prune when the bounds differ by more than $k$.)
