---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "SA picks a random neighbour, always accepts improvements and accepts a worse move with probability e^(dE/T), lowering T by a schedule; at high T it can climb down out of local optima, at low T it behaves greedily."
sources: ["AIMA 3e sec. 4.1.2 (Figure 4.5)"]
---
**Simulated annealing.** Analogy with annealing in metallurgy: heat a metal and cool it slowly so its atoms settle into a low-energy crystalline state. In search, "temperature" $T$ controls how often worse moves are accepted.

```text
function SIMULATED-ANNEALING(problem, schedule) returns a solution state
    current <- MAKE-NODE(problem.INITIAL-STATE)
    for t = 1 to infinity:
        T <- schedule(t)
        if T = 0: return current
        next <- a randomly selected successor of current
        dE   <- VALUE(next) - VALUE(current)
        if dE > 0: current <- next
        else: current <- next only with probability exp(dE / T)
```

Typical schedule: $T_0$ large, $T_{k+1}=\alpha T_k$ with $\alpha\in[0.8,0.99]$, several moves per temperature, stop when $T$ is small or no moves are accepted.

**Avoiding the local optima problem of greedy search.** Greedy search (hill climbing) only ever moves to a better neighbour, so at a local optimum it stops. SA differs in two ways:

1. It chooses a **random** successor rather than the best one, so it does not deterministically return to the same peak.

2. It accepts a **worse** move with probability $P=e^{\Delta E/T}$ ($\Delta E<0$). This probability is high when $T$ is high and when the move is only slightly worse; it decreases exponentially with the badness $|\Delta E|$ and as $T$ decreases.

So early in the search it can go downhill, leave a local optimum and cross "valleys" to other regions. Later, at low temperature, it accepts almost only improving moves and converges like hill climbing on the best region found. If the schedule lowers $T$ slowly enough, SA converges to a global optimum with probability approaching 1.

Example: maximising a function with a local peak 5 and a global peak 10 separated by a valley of height 2: at $T=5$ a downhill step of $-1$ is accepted with probability $e^{-0.2}\approx0.82$; at $T=0.2$ with probability $e^{-5}\approx0.007$. Thus SA wanders between peaks early and stays on the high one late.
