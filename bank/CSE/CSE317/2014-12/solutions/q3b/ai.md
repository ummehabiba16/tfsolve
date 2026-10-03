---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Evolutionary algorithms keep a population of candidate solutions (individuals) and repeatedly evaluate fitness, select parents by fitness, recombine them (crossover) and mutate them, forming a new generation, until a good solution appears (a stochastic beam search with recombination). Self-adaptation: strategy parameters such as mutation step sizes or rates are encoded in each individual and evolve with it, so the algorithm tunes its own search parameters (as in evolution strategies)."
sources: ["AIMA 3e sec. 4.1.4 (genetic algorithms)", "Eiben & Smith, Introduction to Evolutionary Computing, ch. 4 and 8 (self-adaptation)"]
---
**How evolutionary algorithms work** (8). They are inspired by natural selection and work on a **population** of candidate solutions (individuals), each encoded as a string (chromosome): bits, digits or real numbers.

1. **Initialize** a random population of $k$ individuals.
2. **Evaluate** each individual with a **fitness function** (higher means better).
3. **Selection:** choose parents with probability increasing with fitness (roulette wheel, tournament or rank selection).
4. **Recombination (crossover):** combine parts of two parents to make offspring (one-point, two-point or uniform crossover). This lets good partial solutions ("building blocks") from different parents come together.
5. **Mutation:** randomly change small parts of the offspring with low probability, keeping diversity and exploring new regions.
6. **Replacement:** form the next generation (possibly keeping the best: elitism).
7. **Repeat** steps 2-6 until a good enough individual is found or a generation limit is reached.

Variants: genetic algorithms (bit strings, crossover-centred), evolution strategies (real vectors, mutation-centred), genetic programming (evolving programs as trees). They are a population-based, stochastic local search; they escape local optima better than hill climbing.

**Self-adaptation** (4). The algorithm's **own strategy parameters**, such as the mutation step size $\sigma$ or the mutation rate, are **encoded in each individual** alongside its solution, for example $\langle x_1,\dots,x_n,\sigma\rangle$. They are mutated and selected together with the solution. Individuals with good parameter settings produce fitter offspring and spread, so the search parameters **evolve and tune themselves** during the run (large steps early, small steps near an optimum), with no external schedule. This is typical of evolution strategies.
