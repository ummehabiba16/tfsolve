---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'All $\binom{20}{5}=15504$ draws are equally likely; favourable: $\binom52\binom52\binom{10}{1}=1000$. $P=\frac{1000}{15504}=\frac{125}{1938}\approx0.0645$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 1 (naive definition of probability; hypergeometric counting)']
---
Five of the twenty tickets are drawn, without replacement and without regard to order, so all

$$\binom{20}{5}=15504$$

sets of five winning tickets are equally likely.

**Favourable outcomes.** Choose 2 winners from the 5 tickets numbered 1-5, 2 from the 5 tickets numbered 6-10, and 1 from the 10 tickets numbered 11-20:

$$\binom52\binom52\binom{10}{1}=10\times10\times10=1000$$

**Probability.**

$$P=\frac{1000}{15504}=\frac{125}{1938}\approx\mathbf{0.0645}$$
