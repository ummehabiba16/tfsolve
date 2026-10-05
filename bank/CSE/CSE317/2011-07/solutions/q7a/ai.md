---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "States (X = agent, V = visited, . = unvisited): [. X .] (start), [X V .], [. V X], [V X .], [. X V], [V V X], [X V V], [V X V]: 8 valid states, the last three being goals. Transitions: Left/Right move one cell or bump (no change); e.g. [. X .] -L-> [X V .] -R-> [V X .] -R-> [V V X]."
sources: ["AIMA 3e sec. 3.2.1 (vacuum world state space, Fig. 3.3)"]
---
**State.** The agent's position plus which cells have been visited. Write X = agent's current cell (always visited), V = visited earlier, . = never visited. The agent starts in the middle: $[\,.\ X\ .\,]$. Cells left of a visited cell cannot be visited without passing through it, so only these **8 states** are reachable (valid):

| State | Meaning | Goal? |
|:-:|:--|:-:|
| S1 = [. X .] | start: in the middle, nothing else visited | no |
| S2 = [X V .] | in left, left and middle visited | no |
| S3 = [. V X] | in right, middle and right visited | no |
| S4 = [V X .] | back in middle, left visited | no |
| S5 = [. X V] | back in middle, right visited | no |
| S6 = [V V X] | in right, all visited | **yes** |
| S7 = [X V V] | in left, all visited | **yes** |
| S8 = [V X V] | in middle, all visited | **yes** |

(States such as $[X\ .\ V]$ are invalid: you cannot reach the right cell from the left without visiting the middle.)

**State transition diagram** (L = Left, R = Right; a move into the wall leaves the state unchanged):

```text
                    S1 [. X .]
                 L /          \ R
                  v            v
  (L: stay) S2 [X V .]      S3 [. V X] (R: stay)
             R |  ^            L |  ^
               v  | L            v  | R
            S4 [V X .]         S5 [. X V]
             R |                 L |
               v                   v
  (R: stay) S6 [V V X] <-R- S8 [V X V] -L-> S7 [X V V] (L: stay)
                       -L->            <-R-
```

Full transition table:

| From | Left | Right |
|:--|:--|:--|
| S1 [. X .] | S2 | S3 |
| S2 [X V .] | S2 | S4 |
| S3 [. V X] | S5 | S3 |
| S4 [V X .] | S2 | S6 |
| S5 [. X V] | S7 | S3 |
| S6 [V V X] | S8 | S6 |
| S7 [X V V] | S7 | S8 |
| S8 [V X V] | S7 | S6 |

Shortest solutions: L, R, R (S1, S2, S4, S6) or R, L, L (S1, S3, S5, S7).

*Note:* the figure for 7(a) is missing from the scan; the X/V/dot notation of 7(c) is assumed.
