---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'If $X_1,\dots,X_n$ are i.i.d. with mean $\mu$ and finite variance $\sigma^2$, then $\frac{\bar X_n-\mu}{\sigma/\sqrt n}=\frac{S_n-n\mu}{\sigma\sqrt n}\to N(0,1)$ in distribution, whatever the distribution of the $X_i$; so for large $n$, $\bar X_n\approx N(\mu,\sigma^2/n)$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 10 (central limit theorem)', 'Ross, Introduction to Probability Models, Ch. 2 (limit theorems)']
---
**Statement.** Let $X_1,X_2,\dots$ be independent and identically distributed with mean $\mu$ and finite variance $\sigma^2>0$, and let $S_n=X_1+\cdots+X_n$ and $\bar X_n=S_n/n$. Then for every real $x$,

$$\lim_{n\to\infty}P\left(\frac{S_n-n\mu}{\sigma\sqrt n}\le x\right)=\Phi(x)$$

i.e. the standardised sum (equivalently $\frac{\bar X_n-\mu}{\sigma/\sqrt n}$) converges in distribution to $N(0,1)$.

**Explanation.**

- It holds whatever the distribution of the $X_i$ (discrete or continuous, skewed or not), as long as the variance is finite. That is why normal distributions appear so often: totals of many small independent effects are approximately normal.
- In practice, for large $n$: $S_n\approx N(n\mu,\ n\sigma^2)$ and $\bar X_n\approx N(\mu,\ \sigma^2/n)$. The spread of the sample mean shrinks like $\sigma/\sqrt n$.
- Example: $\text{Bin}(n,p)$ is a sum of $n$ Bernoulli($p$) variables, so for large $n$ it is approximately $N(np,\ np(1-p))$ (the normal approximation to the binomial).
- How large $n$ must be depends on how skewed the $X_i$ are; $n\ge30$ is a common rule of thumb.
