---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The cooling schedule specifies: initial temperature T0 (high enough that most moves are accepted), the temperature decrement rule (geometric T <- alpha T with alpha 0.8-0.99, linear, or logarithmic), the number of moves at each temperature (equilibrium / Markov chain length), and the final temperature or stopping criterion."
sources: ["AIMA 3e sec. 4.1.2", "Kirkpatrick, Gelatt and Vecchi (1983)"]
---
The **cooling schedule** decides how the temperature $T$ changes over time, and is the main factor in SA's performance. Its components:

1. **Initial temperature $T_0$.** Must be high enough that almost all moves, including bad ones, are accepted at the start (e.g. acceptance ratio about 80-90%), so the search can explore the whole space. A common method: sample random moves, compute the average deterioration $\overline{\Delta}$, and choose $T_0$ with $e^{-\overline{\Delta}/T_0}\approx0.8$. Too high wastes time; too low makes SA a greedy search.

2. **Temperature decrement function.**

- Geometric (most common): $T_{k+1}=\alpha T_k$ with $\alpha$ between 0.8 and 0.99.

- Linear: $T_{k+1}=T_k-\delta$.

- Logarithmic: $T_k=c/\log(1+k)$, which guarantees convergence to the global optimum but is far too slow in practice.

- Slow cooling gives better solutions but takes longer.

3. **Number of iterations at each temperature** (length of the Markov chain). At each temperature enough moves are tried for the system to reach "thermal equilibrium", e.g. a fixed number proportional to the neighbourhood size, or until a given number of moves have been accepted. Alternatively one move per temperature with a very slow decrease.

4. **Final temperature / stopping criterion.** Stop when $T$ reaches a small $T_f$ (e.g. 0 or $10^{-3}$), when the acceptance ratio falls below a threshold, or when no improvement has occurred for several temperatures. At the end, often a greedy descent polishes the best solution found.

```text
T <- T0
while not STOP:                    // final temperature / no improvement
    repeat L times:                 // moves per temperature
        propose random neighbour; accept by exp(dE / T)
    T <- alpha * T                  // decrement rule
```
