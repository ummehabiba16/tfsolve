---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Components: representation (genotype), initial population, fitness (evaluation) function, parent selection, variation operators (recombination and mutation), survivor selection (replacement), and termination condition; the loop evaluates, selects, recombines, mutates and replaces until termination."
sources: ["Eiben and Smith, Introduction to Evolutionary Computing, ch. 3 (What is an evolutionary algorithm?)", "AIMA 3e sec. 4.1.4"]
---
**Basic idea.** A population of candidate solutions evolves: fitter individuals are more likely to reproduce, offspring are created by recombination and mutation, and competition for survival raises the population's fitness over generations (Darwinian selection plus random variation).

```text
BEGIN
    INITIALISE population with random candidate solutions
    EVALUATE each candidate
    REPEAT UNTIL termination condition is satisfied
        1. SELECT parents
        2. RECOMBINE pairs of parents
        3. MUTATE the resulting offspring
        4. EVALUATE new candidates
        5. SELECT individuals for the next generation
    OD
END
```

**Components.**

1. **Representation (encoding)**: maps the problem's solutions (phenotypes) to chromosomes (genotypes): bit strings, integers, real vectors, permutations, trees. E.g. 8-queens: 8 integers giving each column's queen row.

2. **Fitness (evaluation) function**: measures quality of an individual; it is the objective to optimise (e.g. number of non-attacking queen pairs).

3. **Population**: the multiset of current individuals; its size is usually fixed; diversity in it is important.

4. **Parent selection**: chooses individuals to reproduce, favouring better ones but probabilistically, so weak ones still have a chance: fitness-proportional (roulette wheel), rank-based, tournament.

5. **Variation operators**:

- *Recombination (crossover)*: combines information from two (or more) parents, e.g. one-point crossover `110|0101` + `001|1100` $\to$ `110 1100`, `001 0101`.

- *Mutation*: small random change of a single individual, e.g. flip each bit with probability $1/L$; keeps diversity and introduces new genetic material.

6. **Survivor selection (replacement)**: decides which individuals form the next generation: generational (offspring replace parents), steady-state, ($\mu+\lambda$) or ($\mu,\lambda$), often with elitism (keep the best).

7. **Initialisation**: usually random; sometimes seeded with heuristic solutions.

8. **Termination condition**: maximum number of generations or fitness evaluations, a known optimum reached, or no improvement for some generations (loss of diversity).

Selection drives the population toward better solutions (exploitation); variation creates new candidates (exploration). Balancing them is the key design issue.
