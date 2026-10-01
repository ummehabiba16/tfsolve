---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "P: win (or draw), material and positional advantage, within time; E: chessboard, pieces, opponent, clock; A: move display/robotic arm, press clock; S: board-state input or camera, opponent's moves, clock. Environment: fully observable, multi-agent competitive, deterministic (strategic), sequential, semi-dynamic with a clock (static without), discrete, known."
sources: ["AIMA 3e sec. 2.3 (Figure 2.6)"]
---
**PEAS for a chess-playing agent.**

| | |
|:--|:--|
| **Performance measure** | Win the game (win > draw > loss), e.g. +1/0/-1; possibly rating points; win within the time control; capture material, good position |
| **Environment** | Chessboard and pieces, the opponent (human or program), the chess clock, rules of chess |
| **Actuators** | Output of moves on a screen/network (or a robotic arm that moves pieces), pressing the clock, offering/accepting draws, resigning |
| **Sensors** | Input of the board state / opponent's moves (keyboard, network, or camera for a physical board), clock reading |

**Environment of the chess agent.**

- **Fully observable**: the whole board position is visible.

- **Multi-agent, competitive**: the opponent tries to minimise our performance.

- **Deterministic** (no chance; "strategic": deterministic except for the opponent's actions).

- **Sequential**: each move affects all future positions.

- **Semi-dynamic** when played with a clock (the board does not change while deliberating, but the score does as time runs out); **static** without a clock.

- **Discrete**: finite number of states (positions) and actions (moves).

- **Known**: the rules are fully known.

So chess is a deterministic, fully observable, two-player zero-sum game, solved in practice with adversarial search (minimax with alpha-beta and an evaluation function).
