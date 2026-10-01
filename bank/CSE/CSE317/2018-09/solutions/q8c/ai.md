---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Hill climbing only moves uphill, so it stops at local maxima, ridges and plateaux. Random-restart hill climbing repeats hill climbing from random initial states and keeps the best result (complete with probability approaching 1). For TSP: construct an initial tour greedily (nearest neighbour or cheapest insertion), then improve it with local moves (2-opt / 3-opt swaps) until no move shortens the tour."
sources: ["AIMA 3e sec. 4.1.1", "Johnson and McGeoch, 'The TSP: a case study in local optimization'"]
---
**Why hill climbing often fails to find the global optimum.** Hill climbing always moves to the best neighbouring state and stops when no neighbour is better. It therefore gets stuck at:

- **local maxima**: peaks higher than every neighbour but lower than the global maximum;

- **ridges**: sequences of local maxima where every available single move goes downhill;

- **plateaux and shoulders**: flat regions where no move improves, so the search wanders or stops.

It never goes downhill and never backtracks, so it is incomplete and the result depends on the starting state (8-queens: steepest ascent solves only 14% of instances).

**Random-restart hill climbing.** "If at first you don't succeed, try, try again": run hill climbing repeatedly from **randomly generated initial states** and keep the best result. If each run succeeds with probability $p$, the expected number of restarts is $1/p$ (8-queens: $p\approx0.14$, so about 7 runs). It is complete with probability approaching 1, because eventually a start state in the basin of the global optimum is generated.

**Hill climbing for TSP.**

*Construction heuristics* build a tour from scratch, adding one city at a time greedily:

- **Nearest neighbour**: start at a city, repeatedly go to the nearest unvisited city, then return.

- **Cheapest (or nearest/farthest) insertion**: start with a small sub-tour, repeatedly insert the city whose insertion increases the tour length least.

This gives a complete tour quickly (typically 15-25% above optimal).

*Improvement heuristics* then perform hill climbing on complete tours:

- State: a complete tour; neighbours: tours obtained by a local change.

- **2-opt**: remove two edges $(a,b)$ and $(c,d)$ and reconnect as $(a,c)$ and $(b,d)$ (reversing the segment between). Accept the change if the tour gets shorter: $d(a,c)+d(b,d)<d(a,b)+d(c,d)$.

- **3-opt / Or-opt**: remove three edges, or move a segment of 1-3 cities elsewhere.

- Repeat until no move improves (a 2-opt local optimum, typically about 5% above optimal).

Combined: construction gives a good starting tour, improvement climbs to a local optimum; random restarts (or perturbations) and taking the best tour reduce the risk of a poor local optimum.
