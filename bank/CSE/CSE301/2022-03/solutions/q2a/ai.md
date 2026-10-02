---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) Two-day total $\sim$ Pois(4): $P(6)=e^{-4}4^6/6!\approx0.1042$. (ii) $P(\text{exactly 2 in a day})=2e^{-2}=0.2707$; days with exactly two $\sim\text{Bin}(5,0.2707)$, $P(\ge3)\approx0.1265$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 4 (Poisson distribution, sums of independent Poissons)', 'Ross, Introduction to Probability Models, Ch. 2']
---
Let $X_i\sim\text{Pois}(2)$ be the number of accidents on day $i$, independently.

**(i) Six accidents over two days.** The sum of independent Poisson variables is Poisson with the sum of the means, so $X_1+X_2\sim\text{Pois}(4)$:

$$P(X_1+X_2=6)=e^{-4}\frac{4^6}{6!}=e^{-4}\cdot\frac{4096}{720}\approx\mathbf{0.1042}$$

**(ii) At least three of five days with exactly two accidents.** For one day,

$$p=P(X_i=2)=e^{-2}\frac{2^2}{2!}=2e^{-2}\approx0.2707$$

Days are independent, so the number $K$ of the five days (Sat-Wed) with exactly two accidents is $\text{Bin}(5,\ p)$:

$$P(K\ge3)=\sum_{k=3}^{5}\binom5kp^k(1-p)^{5-k}$$

$$=10p^3(1-p)^2+5p^4(1-p)+p^5\approx0.1055+0.0196+0.0015\approx\mathbf{0.1265}$$
