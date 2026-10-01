---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy search (best-first on h, or hill climbing) commits to locally best choices: it is not optimal (ignores path cost), not complete (can loop or follow dead ends, as tree search in infinite spaces), gets stuck in local optima, ridges and plateaux, and its quality depends heavily on the heuristic and starting point; worst-case time and space O(b^m)."
sources: ["AIMA 3e sec. 3.5.1 and 4.1.1"]
---
**Greedy best-first search** expands the node that appears closest to the goal, $f(n)=h(n)$. **Greedy local search** (hill climbing) moves to the best neighbour. Their problems:

1. **Not optimal.** It ignores the cost already spent ($g$). Example (Romania, Arad to Bucharest): greedy follows Arad-Sibiu-Fagaras-Bucharest (450 km) because Fagaras is closest to Bucharest by straight line, missing the optimal route via Rimnicu Vilcea and Pitesti (418 km).

2. **Not complete (tree search).** It can be misled into dead ends or infinite loops. Example: from Iasi to Fagaras, the heuristic prefers Neamt, a dead end; going back to Iasi it is again led to Neamt: Iasi, Neamt, Iasi, Neamt, ... forever. (The graph-search version is complete in finite spaces.)

3. **Local optima, ridges, plateaux** (greedy local search): it stops at the first local maximum, cannot follow ridges and wanders on plateaux; it never reconsiders a decision (no backtracking).

4. **Dependence on the heuristic and start state**: with a poor heuristic it can be very inefficient; worst-case time and space are $O(b^m)$ ($m$ = maximum depth).

5. **Short-sighted**: a choice that looks best now can force expensive moves later (e.g. nearest-neighbour TSP leaves long edges for the end).

Remedies: A* (adds $g$), random restarts, simulated annealing, beam search, genetic algorithms.
