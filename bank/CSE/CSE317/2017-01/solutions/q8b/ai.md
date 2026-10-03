---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Minimax visits the whole game tree, O(b^m), infeasible for real games; alpha-beta pruning returns the same minimax decision but skips branches that cannot affect it (alpha = best value for MAX so far, beta = best for MIN), down to O(b^{m/2}) with good move ordering, so it searches about twice as deep. Greedy hill climbing gets stuck at local optima: simulated annealing sometimes accepts downhill moves with probability e^{Delta E / T}, T decreasing; a genetic algorithm keeps a population and uses crossover and mutation to jump across the space, so it can leave local optima."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning), sec. 4.1.2 (simulated annealing), sec. 4.1.4 (genetic algorithms)"]
---
**Necessity of alpha-beta pruning in adversarial search.** Minimax must examine every node of the game tree, $O(b^m)$. For chess ($b\approx35$, $m\approx100$) that is far beyond any computer, even with a depth limit. **Alpha-beta pruning** computes the **same minimax value and decision** while skipping subtrees that cannot influence it:

- $\alpha$ = the best value MAX can guarantee so far on the path; $\beta$ = the best value for MIN.
- At a MIN node, once its value is $\le\alpha$, MAX will never choose it, so its remaining children are pruned (symmetrically for MAX nodes with $\ge\beta$).
- With good move ordering, it examines only $O(b^{m/2})$ nodes, so the program can look about **twice as deep** in the same time, which gives much stronger play.

**How GA and simulated annealing escape the local optima of greedy search.** Hill climbing only moves uphill, so it stops at the first local maximum, ridge or plateau.

- **Simulated annealing:** pick a *random* neighbour. If it is better, move. If it is worse by $\Delta E<0$, still move with probability $e^{\Delta E/T}$. The "temperature" $T$ starts high (many downhill moves, exploration) and decreases slowly (fewer bad moves, exploitation). Occasional downhill moves let the search climb **out of local maxima**. If $T$ decreases slowly enough, it finds the global optimum with probability approaching 1.
- **Genetic algorithm:** keep a **population** of $k$ states instead of one. In each generation, select parents in proportion to fitness, apply **crossover** (combine parts of two parents) and **mutation** (random changes). Crossover can create offspring far from both parents, combining good "building blocks" from different regions. Mutation keeps diversity. The population explores many regions in parallel, so it is not trapped by one local optimum.
