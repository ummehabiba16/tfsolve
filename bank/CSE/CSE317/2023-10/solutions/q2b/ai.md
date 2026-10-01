---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Path (permutation) representation, fitness 1/tour length, tournament/rank selection with elitism, order crossover (OX) or PMX, swap/inversion mutation, repeated for many generations to give a near-optimal tour."
sources: ["AIMA 3e sec. 4.1.4", "Eiben and Smith, Introduction to Evolutionary Computing, sec. 4.5 (Permutation representation)"]
---
TSP has $(n-1)!/2$ possible tours, so exhaustive search is infeasible for large $n$. A genetic algorithm (GA) searches with a population of tours.

**Representation.** Path representation: a chromosome is a permutation of the cities, e.g. with 8 cities `3 5 1 8 2 7 4 6` = tour 3$\to$5$\to$1$\to$8$\to$2$\to$7$\to$4$\to$6$\to$3. Every permutation is a legal tour, every tour is representable. (A binary encoding would create invalid tours after crossover.)

**Initial population.** $N$ (e.g. 100) random permutations, possibly plus a few greedy nearest-neighbour tours.

**Fitness.** Tour length $L=\sum_{i=1}^{n-1} d(c_i,c_{i+1}) + d(c_n,c_1)$; fitness $=1/L$ (shorter is fitter).

**Selection.** Tournament selection (choose $k=2$-$5$ tours at random, the shortest becomes a parent) or rank-based selection; elitism keeps the best tours unchanged.

**Crossover: Order crossover (OX).**

1. Pick two cut points; copy the segment between them from parent 1 into the child.

2. Starting after the second cut, fill the remaining positions with the cities of parent 2 in the order they appear (from after the second cut, wrapping around), skipping cities already in the child.

Example: P1 = `1 2 | 3 4 5 | 6 7 8`, P2 = `4 6 | 8 1 7 | 3 5 2`. Child segment `3 4 5`; P2 order after cut: `3 5 2 4 6 8 1 7`, skipping 3, 4, 5 gives `2 6 8 1 7`; child = `1 7 | 3 4 5 | 2 6 8`. The child is a valid tour that keeps a sub-route of P1 and the relative order of P2. PMX (partially mapped crossover) or edge recombination are alternatives; edge recombination preserves adjacencies best.

**Mutation.** With small probability: *swap* two cities, or *inversion*: reverse a segment (`1 2 [3 4 5] 6` $\to$ `1 2 [5 4 3] 6`), which is a 2-opt move that removes two edges and adds two, often removing a crossing in the tour.

**Algorithm.**

```text
P <- N random tours
repeat until G generations or no improvement for many generations:
    compute fitness 1/L for every tour in P
    P' <- elite (best e tours)
    while |P'| < N:
        a, b  <- TOURNAMENT(P), TOURNAMENT(P)
        child <- OX(a, b) with probability pc  else copy of a
        child <- INVERSION(child) with probability pm
        P' <- P' + {child}
    P <- P'
return the shortest tour in P
```

Parameters: $N\approx100$, $p_c\approx0.9$, $p_m\approx0.02$-$0.1$. Optionally apply 2-opt local search to each child (a memetic algorithm), which greatly improves tour quality.
