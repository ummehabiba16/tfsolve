---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hill climbing stops at local maxima, gets stuck on ridges (sequences of local maxima) and wanders on plateaux or shoulders, because it only accepts improving moves. Simulated annealing picks a random neighbour and always accepts it if it is better, otherwise with probability e^{Delta E / T}; T is lowered slowly, so early on it escapes local maxima and later it settles; a slow enough schedule finds the global optimum with probability approaching 1."
sources: ["AIMA 3e sec. 4.1.1 (hill climbing), 4.1.2 (simulated annealing)"]
---
**Main problems of hill climbing** (it always moves to the best neighbour, and stops when none is better):

1. **Local maxima:** a peak higher than its neighbours but lower than the global maximum. The search halts there.
2. **Ridges:** a sequence of local maxima that is very hard to navigate with the available moves. Every single move from a point on the ridge goes downhill.
3. **Plateaux:** flat regions. A *flat local maximum* has no uphill exit; a *shoulder* has one but the search cannot find it, and it wanders or stops.

For 8-queens it gets stuck 86% of the time, because it never accepts a downhill move. It is incomplete.

**How simulated annealing solves them.** Pick a **random** successor $s'$ of the current state $s$, with $\Delta E=\text{Value}(s')-\text{Value}(s)$:

- if $\Delta E>0$ (better): always move to $s'$;
- otherwise move with probability $e^{\Delta E/T}$ (less than 1).

The **temperature** $T$ follows a schedule that decreases from high to low.

- At high $T$, bad moves are accepted often. The search can go **downhill**, escaping local maxima and crossing ridges and plateaux (exploration).
- As $T$ decreases, bad moves become rare, and the search settles into a good maximum (exploitation).
- Moves that are only slightly worse are accepted more often than very bad ones.

If $T$ decreases slowly enough, simulated annealing finds a **global optimum** with probability approaching 1.

```text
function SIMULATED-ANNEALING(problem, schedule)
    current <- problem.INITIAL-STATE
    for t = 1 to infinity:
        T <- schedule(t);  if T = 0 then return current
        next <- a randomly selected successor of current
        dE <- next.VALUE - current.VALUE
        if dE > 0 then current <- next
        else current <- next only with probability e^(dE/T)
```
