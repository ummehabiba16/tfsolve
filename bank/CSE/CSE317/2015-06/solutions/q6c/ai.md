---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(disease | positive) = 0.99(0.00001) / [0.99(0.00001) + 0.01(0.99999)] = 9.9e-6 / 0.0100098 = 0.00099, about 0.1% (about 1 in 1000); P(no disease | positive) = 0.999. The disease is so rare that false positives (1% of everyone) vastly outnumber true positives."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes rule)", "AIMA 3e Exercise 13.8"]
---
**Given.** $P(d)=1/100{,}000=10^{-5}$; $P(+\mid d)=0.99$; $P(-\mid\neg d)=0.99$, so $P(+\mid\neg d)=0.01$.

**Bayes' rule.**

$$P(d\mid +)=\frac{P(+\mid d)P(d)}{P(+\mid d)P(d)+P(+\mid\neg d)P(\neg d)}$$

$$=\frac{0.99\times10^{-5}}{0.99\times10^{-5}+0.01\times0.99999}=\frac{9.9\times10^{-6}}{0.0100098}$$

$$P(d\mid +)=\mathbf{0.00099}\approx0.1\%,\qquad P(\neg d\mid +)=\mathbf{0.99901}\approx99.9\%.$$

**Interpretation.** Despite the 99% accurate test, your friend almost certainly does **not** have the disease: the chance is only about 1 in 1000. Out of 100,000 people, about 1 has the disease (and tests positive), while about 1000 healthy people test positive falsely. This is the *base-rate* effect: a very low prior dominates. (The positive test still raised the probability a hundredfold, from $10^{-5}$ to $10^{-3}$.)
