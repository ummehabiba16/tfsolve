---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Moments $E[X^k]=M^{(k)}(0)$ with $M(t)=E[e^{tX}]$. Poisson: $M(t)=\sum_ke^{tk}e^{-\lambda}\frac{\lambda^k}{k!}=e^{\lambda(e^t-1)}$ (mean $\lambda$, variance $\lambda$). For independent Poissons, $M_{X+Y}=e^{(\lambda_1+\lambda_2)(e^t-1)}$, so $X+Y\sim\text{Pois}(\lambda_1+\lambda_2)$.'
sources: ['Ross, Introduction to Probability Models, Ch. 2 (moment generating functions)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 6']
---
**Moments.** The $k$-th moment of a random variable $X$ is $E[X^k]$ ($k=1,2,\dots$); the first moment is the mean and $\mathrm{Var}(X)=E[X^2]-(E[X])^2$.

**From the moment generating function.** $M(t)=E[e^{tX}]=\sum_k\frac{E[X^k]}{k!}t^k$, so the moments are the derivatives at 0:

$$E[X^k]=M^{(k)}(0)$$

**MGF of the Poisson distribution.** For $X\sim\text{Pois}(\lambda)$,

$$M(t)=\sum_{k=0}^{\infty}e^{tk}\,e^{-\lambda}\frac{\lambda^k}{k!}=e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda e^t)^k}{k!}=e^{-\lambda}e^{\lambda e^t}=e^{\lambda(e^t-1)}$$

Check: $M'(t)=\lambda e^tM(t)$, so $E[X]=\lambda$; $M''(t)=(\lambda e^t)^2M(t)+\lambda e^tM(t)$, so $E[X^2]=\lambda^2+\lambda$ and $\mathrm{Var}(X)=\lambda$.

**Distribution of $X+Y$.** For independent $X\sim\text{Pois}(\lambda_1)$ and $Y\sim\text{Pois}(\lambda_2)$,

$$M_{X+Y}(t)=M_X(t)\,M_Y(t)=e^{\lambda_1(e^t-1)}e^{\lambda_2(e^t-1)}=e^{(\lambda_1+\lambda_2)(e^t-1)}$$

the MGF of $\text{Pois}(\lambda_1+\lambda_2)$. Since the MGF determines the distribution,

$$X+Y\sim\text{Pois}(\lambda_1+\lambda_2)$$
