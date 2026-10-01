---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Adversarial search is search in competitive multi-agent environments (games) where an opponent chooses some moves; unlike single-agent search the solution is a strategy (contingent on opponent replies), not a fixed path. Alpha-beta skips subtrees that cannot affect the minimax decision, so it returns the same value with less work."
sources: ["AIMA 3e sec. 5.1-5.3"]
---
**Adversarial search.** Search in a competitive multi-agent environment in which the agents' goals conflict, i.e. games. Two players, MAX and MIN, alternate moves; the game is defined by an initial state, PLAYER(s), ACTIONS(s), RESULT(s,a), TERMINAL-TEST(s) and UTILITY(s,p).

**Difference from single-agent search.**

| Single-agent search | Adversarial search |
|:--|:--|
| Agent controls every action | Opponent controls half the moves |
| Solution = sequence of actions (path) to a goal | Solution = strategy: a move for every possible opponent reply |
| Goal test, path cost | Terminal test, utility (win/lose/draw) |
| Uncertainty only from environment | Uncertainty from a rational opponent who tries to minimise our utility |
| Often can search to the goal | Game trees are huge (chess $\approx 35^{100}$), need cut-off and evaluation functions, time limits |

**Alpha-beta pruning.** Minimax explores the whole game tree. Alpha-beta computes the **same minimax value** but prunes branches that cannot influence the final decision. It keeps:

- $\alpha$ = best (highest) value found so far for MAX along the path,

- $\beta$ = best (lowest) value found so far for MIN along the path.

At a MIN node, if a child's value $v \le \alpha$, MAX above will never let play reach this node (it already has an alternative worth $\alpha$), so the remaining children are pruned. Symmetrically at a MAX node if $v \ge \beta$.

**Why the outcome is unchanged.** A pruned subtree can only make the value of its MIN parent smaller (or MAX parent larger), which can only make that branch *worse* for the player choosing above, who already has a better option. So the root's value and the chosen move are identical to minimax.

**Performance.** With perfect move ordering, alpha-beta examines $O(b^{m/2})$ nodes instead of $O(b^m)$: the effective branching factor drops to $\sqrt{b}$, so it can search about twice as deep in the same time. With random ordering, about $O(b^{3m/4})$.

Example: root MAX with two MIN children; the first MIN child has leaves 3, 12, 8 (value 3, so $\alpha=3$). The second MIN child's first leaf is 2: its value is at most 2 < 3, so its remaining leaves need not be examined.
