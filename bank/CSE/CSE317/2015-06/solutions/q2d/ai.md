---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Fill the 12-gallon jug: (12, 0, 0); pour 12 into 8: (4, 8, 0); pour 12 into 3: (1, 8, 3). The 12-gallon jug now holds 1 gallon: 3 actions (shortest, found by BFS)."
sources: ["AIMA 3e sec. 3.4.1 (breadth-first search)"]
---
Using the formulation of 2(c), with states $(a,b,c)$ for the 12-, 8- and 3-gallon jugs:

| Step | Action | State |
|:-:|:--|:-:|
| 0 | start | (0, 0, 0) |
| 1 | $Fill(12)$ | (12, 0, 0) |
| 2 | $Pour(12\to8)$: 8 gallons fit | (4, 8, 0) |
| 3 | $Pour(12\to3)$: 3 gallons fit | **(1, 8, 3)** |

After step 3, the 12-gallon jug holds exactly **1 gallon**, so the goal is reached.

This is a shortest solution (3 actions): a breadth-first search over the state space finds no solution with fewer steps. No 1- or 2-step sequence can leave a jug with 1 gallon, because from the empty state the reachable amounts after two steps are 12, 8, 3, 4, 9 and 5 (and combinations).
