---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Adversarial search faces an opponent whose moves are unpredictable and hostile, huge game trees, time limits and the need for strategies, evaluation functions and pruning. In CSPs MRV ('fail-first') prunes the tree early by picking the variable most likely to fail, while LCV ('fail-last') keeps options open because only one solution is needed."
sources: ["AIMA 3e sec. 5.1-5.4 and 6.3.1"]
---
**Main challenges of adversarial search (vs single-agent search).**

1. **An opponent controls some moves.** The result of our action depends on the opponent's reply, which we cannot control or predict exactly, and which is chosen to hurt us. The solution is therefore a *strategy* (a move for every possible opponent reply), not a fixed path.

2. **Assumption about the opponent.** We must model it, usually as optimal (minimax); against a suboptimal or deceptive opponent this may not be best.

3. **Huge search spaces.** Chess has $b\approx35$ and games of about 80 plies: $35^{80}\approx10^{123}$ nodes; we cannot search to terminal states.

4. **Real-time decisions.** Moves must be made within a time limit, so search is cut off and non-terminal positions are scored with a heuristic **evaluation function**, which introduces errors (horizon effect, quiescence).

5. **Efficiency techniques** are needed: alpha-beta pruning, move ordering, transposition tables, iterative deepening, opening books, endgame tables.

6. **Uncertainty** in some games: chance (dice: expectiminimax) and partial observability (card games).

**Most constrained variable / least constraining value.**

- **Most constrained variable (MRV, fail-first)**: choose the variable with the fewest remaining legal values. Every variable must eventually be assigned, so choosing the one most likely to fail first detects dead ends at shallow depth and prunes large parts of the search tree. If some variable has no legal values left, MRV picks it at once and backtracks immediately.

- **Least constraining value (LCV, fail-last)**: for that variable, try first the value that rules out the fewest choices for the neighbouring variables. Since only one solution is needed, we want the value most likely to lead to a solution, keeping maximum flexibility for later variables.

Example (Australia map colouring): after WA = red, NT = green, MRV picks SA (only blue left) rather than V (three colours). For Q, LCV prefers red (leaves SA blue) over blue (leaves SA no value).
