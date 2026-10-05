---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Hill climbing gets stuck at local maxima (no better neighbour), on ridges (sequences of local maxima that greedy moves cannot follow) and on plateaux or shoulders (flat areas with no uphill direction); it is therefore incomplete. Remedies: sideways moves, random restarts, stochastic hill climbing, simulated annealing."
sources: ["AIMA 3e sec. 4.1.1"]
---
Hill climbing always moves to the best neighbouring state and stops when no neighbour is better. It has no memory and never goes downhill, so it often gets stuck:

1. **Local maxima:** a state better than all its neighbours but worse than the global maximum. The algorithm halts there.
2. **Ridges:** a sequence of local maxima. The ridge rises slowly, but every single available move from a point on it goes downhill, so the search cannot follow it.
3. **Plateaux:** flat areas where all neighbours have the same value. A *flat local maximum* has no exit; a *shoulder* has an uphill exit that the search may not find. It wanders randomly or stops.

As a result, hill climbing is **incomplete and not optimal**: in 8-queens it solves only 14% of random instances. Remedies include allowing a limited number of sideways moves, random-restart hill climbing, stochastic or first-choice hill climbing, and simulated annealing.
