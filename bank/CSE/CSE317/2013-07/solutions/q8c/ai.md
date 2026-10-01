---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Treat chess as adversarial search: minimax with alpha-beta to a depth limit (iterative deepening) and a heuristic evaluation function (material, mobility, king safety, pawn structure, centre control); strategies: move ordering and killer moves, transposition tables, quiescence search and singular extensions, forward/null-move pruning, opening books and endgame tablebases, and learning the evaluation (e.g. self-play reinforcement learning with MCTS and a neural network, as in AlphaZero)."
sources: ["AIMA 3e sec. 5.1-5.5 and 5.7 (State-of-the-art game programs)"]
---
**Approach: adversarial search with a heuristic evaluation function.** Chess is a deterministic, fully observable, two-player zero-sum game, so the agent can choose moves by **minimax search** over the game tree. The full tree ($b\approx35$, $\approx10^{40}$ positions) cannot be searched, so:

1. **Depth-limited search with a cutoff test**: search to a fixed depth, using **iterative deepening** so that a move is always ready when the clock runs out.

2. **Evaluation function** EVAL(s) at the cutoff: a weighted linear function of features,

$$EVAL(s)=w_1f_1(s)+\dots+w_nf_n(s)$$

e.g. material (pawn 1, knight 3, bishop 3, rook 5, queen 9), mobility, king safety, pawn structure (doubled/isolated/passed pawns), control of the centre, piece development.

3. **Alpha-beta pruning** to search about twice as deep as minimax.

**Different strategies one can exploit within this approach.**

- **Move ordering**: try captures, killer moves, and the best move from the previous iteration first (history heuristic), so alpha-beta prunes close to the best case $O(b^{m/2})$.

- **Transposition tables**: cache values of positions reached by different move orders.

- **Quiescence search**: extend the search at the cutoff in non-quiet positions (pending captures, checks) to avoid misleading evaluations.

- **Singular extensions** against the horizon effect: search one move deeper when one move is clearly better.

- **Forward pruning**: beam search, null-move pruning, ProbCut, late-move reductions, to ignore probably bad moves.

- **Opening book**: table lookup of well-known openings instead of search.

- **Endgame tablebases**: precomputed perfect play (retrograde analysis) for positions with few pieces.

- **Time management**: allocate more time to critical positions.

- **Learning**: tune the evaluation weights from games (e.g. by regression or temporal-difference learning); or, as in AlphaZero, replace the hand-crafted evaluation by a deep neural network trained by **self-play reinforcement learning** and replace alpha-beta by **Monte Carlo tree search** guided by that network.

- **Opponent modelling**: exploit known weaknesses of the opponent (risky, as in minimax vs suboptimal MIN).

Deep Blue (1997) used parallel alpha-beta search of 30-40 billion positions per move with a 8000-feature evaluation, opening book and endgame tables; modern programs (Stockfish, AlphaZero) reach far above human level using the strategies above.
