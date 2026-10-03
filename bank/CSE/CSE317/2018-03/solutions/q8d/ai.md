---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hill climbing is greedy (it never moves downhill and has no memory), so it gets stuck at local maxima (all neighbours worse), ridges (a sequence of local maxima that is hard to move along) and plateaux (flat local maxima or shoulders, with no uphill direction). A sideways move goes to a neighbour with equal value, to escape shoulders; their number is limited (e.g. 100) to avoid infinite loops on flat maxima."
sources: ["AIMA 3e sec. 4.1.1 (hill-climbing search)"]
---
**Why hill climbing gets stuck.** Hill climbing (greedy local search) moves from the current state to its best neighbour, and stops when no neighbour is better. It looks only one step ahead and keeps no search tree, so it can stop at a state that is not the global optimum:

1. **Local maxima:** a peak higher than all its neighbours but lower than the global maximum. Every move goes downhill, so the algorithm halts. Example: an 8-queens state where every single move increases the number of attacking pairs.
2. **Ridges:** a sequence of local maxima close together, not directly connected by the available moves. Each step may move off the ridge downhill, so the search is very slow or stuck.
3. **Plateaux:** flat areas where all neighbours have the same value. They are either *flat local maxima* (no uphill exit) or *shoulders* (an uphill exit exists further along). The search wanders randomly or stops.

For 8-queens, steepest-ascent hill climbing from a random state gets stuck 86% of the time; it solves only 14% of instances.

**Sideways move.** A move to a neighbour with the **same** value. Allowing sideways moves lets the search cross shoulders and plateaux, hoping to find an uphill exit. On a flat local maximum it would loop forever, so the number of consecutive sideways moves is **limited** (e.g. 100). With up to 100 sideways moves, the success rate for 8-queens rises from 14% to 94%, at the cost of more steps (21 per success). Other remedies: random-restart hill climbing, stochastic hill climbing, and simulated annealing.
