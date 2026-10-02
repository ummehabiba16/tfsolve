---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A package is returned w.p. $q=1-0.99^{10}=0.0956$; returns among 3 packages $\sim\text{Bin}(3,q)$, so $P(\text{exactly 1})=3q(1-q)^2\approx0.2346$.'
sources: ['Ross, Introduction to Probability Models, Ch. 2 (binomial random variables)']
---
**One package.** Each of the 10 DVDs is defective with probability 0.01, independently, so the number of defective DVDs in a package is $\text{Bin}(10,\ 0.01)$. A package is returned if it has at least one defective DVD:

$$q=P(\text{package returned})=1-P(\text{no defective})=1-(0.99)^{10}=1-0.90438=0.09562$$

**Three packages.** Packages are independent, so the number $R$ of the 3 packages returned is $\text{Bin}(3,\ q)$:

$$P(R=1)=\binom31q(1-q)^2=3(0.09562)(0.90438)^2\approx\mathbf{0.2346}$$
