---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Encode a tour as a permutation of cities; fitness = 1/tour length; tournament or rank selection; order crossover (OX/PMX) so children stay valid permutations; swap/inversion mutation; elitism."
sources: ["AIMA 3e sec. 4.1.4 (Genetic algorithms)", "AIMA 4e sec. 4.1.4"]
---
**Idea.** A genetic algorithm (GA) keeps a *population* of candidate tours and improves it over generations by selecting good tours, recombining them and making small random changes. It does not guarantee the optimum, but it finds near-optimal tours for large TSP instances where exact search is infeasible ($(n-1)!/2$ tours).

**1. Encoding (path representation).** A chromosome is a permutation of the $n$ cities, e.g. for cities A-H: `C A F B H D G E`, meaning the tour C$\to$A$\to$F$\to\dots\to$E$\to$C.

*Justification:* every permutation is a valid tour and every tour has a representation, so no repair or penalty is needed. A binary string encoding would produce many invalid offspring (repeated or missing cities).

**2. Fitness.** For tour $T$ with length $L(T)=\sum_i d(c_i,c_{i+1})+d(c_n,c_1)$, use $\text{fitness}(T)=1/L(T)$ (or $L_{\max}-L(T)$). Shorter tours get higher fitness.

**3. Selection.** Choose parents with probability increasing with fitness:

- *Tournament selection* (pick $k$ random tours, keep the best) or *rank-based selection*. Justification: roulette-wheel selection on $1/L$ gives almost equal probabilities when tour lengths are close, and lets one very good tour take over too early; tournament/rank keeps a controllable selection pressure.

- *Elitism*: copy the best one or two tours unchanged to the next generation so the best solution is never lost.

**4. Crossover.** Ordinary one-point crossover breaks permutations (cities duplicated). Use a permutation-preserving operator, e.g. **Order Crossover (OX)**:

Parent 1: `A B | C D E | F G H`, Parent 2: `D H | B A G | E C F`.
Copy the segment `C D E` from Parent 1, then fill the remaining positions with the cities of Parent 2 in their order, skipping ones already used, starting after the cut: Parent 2 order from position 6 is `E C F D H B A G`; skipping C, D, E gives `F H B A G`, so the child is `A G | C D E | F H B` (positions 6-8, then 1-2).

Justification: the child is always a valid tour and inherits a *sub-route* (adjacent cities) from one parent and the relative order from the other; adjacency is what determines tour length. PMX or edge-recombination are also acceptable.

**5. Mutation.** With small probability (e.g. 1-5%) apply *swap* mutation (exchange two cities) or *inversion* (2-opt style: reverse a sub-sequence, `A B [C D E] F` $\to$ `A B [E D C] F`). Justification: keeps the result a valid permutation and keeps diversity, so the population can escape local optima; inversion changes only two edges, so it is a small, meaningful step.

**6. Algorithm.**

```text
population <- N random permutations of the cities
repeat for G generations (or until no improvement):
    evaluate fitness = 1 / tour length for every tour
    new_pop <- best e tours (elitism)
    while |new_pop| < N:
        p1, p2 <- TOURNAMENT-SELECT(population)
        child  <- ORDER-CROSSOVER(p1, p2)   with probability pc, else copy p1
        child  <- INVERSION-MUTATE(child)   with probability pm
        add child to new_pop
    population <- new_pop
return the shortest tour found
```

Typical settings: $N=50$-$200$, $p_c\approx0.8$-$0.9$, $p_m\approx0.01$-$0.05$. The result is a near-optimal route.
