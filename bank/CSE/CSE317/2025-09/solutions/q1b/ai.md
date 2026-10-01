---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "SA picks a random successor and always accepts improvements but accepts a worse move with probability e^(dE/T); T decreases slowly, so early on it can jump out of local maxima and at the end it behaves like hill climbing."
sources: ["AIMA 3e sec. 4.1.1-4.1.2 (Hill climbing, Simulated annealing)"]
---
**Why hill climbing gets stuck.** Hill climbing always moves to the best neighbour and stops when no neighbour is better. At a local maximum every neighbour is worse, so it stops there even though a higher (global) peak exists elsewhere. It never makes a downhill move.

**Simulated annealing (SA).** SA, inspired by annealing of metals, allows *some* downhill moves:

1. Pick a **random** successor `next` of `current`; let $\Delta E = \text{Value(next)} - \text{Value(current)}$.

2. If $\Delta E > 0$ (better), move to it.

3. Otherwise move to it only with probability $e^{\Delta E/T}$, where $T$ is the "temperature".

4. Lower $T$ according to a schedule (e.g. $T \leftarrow \alpha T$, $\alpha=0.95$).

```text
function SIMULATED-ANNEALING(problem, schedule):
    current <- initial state
    for t = 1, 2, 3, ...:
        T <- schedule(t)
        if T = 0: return current
        next <- a random successor of current
        dE <- VALUE(next) - VALUE(current)
        if dE > 0: current <- next
        else: current <- next with probability exp(dE / T)
```

**How it overcomes local maxima.** When $T$ is high, $e^{\Delta E/T}$ is close to 1, so the search can walk *down* out of a local maximum and cross valleys to other hills. Bad moves with a large $|\Delta E|$ are accepted less often than slightly bad ones. As $T$ falls, downhill moves become rare and SA behaves like hill climbing, settling on a high peak. If $T$ is lowered slowly enough, SA finds the global optimum with probability approaching 1.

**Example where SA beats hill climbing.** Consider a 1-D objective with a small peak at $x=2$ (value 5) and a higher peak at $x=8$ (value 10), separated by a valley of value 2 at $x=5$. Started at $x=1$, hill climbing climbs to $x=2$ and stops at value 5. SA at high temperature (say $T=5$) accepts a move from value 5 down to 4 with probability $e^{-1/5}\approx0.82$, so it can drift across the valley, reach the slope of the second hill and, as $T$ cools, finish at $x=8$ with value 10.

A practical scenario: TSP or VLSI layout, which have huge numbers of local optima; SA routinely produces much shorter tours / better layouts than plain hill climbing (2-opt), which stops at the first 2-opt local optimum.
