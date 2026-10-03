---
marks: 20
topics: [bn-exact-inference]
kind: numerical
source: {page: 49}
---
Consider the following Bayesian Network. Find out the probability of the following query: $P(B \mid D = \text{True}, E = \text{False})$

![Bayesian network for Q8(b)](figures/q8b-1.png)

*Edges: $A \to C$, $B \to C$, $C \to D$, $C \to E$.*

The CPT (Conditional Probability Tables) are given below:

| P(B) | P(A) |
|:-:|:-:|
| 0.3 | 0.1 |

| A | B | P(C) |
|:-:|:-:|:-:|
| T | T | 0.95 |
| T | F | 0.94 |
| F | T | 0.29 |
| F | F | 0.01 |

| C | P(D) | P(E) |
|:-:|:-:|:-:|
| T | 0.90 | 0.7 |
| F | 0.05 | 0.01 |
