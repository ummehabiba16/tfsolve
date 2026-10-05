---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) P(cancer | +) = 0.8 x 0.01 / (0.8 x 0.01 + 0.096 x 0.99) = 0.008/0.10304 = 0.0776 (7.8%). (ii) Naive Bayes (M1, M2 independent given cancer status): P(c | +, +) = 0.01 x 0.8^2 / (0.01 x 0.64 + 0.99 x 0.096^2) = 0.0064/0.015524 = 0.412."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes rule)", "AIMA 3e sec. 13.5.2 (combining evidence, naive Bayes)"]
---
**Given.** $P(c)=0.01$, $P(+\mid c)=0.80$, $P(+\mid\neg c)=0.096$.

**(i) One positive mammogram.**

$$P(c\mid +)=\frac{P(+\mid c)P(c)}{P(+\mid c)P(c)+P(+\mid\neg c)P(\neg c)}=\frac{0.8\times0.01}{0.8\times0.01+0.096\times0.99}$$

$$=\frac{0.008}{0.008+0.09504}=\frac{0.008}{0.10304}=\mathbf{0.0776}\ (\approx7.8\%)$$

Most positive results are false positives, because the disease is rare (the base rate).

**(ii) Two positive mammograms, $M_1$ and $M_2$.** The naive Bayes assumption says the tests are **conditionally independent given cancer status**:

$$P(M_1^+,M_2^+\mid c)=P(+\mid c)^2=0.64,\qquad P(M_1^+,M_2^+\mid\neg c)=0.096^2=0.009216.$$

$$P(c\mid M_1^+,M_2^+)=\frac{0.64\times0.01}{0.64\times0.01+0.009216\times0.99}$$

$$=\frac{0.0064}{0.0064+0.009124}=\frac{0.0064}{0.015524}=\mathbf{0.412}$$

The second positive test raises the probability from 7.8% to about **41%**. Equivalently, the posterior from (i) becomes the new prior for the second test.
