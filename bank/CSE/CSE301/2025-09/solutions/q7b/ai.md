---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'By the CLT $\bar X\approx N(167,\ (27/6)^2)=N(167,\ 4.5^2)$: $P(163<\bar X<170)\approx\Phi(0.67)-\Phi(-0.89)=0.7486-0.1867\approx0.562$ (exact $z$-values give $0.5605$).'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 10 (central limit theorem)', 'Wasserman, All of Statistics, Ch. 5']
---
Let $X_1,\dots,X_{36}$ be the weights of the sampled workers, with mean $\mu=167$ and standard deviation $\sigma=27$, and let $\bar X$ be their sample mean.

**Distribution of $\bar X$.** $E[\bar X]=\mu=167$ and $\mathrm{SD}(\bar X)=\frac{\sigma}{\sqrt n}=\frac{27}{\sqrt{36}}=\frac{27}{6}=4.5$. By the central limit theorem ($n=36$ is reasonably large),

$$\bar X\approx N(167,\ 4.5^2)$$

**Standardise.**

$$P(163<\bar X<170)\approx P\left(\frac{163-167}{4.5}<Z<\frac{170-167}{4.5}\right)=P(-0.89<Z<0.67)$$

From the standard normal table:

$$\Phi(0.67)=0.7486,\qquad\Phi(-0.89)=0.1867$$

$$P(163<\bar X<170)\approx0.7486-0.1867=\mathbf{0.562}$$

(Using the unrounded $z$-values $0.667$ and $-0.889$ gives $0.5605$.)

*Tables used: [Standard normal table, negative z (opens in a new tab)](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/standard-normal-table-negative-z.png) and [standard normal table, positive z (opens in a new tab)](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/standard-normal-table-positive-z.png).*
