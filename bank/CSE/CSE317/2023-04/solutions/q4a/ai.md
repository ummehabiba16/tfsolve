---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Use utility vectors (uA, uB) and let each player pick the child maximising its own component; with unconstrained utilities nothing can be pruned; with |uA - uB| <= k the game is almost cooperative, both players nearly maximise the same function, and alpha-beta still cannot prune (only bound-based pruning with a known maximum utility)."
sources: ["AIMA 3e sec. 5.2.2 (Multiplayer games) and its exercise on non-zero-sum games"]
---
**Minimax for two-player non-zero-sum games.** Each terminal state has a utility **vector** $(u_A,u_B)$, both known to both players. At a node where player $p$ moves, the backed-up value is the vector of the child with the largest $p$-component:

```text
function VALUE(s):
    if TERMINAL-TEST(s): return (UA(s), UB(s))
    p <- PLAYER(s)
    best <- none
    for each child c of s:
        v <- VALUE(c)
        if best = none or v[p] > best[p]: best <- v
    return best
```

So A maximises $u_A$ and B maximises $u_B$ (instead of minimising $u_A$). In the zero-sum case $u_B=-u_A$ and this reduces to ordinary minimax.

**Alpha-beta with no constraints on the two terminal utilities.** No node can be pruned. Alpha-beta prunes a MIN node when its value is already $\le\alpha$, because MIN's gain is MAX's loss. Here, an unexplored leaf below a B node could have a very high $u_B$ (so B would choose it) together with any $u_A$ (very good or very bad for A). Its value can therefore always change the decision at some ancestor, so every leaf must be examined.

**If the utilities differ by at most $k$** ($|u_A(s)-u_B(s)|\le k$, almost cooperative). Both players are now maximising nearly the same quantity, so B is not an adversary of A. Alpha-beta pruning depends on the players having opposite interests, so it still cannot prune: the tree behaves like a single-agent maximisation, where any unexplored leaf might be better for both players. Pruning is possible only with additional bounds: if the maximum possible utility $U$ is known, a player who has found a move with its own utility $U$ need not examine its other moves, and the other player's utility of that outcome is known to within $k$. With $k=0$ the game is fully cooperative and both players simply search for the leaf with the highest common utility.

(By contrast, if $|u_A+u_B|\le k$ the game is almost zero-sum and alpha-beta pruning works with a margin of $k$.)
