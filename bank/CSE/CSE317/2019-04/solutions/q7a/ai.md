---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Minimax recursively backs up utilities: MAX nodes take the maximum of their children, MIN nodes the minimum, choosing the move with the best value against an optimal opponent (O(b^m) time). For realistic games: cut off the search at a depth limit, replace utilities by a heuristic evaluation function, use alpha-beta pruning, move ordering, iterative deepening, quiescence search, transposition tables and opening/endgame databases."
sources: ["AIMA 3e sec. 5.2, 5.3 and 5.4 (Imperfect real-time decisions)"]
---
**Minimax algorithm.** A two-player zero-sum game with players MAX and MIN is a search problem: initial state, PLAYER(s), ACTIONS(s), RESULT(s,a), TERMINAL-TEST(s), UTILITY(s). The minimax value of a node is the utility (for MAX) of being in that state, assuming both play optimally:

- if $s$ is terminal:

$$\text{MINIMAX}(s)=\text{UTILITY}(s)$$

- if MAX is to move:

$$\text{MINIMAX}(s)=\max_a \text{MINIMAX}(\text{RESULT}(s,a))$$

- if MIN is to move:

$$\text{MINIMAX}(s)=\min_a \text{MINIMAX}(\text{RESULT}(s,a))$$

```text
function MINIMAX-DECISION(state):
    return the action a in ACTIONS(state) maximising MIN-VALUE(RESULT(state, a))

function MAX-VALUE(state):
    if TERMINAL-TEST(state): return UTILITY(state)
    v <- -infinity
    for each a in ACTIONS(state): v <- MAX(v, MIN-VALUE(RESULT(state, a)))
    return v

function MIN-VALUE(state):
    if TERMINAL-TEST(state): return UTILITY(state)
    v <- +infinity
    for each a in ACTIONS(state): v <- MIN(v, MAX-VALUE(RESULT(state, a)))
    return v
```

It is a depth-first exploration of the full game tree: complete (finite tree), optimal against an optimal opponent, time $O(b^m)$, space $O(bm)$.

**Modifications for realistic games.** For chess, $b\approx35$, $m\approx100$: $35^{100}$ nodes is impossible, and moves must be made within a time limit.

1. **Cutoff test instead of terminal test**: stop at a depth limit (chosen by iterative deepening so a move is ready when time runs out).

2. **Heuristic evaluation function EVAL(s)** instead of UTILITY at the cutoff: estimates expected utility, typically a weighted linear sum of features, e.g. material $w_1f_1+\dots+w_nf_n$ (pawn 1, knight/bishop 3, rook 5, queen 9) plus positional features. It must order terminal states like the true utility and be fast.

3. **Alpha-beta pruning** to skip irrelevant branches (search about twice as deep), with good **move ordering** (killer moves, captures first, best moves from previous iteration).

4. **Quiescence search**: only apply EVAL to quiet positions; extend the search in positions with pending captures (avoids wild swings).

5. Handle the **horizon effect** (singular extensions).

6. **Forward pruning** (beam search, ProbCut) of moves that are probably bad.

7. **Transposition tables** to avoid re-searching positions reached by different move orders.

8. **Opening books and endgame tablebases**: table lookup instead of search.

9. For games of chance: **expectiminimax** with chance nodes; for imperfect information: reasoning over belief states / sampling.
