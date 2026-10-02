---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(\text{exactly }j\text{ matches})=\frac{1}{j!}\sum_{r=0}^{n-j}\frac{(-1)^r}{r!}\approx\frac{e^{-1}}{j!}$ for large $n$, so $P(\text{at most }k)\approx\sum_{j=0}^{k}\frac{e^{-1}}{j!}$ (the number of matches is approximately Poisson(1)).'
sources: ['Ross, Introduction to Probability Models, Ch. 2-3 (the matching problem)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 1 and 4 (matching problem, Poisson approximation)']
---
Let $E_i$ be the event that man $i$ gets his own hat. All $n!$ ways of handing out the hats are equally likely.

**Probability of no matches.** For any $i_1<\cdots<i_r$, the men $i_1,\dots,i_r$ all get their own hats in $(n-r)!$ of the $n!$ arrangements, so $P(E_{i_1}\cdots E_{i_r})=\frac{(n-r)!}{n!}$, and there are $\binom nr$ such sets. By inclusion-exclusion,

$$P\Big(\bigcup_{i=1}^{n}E_i\Big)=\sum_{r=1}^{n}(-1)^{r+1}\binom nr\frac{(n-r)!}{n!}=\sum_{r=1}^{n}\frac{(-1)^{r+1}}{r!}$$

$$P_n=P(\text{no matches})=1-\sum_{r=1}^{n}\frac{(-1)^{r+1}}{r!}=\sum_{r=0}^{n}\frac{(-1)^r}{r!}$$

$$=1-1+\frac1{2!}-\frac1{3!}+\cdots+\frac{(-1)^n}{n!}\approx e^{-1}\approx0.3679$$

**Probability of exactly $k$ matches.** Fix a set of $k$ men. The probability that exactly these $k$ men match is

$$\frac{(n-k)!}{n!}\cdot P_{n-k}$$

because the $k$ men all get their own hats with probability $\frac{(n-k)!}{n!}$, and then the other $n-k$ men are randomly matched with their own $n-k$ hats and must have no match (probability $P_{n-k}$). There are $\binom nk$ sets of $k$ men, so

$$P(\text{exactly }k\text{ matches})=\binom nk\frac{(n-k)!}{n!}P_{n-k}=\frac{P_{n-k}}{k!}$$

$$=\frac{1}{k!}\sum_{r=0}^{n-k}\frac{(-1)^r}{r!}\approx\frac{e^{-1}}{k!}\quad\text{for large }n$$

So for large $n$ the number of matches is approximately Poisson with mean 1.

**Probability of at most $k$ matches.** Adding the exact probabilities for $j=0,1,\dots,k$:

$$P(\text{at most }k\text{ matches})=\sum_{j=0}^{k}\frac{1}{j!}\sum_{r=0}^{n-j}\frac{(-1)^r}{r!}$$

For large $n$ each inner sum is essentially $e^{-1}$, so

$$P(\text{at most }k\text{ matches})\approx e^{-1}\sum_{j=0}^{k}\frac{1}{j!}=e^{-1}\left(1+1+\frac1{2!}+\cdots+\frac1{k!}\right)$$

This is the Poisson(1) CDF at $k$. For example, $P(\text{at most 1 match})\approx2e^{-1}\approx0.736$ and $P(\text{at most 2})\approx2.5e^{-1}\approx0.920$.
