---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "All three are evolutionary algorithms but differ in representation and operators: GAs evolve fixed-length (often binary) strings mainly by crossover; evolutionary programming evolves real-valued vectors or finite-state machines by mutation only (no crossover); genetic programming evolves variable-size programs (parse trees) by subtree crossover and mutation."
sources: ["Eiben and Smith, Introduction to Evolutionary Computing, ch. 4-6", "AIMA 3e sec. 4.1.4 (Bibliographical notes)"]
---
All three are **evolutionary algorithms**: a population evolves through selection and variation, guided by a fitness function. They differ mainly in what is evolved and which variation operators dominate.

| | Genetic algorithm (GA) | Evolutionary programming (EP) | Genetic programming (GP) |
|:--|:--|:--|:--|
| Origin | Holland (1975) | L. Fogel (1960s), later D. Fogel | Koza (1992) |
| Individuals | fixed-length strings (binary, integer, permutation) | real-valued vectors (originally finite-state machines) | computer programs: variable-size parse trees (e.g. Lisp expressions) |
| Main operator | **crossover** (recombination); mutation secondary, low rate | **mutation only** (e.g. Gaussian with self-adapted step sizes); no crossover | subtree **crossover** (swap subtrees); subtree mutation |
| Selection | fitness-proportional / tournament for parents, generational replacement | each parent produces offspring; ($\mu+\mu$) stochastic tournament for survivors | tournament / fitness-proportional |
| Typical use | combinatorial optimisation (scheduling, TSP, design) | continuous optimisation, prediction (FSMs) | automatic program/formula synthesis, symbolic regression |
| Size of solution | fixed | fixed | grows during evolution (bloat) |

**Key differences in words.**

- A **GA** treats a solution like a chromosome (genotype) and relies on crossover to combine good building blocks from two parents.

- **EP** treats each individual as a species and works at the phenotypic level; variation is only by mutation, often with mutation parameters that are themselves evolved (self-adaptation).

- **GP** evolves executable structures; fitness is computed by running the program on test cases, so the result is a program/formula, not a parameter vector.

Example: to fit a function to data, a GA could evolve the coefficients of a fixed polynomial, EP could mutate a real vector of coefficients, while GP would evolve the formula itself, such as `(+ (* x x) (sin x))`.
