---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Accuracy 0.975 for both positive and negative cases, prevalence 1/50,000. (i) P(no disease | positive) = 0.025(49,999/50,000) / [0.975/50,000 + 0.025(49,999/50,000)] = 0.99922. (ii) P(disease | negative) = 0.025/50,000 / [0.025/50,000 + 0.975(49,999/50,000)] = 5.1 x 10^-7."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes rule)", "AIMA 3e sec. 13.5"]
---
**Given.** $P(d)=\frac{1}{50{,}000}=2\times10^{-5}$ and accuracy 97.5% (assumed the same for both classes): $P(+\mid d)=P(-\mid\neg d)=0.975$, so $P(-\mid d)=P(+\mid\neg d)=0.025$.

**(i) $P(\neg d\mid +)$.**

$$P(+)=P(+\mid d)P(d)+P(+\mid\neg d)P(\neg d)=0.975(2\times10^{-5})+0.025(0.99998)$$

$$=1.95\times10^{-5}+0.0249995=0.025019$$

$$P(\neg d\mid +)=\frac{0.025\times0.99998}{0.025019}=\mathbf{0.99922}$$

Even after a positive test, there is a 99.9% chance of **not** having the disease, because the disease is extremely rare.

**(ii) $P(d\mid -)$.**

$$P(-)=0.025(2\times10^{-5})+0.975(0.99998)=5\times10^{-7}+0.97498=0.97498$$

$$P(d\mid -)=\frac{0.025\times2\times10^{-5}}{0.97498}=\mathbf{5.13\times10^{-7}}$$

That is about 1 in 2 million.
