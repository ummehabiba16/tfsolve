---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Chromosome: the 5 distinct cell indices (0-24), or 5 (row, col) pairs; fitness = the minimum Euclidean distance over the 10 pairs (to maximize). Crossover: one-point on the list of 5 positions, repairing duplicates with random free cells (or uniform crossover with repair). Mutation: move one piece to a random free cell (or to an adjacent free cell). The optimum is the 4 corners plus the centre, with fitness 2 sqrt(2) = 2.83."
sources: ["AIMA 3e sec. 4.1.4 (genetic algorithms)"]
---
**Formulation.**

- **Individual (chromosome):** the positions of the 5 pieces, encoded as 5 **distinct cell indices** $k\in\{0,\dots,24\}$ (cell $k$ is at row $\lfloor k/5\rfloor$ and column $k\bmod5$), e.g. `[0, 4, 12, 20, 24]`. Equivalently, 5 $(r,c)$ pairs. The order does not matter.
- **Population:** for example 30-50 random individuals (5 distinct cells each).
- **Fitness function:** the minimum Euclidean distance among all $\binom52=10$ pairs, to be **maximized**:

$$fitness(I)=\min_{i<j}\sqrt{(r_i-r_j)^2+(c_i-c_j)^2}.$$

(Optionally add a small term, the average pairwise distance, to break ties.)

- **Selection:** tournament or fitness-proportional selection, plus elitism (keep the best individual).
- **Crossover:** one-point crossover on the 5-gene lists. Parents `[0, 4, 12 | 20, 24]` and `[1, 7, 13 | 18, 22]` give the children `[0, 4, 12, 18, 22]` and `[1, 7, 13, 20, 24]`. If a child contains a **duplicate** cell, repair it by replacing the duplicate with a random free cell. (Uniform crossover with repair also works.)
- **Mutation:** with a small probability (e.g. 0.1 per piece), move one piece to a random free cell, or to an adjacent free cell for fine-tuning.
- **Termination:** after a fixed number of generations, or when the best fitness stops improving.

**Expected result.** The optimum places the pieces at the **four corners and the centre**, cells $\{0,4,12,20,24\}$. Each corner is $2\sqrt2$ from the centre, and corners are 4 apart, so $fitness=2\sqrt2\approx2.83$. (This matches the best known packing of 5 points in a square.)
