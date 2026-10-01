---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy (hill climbing): fast, simple, little memory, but stops at local optima, ridges and plateaux, incomplete and not optimal. SA: same cheap single-state search but accepts worse moves with probability e^(dE/T), so it escapes local optima and converges to a global optimum with a slow enough schedule; it is slower and needs parameter tuning."
sources: ["AIMA 3e sec. 4.1.1-4.1.2"]
---
| | Greedy search (hill climbing) | Simulated annealing |
|:--|:--|:--|
| Move rule | always the best (or first better) neighbour | random neighbour; better: accept; worse: accept with probability $e^{\Delta E/T}$ |
| Memory | one state: $O(1)$ | one state: $O(1)$ |
| Speed | very fast, few iterations | slower: many iterations, cooling schedule |
| Local optima | gets stuck at local maxima, ridges, plateaux | can escape by downhill moves at high $T$ |
| Completeness/optimality | neither; result depends on start | probabilistically complete; finds the global optimum with probability $\to1$ if $T$ decreases slowly enough |
| Determinism | deterministic (steepest ascent) | stochastic: different runs give different results |
| Parameters | none | initial $T$, cooling rate, moves per $T$, stopping rule: need tuning |

**Advantages of greedy search:** simple to implement, fast convergence, good when the landscape is smooth or has a single peak (convex), useful to polish a solution.

**Pitfalls of greedy search:** stops at the first local optimum; on 8-queens steepest-ascent hill climbing solves only about 14% of random instances; plateaux cause aimless wandering; it cannot recover from a bad early choice.

**Advantages of SA:** escapes local optima; theoretical convergence guarantee; works well on very rugged landscapes (TSP, VLSI layout, scheduling); still memory-light.

**Pitfalls of SA:** slow (the theoretical schedule is impractically slow); quality depends heavily on the cooling schedule; no guarantee in finite time; a too-fast cooling makes it behave like greedy search, a too-slow one wastes time.

In practice SA is often combined with greedy steps (e.g. greedy local improvement at the end) to get the speed of greedy search and the robustness of annealing.
