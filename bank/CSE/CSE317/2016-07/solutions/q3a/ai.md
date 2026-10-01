---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Proof by induction on the tree: at MAX nodes MAX plays the minimax choice; at a MIN node a suboptimal MIN chooses some child whose value is at least the minimum, so the value obtained is >= the minimax value at every node. Yes: if MIN is suboptimal and predictable (e.g. always chooses the right child), MAX can do better by choosing a move that is bad against an optimal MIN (example tree with values 1,1 vs 0,10)."
sources: ["AIMA 3e sec. 5.2 and Exercise 5.7"]
---
**Assertion.** If MAX plays minimax decisions, the utility it obtains against a suboptimal MIN is never lower than against an optimal MIN.

**Proof (by induction on the height of the node).** Let $M(n)$ be the minimax value of node $n$ (value with both players optimal), and let $V(n)$ be the utility MAX actually obtains from $n$ when MAX plays minimax and MIN plays any (possibly suboptimal) strategy. Claim: $V(n)\ge M(n)$ for all $n$.

- *Terminal nodes*: $V(n)=M(n)=\text{UTILITY}(n)$.

- *MAX node*: MAX chooses the child $c^*$ with $M(c^*)=\max_c M(c)=M(n)$. By the induction hypothesis $V(c^*)\ge M(c^*)$, so $V(n)=V(c^*)\ge M(n)$.

- *MIN node*: MIN chooses some child $c'$ (not necessarily the minimising one). By induction $V(c')\ge M(c')$, and $M(c')\ge\min_c M(c)=M(n)$. Hence $V(n)\ge M(n)$.

At the root, $V(\text{root})\ge M(\text{root})$, the value obtained against an optimal MIN. $\blacksquare$

**Doing better with a suboptimal strategy against a suboptimal MIN.** Yes, if MAX knows how MIN deviates. Example:

```text
                 MAX
            a /       \ b
           MIN         MIN
          /   \       /   \
         1     1     0    10
```

Minimax: move $a$ has value 1, move $b$ value 0, so MAX plays $a$ and gets **1** against any MIN. Suppose MIN is suboptimal in a predictable way, e.g. it always picks the right-hand move. Then playing $b$ (suboptimal by minimax) gives MAX **10**, better than 1. But against an optimal MIN, $b$ gives 0 < 1, so the minimax move is the safe one; exploiting a weak opponent is risky if the model of the opponent is wrong.
