---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Fitness f = 5x1 - 3x2x3 + x3 - 2x4: parents 0110 -> -2, 1100 -> 5, 1011 -> 4, 0001 -> -2 (the maximum is 1010 -> 6). Next generation: shift fitness (+3) or use rank or tournament selection, so 1100 and 1011 are chosen most; crossover 101|1 x 110|0 gives 1010 (fitness 6, optimal) and 1101 (3); mutate a bit with small probability; keep the best (elitism)."
sources: ["AIMA 3e sec. 4.1.4 (genetic algorithms)"]
---
**Fitness of the initial population** ($f=5X_1-3X_2X_3+X_3-2X_4$, binary genes):

| Parent | $X_1X_2X_3X_4$ | $f$ |
|:-:|:-:|:-:|
| 1 | 0110 | $0-3+1-0=-2$ |
| 2 | 1100 | $5-0+0-0=5$ |
| 3 | 1011 | $5-0+1-2=4$ |
| 4 | 0001 | $0-0+0-2=-2$ |

(The global maximum is $X=1010$ with $f=6$: $X_1=1$, $X_3=1$, $X_2=0$, $X_4=0$.)

**Creating the next generation.**

1. **Selection.** Fitness-proportional (roulette-wheel) selection needs non-negative values, so shift the fitness by +3, giving 1, 8, 7, 1 (total 17). The selection probabilities are about 6%, 47%, 41% and 6%. Alternatively use **rank** or **tournament** selection. Parents 2 (1100) and 3 (1011) will be picked most often, for example the pairs (2, 3), (3, 2), (2, 1), (3, 4).
2. **Crossover.** Choose a crossover point at random and swap the tails. For example, parents 3 and 2 crossed after the third bit:

$$101|1\ \times\ 110|0\ \longrightarrow\ 101|0=\mathbf{1010}\ (f=6),\qquad 110|1=1101\ (f=3).$$

Crossing 2 and 1 after the first bit: $1|100\times0|110$ gives 1110 ($f=3$) and 0100 ($f=0$).
3. **Mutation.** Flip each bit with a small probability (e.g. 0.05) to keep diversity. For example, 1101 might become 1100.
4. **Elitism / replacement.** Keep the best individuals (e.g. 1010 and 1100). The new population could be {1010, 1100, 1011, 1110}, whose average fitness ($\frac{6+5+4+3}{4}=4.5$) is much higher than the parents' ($\frac{5}{4}=1.25$).

Repeat until the population converges. Here the optimum 1010 ($f=6$) can appear in the first generation.
