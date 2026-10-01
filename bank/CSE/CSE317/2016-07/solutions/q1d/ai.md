---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Stochastic: taxi driving, dice games; strategic: chess, auction bidding; discrete: chess, crossword; semi-dynamic: chess with a clock; partially observable: poker, taxi driving; sequential: chess, taxi driving."
sources: ["AIMA 3e sec. 2.3.2 (Figure 2.6)"]
---
| Environment type | Meaning | Examples |
|:--|:--|:--|
| (i) Stochastic | Next state not completely determined by current state and action | Taxi driving, backgammon (dice), medical diagnosis |
| (ii) Strategic | Deterministic except for the actions of other agents | Chess, tic-tac-toe, auction bidding |
| (iii) Discrete | Finite number of distinct states, percepts and actions | Chess, crossword puzzle, 8-puzzle |
| (iv) Semi-dynamic | Environment does not change with time, but the performance score does | Chess with a clock |
| (v) Partially observable | Sensors do not give the complete state | Poker, taxi driving, vacuum cleaner with only a local dirt sensor |
| (vi) Sequential | Current decision affects all future decisions | Chess, taxi driving, medical diagnosis (vs episodic: image classification, part-picking robot) |
