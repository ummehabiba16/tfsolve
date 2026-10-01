---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A game is a search problem with initial state, PLAYER, ACTIONS, RESULT, TERMINAL-TEST and UTILITY. For the 5-token game with MIN first: MIN can split 5 into 1+4 or 2+3. 1+4 leads to (1,1,3) then (1,1,1,2) where MAX cannot move: utility 0. 2+3 leads to (1,2,2) where MIN cannot move: utility 1. Root value 0: with perfect play MIN wins by splitting into 4 and 1."
sources: ["AIMA 3e sec. 5.1-5.2 (Grundy's game is a standard textbook exercise)"]
---
**Game as a search problem.** A game is defined by:

- $S_0$: the **initial state** (initial position);

- PLAYER(s): which player moves in state $s$;

- ACTIONS(s): legal moves in $s$;

- RESULT(s, a): the **transition model**, state after a move;

- TERMINAL-TEST(s): true when the game is over (terminal states);

- UTILITY(s, p): the payoff for player $p$ at terminal state $s$ (e.g. 1, 0 / +1, -1, 0).

The initial state, ACTIONS and RESULT define the **game tree**; the search finds a strategy (a move for each opponent reply) rather than a path.

**The token game (Grundy's game) with 5 tokens, MIN first.** A state is the multiset of stack sizes plus whose turn it is. A move splits one stack into two non-empty, unequal stacks; stacks of size 1 or 2 cannot be split. Terminal: no stack can be split; the player to move loses, so utility 1 if MIN is to move (MAX wins), 0 if MAX is to move (MIN wins).

**Complete search tree with minimax values** (values in brackets):

```text
                    (5)  MIN to move           [0]
                  /                  \
        (4,1)  MAX [0]              (3,2)  MAX [1]
            |                           |
        (3,1,1)  MIN [0]            (2,2,1)  MIN, terminal [1]
            |                       (MIN cannot move: MAX wins)
        (2,1,1,1)  MAX, terminal [0]
        (MAX cannot move: MIN wins)
```

- From (5), MIN can split into 4+1 or 3+2 (5 = 2.5 + 2.5 is impossible).

- (4,1), MAX: 4 can only be split as 3+1 (2+2 is equal, illegal) $\to$ (3,1,1).

- (3,1,1), MIN: 3 can only be split as 2+1 $\to$ (2,1,1,1).

- (2,1,1,1), MAX to move: no stack can be split $\to$ MAX loses, utility 0.

- (3,2), MAX: split 3 into 2+1 $\to$ (2,2,1).

- (2,2,1), MIN to move: no legal move $\to$ MIN loses, utility 1.

**Minimax backing up.** (3,1,1): MIN node with one child of value 0 $\to$ 0. (4,1): MAX node with one child 0 $\to$ 0. (2,2,1) = 1, so (3,2) = 1. Root (MIN): $\min(0,1)=0$.

**Who wins?** The root value is 0, so with perfect play **MIN wins**. MIN's winning first move is to split the 5 tokens into **4 and 1**: after that every move is forced (MAX must make 3+1+1, MIN makes 2+1+1+1) and MAX is left without a move. If MIN instead split into 3 and 2, MAX would win by splitting the 3.
