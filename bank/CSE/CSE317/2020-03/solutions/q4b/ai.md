---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Use utility vectors (uA, uB); at each node the player to move chooses the child maximising its own utility (generalised minimax). With no constraints on the two terminal utilities, alpha-beta cannot prune any node, because any unexplored leaf could change some player's choice."
sources: ["AIMA 3e sec. 5.2.2 (Optimal decisions in multiplayer games)"]
---
**Changing minimax.** In a two-player non-zero-sum game the two utilities are not opposites, so a node's value must be a **vector** $(u_A,u_B)$. Terminal states return their vector. At an internal node, the player to move picks the child whose vector has the **largest value of its own component**, and that vector is backed up:

```text
function VALUE(s):
    if TERMINAL-TEST(s): return (UA(s), UB(s))
    p <- PLAYER(s)
    return the VALUE(c), over children c of s, that maximises component p
```

Both players are maximisers (A of $u_A$, B of $u_B$). In the zero-sum special case $u_B=-u_A$, B maximising $u_B$ is the same as minimising $u_A$, which is ordinary minimax. Ties need a tie-breaking rule (e.g. B breaks ties in favour of or against A), which can change A's value.

**Changing alpha-beta / can anything be pruned?** Alpha-beta pruning works because one player's gain is the other's loss: at a MIN node with value already $\le\alpha$, MAX will never let play reach it. If there are **no constraints** relating $u_A$ and $u_B$, **no node can be pruned**:

- At a B node, B has so far found a child with $u_B=v$. An unexplored leaf could have $u_B>v$ (so B would switch to it) and an arbitrary $u_A$, very high or very low.

- Therefore that leaf could make this B node either better or worse for A than A's alternatives, so A's decision above can depend on it.

Since every unexplored leaf can affect the decision, the full tree must be searched; the algorithm is just the vector minimax above, with no $\alpha$/$\beta$ cut-offs.
