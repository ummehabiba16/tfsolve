---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Classical algorithms are deterministic, single-solution, problem-specific and often need gradients/structure; evolutionary algorithms are stochastic, population-based, need only a fitness function and suit large, multimodal, poorly understood problems. A GA encodes solutions as chromosomes and repeats fitness evaluation, selection, crossover and mutation."
sources: ["AIMA 3e sec. 4.1.4 (Genetic algorithms)", "Eiben and Smith, Introduction to Evolutionary Computing, ch. 2-3"]
---
**Classical vs evolutionary algorithms.**

| Classical algorithms | Evolutionary algorithms |
|:--|:--|
| Deterministic: same input, same steps and result | Stochastic: random initialisation, selection, variation |
| Work on one candidate solution at a time | Work on a population of solutions in parallel |
| Need problem structure: gradients, convexity, exact model | Need only a fitness (objective) value: black-box |
| Exact/optimal for problems they fit (e.g. Dijkstra, simplex) | Near-optimal, no guarantee, but robust |
| Can get stuck in local optima (gradient descent, hill climbing) | Population and mutation keep diversity, good for multimodal landscapes |
| Often intractable for NP-hard problems (TSP, scheduling) | Scale to large combinatorial problems; anytime |
| Problem-specific design | Generic framework; easily adapted, hybridised, parallelised |

**Genetic algorithm (GA).**

1. **Representation**: each candidate solution is encoded as a chromosome (bit string, real vector or permutation). E.g. 8-queens: string of 8 digits, digit $i$ = row of queen in column $i$.

2. **Initial population** of $N$ random individuals.

3. **Fitness function** evaluates each individual (8-queens: number of non-attacking pairs, max 28).

4. **Selection**: parents are chosen with probability proportional to fitness (roulette wheel), by tournament or by rank.

5. **Crossover** (recombination) with probability $p_c$: a crossover point is chosen and the parents' strings are swapped after it. Example: `327|52411` + `247|48552` $\to$ `32748552` and `24752411`.

6. **Mutation** with small probability $p_m$ per gene: a random gene is changed (e.g. a queen moved to a random row). This restores lost diversity.

7. **Replacement**: offspring form the next generation (often with elitism, keeping the best).

8. **Termination**: after a fixed number of generations, when a good enough solution is found, or when the population converges.

```text
function GENETIC-ALGORITHM(population, FITNESS):
    repeat
        new_population <- empty
        for i = 1 to SIZE(population):
            x <- SELECT(population, FITNESS);  y <- SELECT(population, FITNESS)
            child <- CROSSOVER(x, y)
            if RANDOM() < p_m: child <- MUTATE(child)
            add child to new_population
        population <- new_population
    until some individual is fit enough, or enough time has elapsed
    return the best individual in population
```

Crossover is useful because it combines good "building blocks" (schemata) found by different parents; selection pushes the population uphill; mutation prevents premature convergence.
