---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Alpha-beta returns the same move as minimax but prunes branches that cannot affect the decision (alpha = best for MAX so far, beta = best for MIN so far), reducing O(b^m) to about O(b^(m/2)) with good ordering. Assumptions: two players, alternating moves, zero-sum (MIN minimises what MAX maximises), perfect information, deterministic, and an optimal (minimax-playing) opponent."
sources: ["AIMA 3e sec. 5.3"]
---
**Why alpha-beta is better.** Conventional minimax examines every node of the game tree up to the search depth, $O(b^m)$. Alpha-beta computes the **same minimax decision** but **prunes** subtrees that cannot influence it. It maintains along the current path:

- $\alpha$ = value of the best (highest) choice found so far for MAX;

- $\beta$ = value of the best (lowest) choice found so far for MIN.

At a MIN node, once its value drops to $\le\alpha$, MAX will never choose this node (MAX already has something at least as good), so its remaining children are pruned. At a MAX node, once its value is $\ge\beta$, MIN will avoid it, so its remaining children are pruned.

```text
function MAX-VALUE(s, alpha, beta):
    if CUTOFF(s): return EVAL(s)
    v <- -infinity
    for each a in ACTIONS(s):
        v <- MAX(v, MIN-VALUE(RESULT(s, a), alpha, beta))
        if v >= beta: return v            // beta cut-off
        alpha <- MAX(alpha, v)
    return v
(MIN-VALUE is symmetric: v <- MIN(...); if v <= alpha return v; beta <- MIN(beta, v))
```

**Gain.** With perfect move ordering alpha-beta examines $O(b^{m/2})$ nodes, i.e. effective branching factor $\sqrt b$ (about 6 instead of 35 in chess), so it can search **twice as deep** in the same time; with random ordering about $O(b^{3m/4})$. Since deeper search gives stronger play, alpha-beta is far better than plain minimax, and it is exact (no loss of quality).

**Assumptions about how the game is played.**

1. **Two players who alternate moves** (MAX, MIN).

2. **Zero-sum (strictly competitive)**: what is good for one is equally bad for the other; one value describes a position for both. This is what makes pruning valid.

3. **Both players play optimally** (MIN always chooses the minimum, MAX the maximum). Against a non-optimal opponent the minimax move is safe but not necessarily best.

4. **Deterministic** (no chance moves) and **perfect information** (fully observable).

5. The values (utilities/evaluation function) are correct, or at least consistently ordered; with a heuristic evaluation the result is only as good as EVAL. Its efficiency also assumes good move ordering.
