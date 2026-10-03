---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Class Y is the single parent of F1, F2, F3 (no edges between features). Parameters: the prior P(Y) and the conditional tables P(F1|Y), P(F2|Y), P(F3|Y); for binary Y and F: 1 + 3 x 2 = 7 independent numbers."
sources: ["AIMA 4e sec. 12.6 (naive Bayes models)", "Berkeley CS188 Naive Bayes lecture"]
---
**Topology.** The class variable $Y$ is the only parent of every feature, and the features are not connected to each other:

```text
              Y   (class)
           /  |  \
          v   v   v
         F1   F2   F3   (features)
```

This encodes the naive Bayes assumption that the features are conditionally independent given the class:

$$P(Y,F_1,F_2,F_3)=P(Y)\prod_{i=1}^{3}P(F_i\mid Y),\qquad P(Y\mid f_1,f_2,f_3)\propto P(Y)\prod_iP(f_i\mid Y).$$

**Parameters to learn.**

- The **prior** $P(Y)$: $|Y|-1$ independent numbers.
- One **conditional probability table per feature**, $P(F_i\mid Y)$ for $i=1,2,3$: $|Y|\,(|F_i|-1)$ numbers each.

For binary class and features: $P(y)$ is 1 number, and $P(F_i=1\mid y)$, $P(F_i=1\mid\neg y)$ are 2 numbers per feature. That is $1+3\times2=\mathbf{7}$ parameters, against $2^4-1=15$ for the full joint. They are estimated by counting (relative frequencies) on the training data, usually with Laplace smoothing.
