---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A game is a search problem with initial state S0, PLAYER(s), ACTIONS(s), RESULT(s,a), TERMINAL-TEST(s) and UTILITY(s,p) (zero-sum: payoffs sum to a constant). The game tree has the states as nodes and the moves as edges, alternating MAX and MIN levels, with utilities at the terminal leaves; it is searched by minimax."
sources: ["AIMA 3e sec. 5.1 (games as search problems)"]
---
**Formal definition of a game** (two players, MAX and MIN, who move in turn):

- $S_0$: the **initial state**, how the game is set up at the start.
- $\text{PLAYER}(s)$: which player has the move in state $s$.
- $\text{ACTIONS}(s)$: the set of legal moves in $s$.
- $\text{RESULT}(s,a)$: the **transition model**, the state that results from a move.
- $\text{TERMINAL-TEST}(s)$: true when the game is over (terminal states).
- $\text{UTILITY}(s,p)$: the **objective (payoff) function**, the final numeric value for player $p$ in terminal state $s$ (for chess: +1, 0 or $\frac12$). In a **zero-sum** game the players' payoffs always add up to the same constant.

Unlike ordinary search, the agent cannot pick a whole path: the opponent's moves are not under its control, so it needs a *strategy* (contingent plan) that specifies a move for every possible reply.

**Game tree.** The initial state, ACTIONS and RESULT define a tree. **Nodes** are game states, **edges** are moves, and levels alternate between MAX's and MIN's turns (plies). **Leaves** are terminal states, labeled with their utility for MAX.

*Example:* tic-tac-toe has fewer than $9!=362{,}880$ terminal nodes. Chess has about $10^{40}$ distinct positions, so its tree cannot be searched completely.

The minimax value of each node is backed up from the leaves (max at MAX nodes, min at MIN nodes). It gives the optimal move under the assumption that the opponent also plays optimally.
