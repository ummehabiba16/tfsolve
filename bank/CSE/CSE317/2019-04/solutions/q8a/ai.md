---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy search (hill climbing) gets stuck on local maxima, ridges, plateaux and shoulders (figure: state-space landscape). Combining it with SA: pick a random neighbour, accept improvements greedily and accept worse moves with probability e^(dE/T), T decreasing; this escapes local maxima early and behaves greedily later."
sources: ["AIMA 3e sec. 4.1.1 (Figure 4.1) and 4.1.2 (Figure 4.5)"]
---
**State-space landscape (objective value vs state).**

```text
objective
  ^                         global maximum
  |                              /\
  |        local maximum        /  \
  |            /\              /    \___ shoulder
  |           /  \    ____    /         \
  |          /    \__/    \__/           \
  |   ______/   "flat" local max           \
  |  /                                       \
  +------------------------------------------------> state space
            ^ current state
```

**Pitfalls of greedy search.** A greedy (hill-climbing) search moves to the best neighbouring state and stops when no neighbour is better.

1. **Local maxima**: a peak higher than its neighbours but lower than the global maximum; from the current state shown, greedy search climbs to the nearest local peak and stops.

2. **Ridges**: a sequence of local maxima not directly connected by available moves; each single move goes downhill, so the search zigzags slowly or stops.

3. **Plateaux**: flat regions, either a flat local maximum (no way up) or a **shoulder** (progress possible further on); the search has no gradient and wanders randomly or stops.

4. Consequences: incomplete, not optimal, highly dependent on the starting state (8-queens: steepest ascent succeeds in only 14% of random instances, getting stuck after about 4 steps).

**Main pitfall solved with simulated annealing.** Keep the greedy idea of improving moves, but allow occasional downhill moves controlled by a temperature $T$:

```text
function SIMULATED-ANNEALING(problem, schedule):
    current <- problem.INITIAL-STATE
    for t = 1, 2, ...:
        T <- schedule(t)                       // decreasing temperature
        if T = 0: return current
        next <- a randomly selected successor of current
        dE <- VALUE(next) - VALUE(current)
        if dE > 0: current <- next             // greedy: accept improvement
        else if RANDOM(0,1) < exp(dE / T):     // accept a worse move sometimes
            current <- next
```

**How it works.**

- A random successor is chosen (not the best), so the search is not deterministically pulled back to the same peak.

- Improving moves are always accepted (the greedy part).

- A worse move is accepted with probability $e^{\Delta E/T}$: high when $T$ is high and $|\Delta E|$ small. Early on the search can leave a local maximum and cross valleys, ridges and plateaux; as $T$ decreases (e.g. $T\leftarrow0.95T$), worse moves are rarely accepted and the search behaves like hill climbing on the best region.

- If $T$ decreases slowly enough, SA finds a global optimum with probability approaching 1.
