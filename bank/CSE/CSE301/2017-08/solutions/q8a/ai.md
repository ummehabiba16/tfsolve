---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(X=k\mid X+Y=n)=\frac{e^{-\lambda_1}\frac{\lambda_1^k}{k!}e^{-\lambda_2}\frac{\lambda_2^{n-k}}{(n-k)!}}{e^{-(\lambda_1+\lambda_2)}\frac{(\lambda_1+\lambda_2)^n}{n!}}=\binom nk\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$, a binomial, so $E[X\mid X+Y=n]=\frac{n\lambda_1}{\lambda_1+\lambda_2}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (conditional distributions: Poisson example)']
---
$X+Y\sim\text{Pois}(\lambda_1+\lambda_2)$ (sum of independent Poissons). For $0\le k\le n$, using independence,

$$P(X=k\mid X+Y=n)=\frac{P(X=k,\ Y=n-k)}{P(X+Y=n)}=\frac{e^{-\lambda_1}\dfrac{\lambda_1^k}{k!}\cdot e^{-\lambda_2}\dfrac{\lambda_2^{n-k}}{(n-k)!}}{e^{-(\lambda_1+\lambda_2)}\dfrac{(\lambda_1+\lambda_2)^n}{n!}}$$

$$=\frac{n!}{k!\,(n-k)!}\cdot\frac{\lambda_1^k\lambda_2^{n-k}}{(\lambda_1+\lambda_2)^n}=\binom nk\left(\frac{\lambda_1}{\lambda_1+\lambda_2}\right)^k\left(\frac{\lambda_2}{\lambda_1+\lambda_2}\right)^{n-k}$$

So, given $X+Y=n$, $X$ is binomial with parameters $n$ and $\frac{\lambda_1}{\lambda_1+\lambda_2}$, and therefore

$$E[X\mid X+Y=n]=\frac{n\,\lambda_1}{\lambda_1+\lambda_2}$$

(Intuition: each of the $n$ events independently "belongs" to $X$ with probability $\frac{\lambda_1}{\lambda_1+\lambda_2}$.)
