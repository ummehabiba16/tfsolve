---
marks: 13
topics: [bn-exact-inference]
kind: numerical
source: {page: 55}
set_by: [UNKNOWN]
note: "Hand-drawn figure; the CPT values are read as the standard burglary network (P(A): .95, .94, .29, .001; P(J): .9, .05; P(M): .7, .01). Check them against the scan."
---
For the given Bayesian Network find the correctness of the following query, $P(B \mid J = \text{true}, M = \text{true})$ using variable elimination method. (Show the calculations).

![Figure for 2(c)](figures/q2c-1.png)

*Edges: $B \to A$, $E \to A$, $A \to J$, $A \to M$. $P(B) = .001$, $P(E) = .002$.*

| B | E | P(A) |
|:-:|:-:|:-:|
| t | t | .95 |
| t | f | .94 |
| f | t | .29 |
| f | f | .001 |

| A | P(J) | P(M) |
|:-:|:-:|:-:|
| t | .9 | .7 |
| f | .05 | .01 |
