---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Individual = 8 digits, the row of the queen in each column (e.g. 24748552); fitness = number of non-attacking pairs (max 28). Selection probability proportional to fitness (24/78 = 31%, 23 = 29%, 20 = 26%, 11 = 14%); crossover at a random point (327|48552 + 247|52411 gives 32748552); mutation changes one digit (one queen moves within its column) with small probability; repeat until fitness 28."
sources: ["AIMA 3e sec. 4.1.4 (genetic algorithms, Fig. 4.6-4.8)"]
---
**1. Representation of an individual.** A string of 8 digits, one per column. Digit $i\in\{1..8\}$ gives the **row of the queen in column $i$**. For example, `24748552` means the queen of column 1 is in row 2, of column 2 in row 4, and so on. This encoding already guarantees one queen per column. (A 24-bit binary string would also work.)

**2. Fitness function.** The number of **non-attacking pairs** of queens. The maximum is $\binom82=28$ for a solution.

**3. Initial population.** For example, $k=4$ random individuals:

| Individual | Fitness | Selection probability |
|:--|:-:|:-:|
| 24748552 | 24 | 24/78 = 31% |
| 32752411 | 23 | 29% |
| 24415124 | 20 | 26% |
| 32543213 | 11 | 14% |

(Sum = 78.)

**4. Selection.** Choose pairs of parents at random, with probability proportional to fitness (roulette wheel). For example, the pairs (32752411, 24748552) and (32752411, 24415124). The weakest may not be chosen at all, and one individual can be chosen twice.

**5. Crossover.** For each pair, pick a random crossover point and swap the tails:

- parents `327|52411` and `247|48552` give children `327|48552` and `247|52411`;
- parents `32752|411` and `24415|124` give `32752124` and `24415411`.

The child takes the queens of the first 3 columns from one parent and the rest from the other, so good "blocks" of non-attacking queens are combined.

**6. Mutation.** Each digit is changed to a random value with a small probability (e.g. 1/8 per child). For example `32748552` becomes `32748152`: one queen moves to another row in its column. This keeps diversity.

**7. Repeat** with the new population until an individual with fitness 28 appears (a solution, e.g. `16257483`) or a generation limit is reached.
