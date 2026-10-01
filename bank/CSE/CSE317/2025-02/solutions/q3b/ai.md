---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy (hill-climbing) search is fast, simple, needs little memory and gives good solutions quickly, but it gets stuck in local optima, ridges and plateaux and is incomplete/non-optimal. Simulated annealing keeps the greedy moves but accepts worse moves with probability e^(dE/T) and a decreasing temperature, escaping local optima."
sources: ["AIMA 3e sec. 4.1.1-4.1.2", "AIMA 3e sec. 3.5.1"]
---
**Greedy algorithm (greedy local search / hill climbing).** At each step it takes the locally best choice (the best neighbour, or the node that looks closest to the goal) and never reconsiders.

**Facilities (advantages).**

- Very simple and fast: each step only evaluates the current neighbours.

- Very little memory: only the current state ($O(1)$ or $O(b)$).

- Works on huge or continuous state spaces where systematic search is impossible, and quickly gives a reasonably good solution; it can be stopped at any time (anytime behaviour).

**Pitfalls.**

- **Local maxima/minima**: a peak higher than its neighbours but lower than the global peak; the algorithm stops there.

- **Ridges**: a sequence of local maxima that is hard to follow with the available moves.

- **Plateaux / shoulders**: flat regions with no uphill direction; the search wanders or stops.

- Not complete and not optimal; the result depends strongly on the start state (8-queens: steepest-ascent hill climbing solves only 14% of instances).

**Algorithm that keeps the facilities but avoids the optimality problem: simulated annealing (SA).** SA is still a one-state local search (cheap, little memory), but instead of always taking the best move it picks a random neighbour and:

- accepts it if it is better;

- if it is worse by $\Delta E<0$, accepts it with probability $e^{\Delta E/T}$.

The temperature $T$ starts high (many downhill moves accepted, so the search can leave local optima) and decreases slowly (eventually only uphill moves, like greedy search).

```text
function SIMULATED-ANNEALING(problem, T0, alpha, Tmin):
    current <- problem.INITIAL-STATE ;  best <- current
    T <- T0
    while T > Tmin:
        repeat L times:                           // moves per temperature
            next <- RANDOM-NEIGHBOUR(current)
            dE   <- VALUE(next) - VALUE(current)
            if dE > 0 or RANDOM(0,1) < exp(dE / T):
                current <- next
                if VALUE(current) > VALUE(best): best <- current
        T <- alpha * T                            // e.g. alpha = 0.95
    return best
```

**How it works.** At high $T$ the search behaves almost like a random walk and explores the space; as $T$ falls it concentrates on the best regions and finally becomes greedy. If $T$ decreases slowly enough, SA finds a global optimum with probability approaching 1. Thus it uses the greedy step (cheap local improvement) but avoids being trapped in local optima. (Random-restart hill climbing and genetic algorithms are alternative answers.)
