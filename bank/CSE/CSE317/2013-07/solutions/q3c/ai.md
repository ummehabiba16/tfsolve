---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Alpha-beta gives exactly the same minimax value and move but prunes subtrees that cannot affect the decision, so it examines far fewer nodes: O(b^(m/2)) with perfect ordering instead of O(b^m), letting it search about twice as deep in the same time."
sources: ["AIMA 3e sec. 5.3"]
---
1. **Same result**: alpha-beta returns exactly the minimax value and the same best move; pruning never changes the decision.

2. **Fewer nodes**: it skips branches that cannot influence the final decision (a MIN node whose value is already $\le\alpha$, a MAX node already $\ge\beta$). Minimax always examines $O(b^m)$ nodes.

3. **Deeper search**: with perfect move ordering alpha-beta examines only $O(b^{m/2})$ nodes (effective branching factor $\sqrt b$, about 6 instead of 35 in chess); with random ordering about $O(b^{3m/4})$. In the same time it can look about **twice as deep**, which gives much stronger play.

4. **Same memory**: still a depth-first search, $O(bm)$ space.

5. Works naturally with move ordering heuristics (killer moves, iterative deepening, transposition tables) to get close to the best case.
