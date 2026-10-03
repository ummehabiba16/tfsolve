---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Alpha-beta is better in efficiency: it returns exactly the same minimax value and move but prunes branches that cannot affect the decision, needing O(b^{m/2}) nodes in the best case, so it searches about twice as deep. It is not always better: with the worst move ordering it prunes nothing and examines all O(b^m) nodes, the same as minimax (plus a little overhead); e.g. a MIN node whose children are examined in increasing order never triggers a cutoff."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning, move ordering)"]
---
**Yes, in efficiency (time and nodes examined), never in the result.**

- **Same answer:** alpha-beta always returns the **same minimax value and the same best move** as minimax. It only skips branches that provably cannot influence the decision, so the quality of play is identical.
- **Fewer nodes:** with good move ordering it examines only $O(b^{m/2})$ nodes instead of $O(b^m)$, an effective branching factor of $\sqrt b$. In the same time it can search about **twice as deep**, so a depth-limited player is much stronger. With random ordering it examines about $O(b^{3m/4})$ nodes.

**Is it guaranteed to always be better? No.** The pruning depends on move ordering. With the **worst ordering**, no cutoff ever happens. Alpha-beta then examines **every** node, exactly like minimax (with slight bookkeeping overhead), so it is no faster.

*Example:* MAX root with two MIN children. $m_1$ has leaves (3, 5) and $m_2$ has leaves (9, 6).

- Minimax: $m_1=3$, $m_2=6$, root $=6$. All 4 leaves are examined.
- Alpha-beta, this order: after $m_1=3$, $\alpha=3$. At $m_2$, leaf 9 gives $v=9>\alpha$, so no cutoff, and leaf 6 is examined too. **All 4 leaves are examined: no saving.**
- If $m_2$'s children were ordered (6, 9) and $m_1$'s values were higher, say (7, 8), so that $\alpha=7$: then after leaf 6 ($6\le\alpha$), leaf 9 is pruned.

So alpha-beta is **never worse** in its result and is usually far faster, but its speed-up is not guaranteed: it depends on examining good moves first.
