---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Differences: a game tree alternates MAX and MIN levels (an opponent chooses half the moves), leaves carry utilities (not a single goal), and the solution is a strategy (a move for every opponent reply), not a path; usually it can only be searched to a depth limit with an evaluation function. DFS is used because minimax must evaluate leaves and back values up, and DFS does this in O(bm) memory. Alpha-beta prunes subtrees: at a MIN node with value <= alpha (or a MAX node >= beta), the remaining children cannot affect the decision."
sources: ["AIMA 3e sec. 5.1-5.3"]
---
**Adversarial search tree versus single-agent search tree** (3).

- **Two players alternate:** levels alternate between MAX and MIN. MIN's choices are not controlled by the agent, so we cannot just pick a path.
- **Utilities at terminal states** (win, lose, draw, or a score) instead of a goal test and a path cost. The best move maximizes the worst-case outcome.
- **The solution is a strategy** (a contingent plan): a move for every possible opponent reply, not a single sequence of actions.
- The trees are huge, so search is usually cut off at a depth limit and positions are estimated with an evaluation function.

**Why depth-first search?** (3) The minimax value of a node depends on the values of **all** its children down to the leaves (or the cut-off). It is computed recursively: go down to a leaf, evaluate it, and **back up** max or min values. Depth-first traversal does exactly this, finishing one subtree before the next. It needs only $O(bm)$ memory (the current path), which matters for trees with billions of nodes. It also lets alpha-beta use the values found so far to prune the rest.

**Operation of alpha-beta pruning** (5). It carries two bounds down the depth-first search:

- $\alpha$ = the value of the best choice found so far for **MAX** along the path (a lower bound);
- $\beta$ = the value of the best choice so far for **MIN** (an upper bound).

At a MAX node, update $\alpha=\max(\alpha,v)$; if $v\ge\beta$, **prune** the remaining children (MIN will never allow this node). At a MIN node, update $\beta=\min(\beta,v)$; if $v\le\alpha$, prune (MAX will never choose this node).

```text
function MAX-VALUE(s, a, b):
    if TERMINAL(s): return UTILITY(s)
    v <- -infinity
    for each move: v <- max(v, MIN-VALUE(result, a, b))
                   if v >= b: return v          # beta cutoff
                   a <- max(a, v)
    return v
(MIN-VALUE is symmetric, with v <= a giving an alpha cutoff)
```

It gives the same decision as minimax. With good move ordering it examines $O(b^{m/2})$ nodes instead of $O(b^m)$.
