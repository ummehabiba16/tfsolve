---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Negative binomial (failures before the $r$-th success) is a sum of $r$ geometrics with mean $q/p$ each, so $E[X]=r(1-p)/p$ (or $r/p$ if it counts trials). Poisson: $E[X]=\sum_k k\,e^{-\lambda}\lambda^k/k!=\lambda$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 4 (geometric and negative binomial distributions, Poisson distribution)', 'Ross, Introduction to Probability Models, Ch. 2']
---
Throughout, $q=1-p$.

**Negative binomial.** Independent Bernoulli($p$) trials are performed until the $r$-th success. Let $X$ be the number of **failures** before the $r$-th success, $X\sim\text{NBin}(r,p)$:

$$P(X=n)=\binom{n+r-1}{r-1}p^r q^n,\qquad n=0,1,2,\dots$$

Write $X=X_1+X_2+\cdots+X_r$, where $X_i$ is the number of failures between the $(i-1)$-st and the $i$-th success. The $X_i$ are i.i.d. geometric: $P(X_i=k)=q^kp$, $k=0,1,2,\dots$

*Mean of a geometric.* Differentiating $\sum_{k\ge0}q^k=\frac{1}{1-q}$ gives $\sum_{k\ge1}kq^{k-1}=\frac{1}{(1-q)^2}$, so

$$E[X_i]=\sum_{k=0}^{\infty}k\,q^kp=pq\sum_{k=1}^{\infty}kq^{k-1}=\frac{pq}{(1-q)^2}=\frac{q}{p}$$

By linearity of expectation,

$$E[X]=r\cdot\frac{q}{p}=\frac{r(1-p)}{p}$$

If instead the negative binomial counts the **total number of trials** $Y$ needed for $r$ successes (Ross's convention, $P(Y=n)=\binom{n-1}{r-1}p^rq^{n-r}$ for $n\ge r$), then $Y=X+r$ and

$$E[Y]=\frac{rq}{p}+r=\frac{r}{p}$$

**Poisson.** $X\sim\text{Pois}(\lambda)$ has $P(X=k)=e^{-\lambda}\lambda^k/k!$ for $k=0,1,2,\dots$ The $k=0$ term of the sum is zero, so

$$E[X]=\sum_{k=1}^{\infty}k\,\frac{e^{-\lambda}\lambda^k}{k!}=\lambda e^{-\lambda}\sum_{k=1}^{\infty}\frac{\lambda^{k-1}}{(k-1)!}$$

$$=\lambda e^{-\lambda}\,e^{\lambda}=\lambda$$

**Answer:** negative binomial: $E[X]=r(1-p)/p$ failures (equivalently $r/p$ trials); Poisson: $E[X]=\lambda$.
