---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "EAs evolve a population: initialise, evaluate fitness, select parents, recombine, mutate, select survivors, repeat until termination. Self-adaptation: the strategy parameters (e.g. mutation step sizes sigma) are encoded in the individuals and evolve with them, so good parameter values are selected automatically; it is needed because the best parameters are problem-dependent and change during the run."
sources: ["Eiben and Smith, Introduction to Evolutionary Computing, ch. 3-4 and 8 (Parameter control)"]
---
**How evolutionary algorithms work.** EAs imitate natural evolution on a population of candidate solutions:

1. **Initialise** a population of random individuals (encoded solutions).

2. **Evaluate** each individual with the fitness function.

3. **Parent selection**: fitter individuals are more likely to become parents (roulette wheel, tournament, rank).

4. **Recombination (crossover)**: combine parents to produce offspring.

5. **Mutation**: make small random changes to offspring.

6. **Survivor selection**: choose which individuals form the next generation (generational, $(\mu+\lambda)$, $(\mu,\lambda)$, elitism).

7. **Repeat** until a termination condition (generations, target fitness, stagnation).

Selection exploits good solutions; variation (crossover, mutation) explores new ones. Over generations average fitness increases.

**Self-adaptation.** EAs have **strategy parameters**: mutation rate or step size $\sigma$, crossover rate, etc. In self-adaptation these parameters are **encoded in each individual's chromosome alongside the solution** and are themselves subject to mutation and recombination. Individuals with good parameter values tend to produce better offspring, so those values are selected indirectly ("evolution of evolution").

Example (evolution strategies): individual $\langle x_1,\dots,x_n,\sigma\rangle$. Mutation first changes the step size, $\sigma'=\sigma\,e^{\tau N(0,1)}$, then the solution, $x_i'=x_i+\sigma' N_i(0,1)$. Individuals with a suitable $\sigma$ (large when far from the optimum, small when close) produce fitter offspring and survive, so $\sigma$ adapts automatically.

**Necessity in AI.**

- The best parameter values are **problem-specific** and unknown in advance; hand-tuning is expensive and requires expertise.

- The best values **change during the run**: large steps are useful early (exploration), small steps late (fine-tuning). A fixed value cannot be optimal throughout.

- Self-adaptation makes the algorithm robust, autonomous and able to track **dynamic environments**, which matches the AI goal of systems that adapt themselves rather than relying on their designer's settings.
