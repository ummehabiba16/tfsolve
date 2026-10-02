---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With $p=\lambda/n$, $\binom nk p^k(1-p)^{n-k}=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot(1-\frac\lambda n)^n(1-\frac\lambda n)^{-k}\to1\cdot\frac{\lambda^k}{k!}\cdot e^{-\lambda}\cdot1$ as $n\to\infty$.'
sources: ['Ross, Introduction to Probability Models, Ch. 2 (the Poisson random variable as a limit of binomials)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 4 (Poisson approximation)']
---
Let $X\sim\text{Bin}(n,p)$ and let $n\to\infty$, $p\to0$ in such a way that $np=\lambda$ stays fixed, i.e. $p=\lambda/n$. For a fixed $k\ge0$,

$$P(X=k)=\binom nk p^k(1-p)^{n-k}=\frac{n!}{k!\,(n-k)!}\left(\frac\lambda n\right)^k\left(1-\frac\lambda n\right)^{n-k}$$

Regroup the factors:

$$P(X=k)=\frac{n(n-1)\cdots(n-k+1)}{n^k}\cdot\frac{\lambda^k}{k!}\cdot\left(1-\frac\lambda n\right)^n\cdot\left(1-\frac\lambda n\right)^{-k}$$

Now take the limit of each factor as $n\to\infty$ ($k$ and $\lambda$ fixed):

- $\dfrac{n(n-1)\cdots(n-k+1)}{n^k}=1\cdot\left(1-\frac1n\right)\cdots\left(1-\frac{k-1}{n}\right)\to1$ (a fixed number $k$ of factors, each tending to 1);
- $\left(1-\dfrac\lambda n\right)^n\to e^{-\lambda}$;
- $\left(1-\dfrac\lambda n\right)^{-k}\to1$.

Therefore

$$\lim_{n\to\infty}P(X=k)=e^{-\lambda}\frac{\lambda^k}{k!},\qquad k=0,1,2,\dots$$

which is the Poisson($\lambda$) PMF with $\lambda=np$. So for large $n$ and small $p$, $\text{Bin}(n,p)\approx\text{Pois}(np)$. The moments agree as well: the binomial mean is $np=\lambda$ and its variance $np(1-p)\to\lambda$, which is the Poisson variance.

(Same result with MGFs: $\big(1-p+pe^t\big)^n=\big(1+\frac{\lambda(e^t-1)}{n}\big)^n\to e^{\lambda(e^t-1)}$, the Poisson MGF.)
