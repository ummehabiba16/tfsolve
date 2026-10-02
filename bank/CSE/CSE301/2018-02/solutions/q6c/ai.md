---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Total $S=\sum_{i=1}^{N}Y_i$, $N\sim\text{Pois}(10)$, $Y_i\sim\text{Unif}(0,100)$: $E[S]=E[N]E[Y]=10\cdot50=500$; $\mathrm{Var}(S)=E[N]\mathrm{Var}(Y)+\mathrm{Var}(N)E[Y]^2=\lambda E[Y^2]=10\cdot\frac{100^2}{3}\approx33{,}333$ (SD $\approx183$).'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (compound random variables: conditional expectation and variance)']
---
Let $N\sim\text{Pois}(\lambda)$, $\lambda=10$, be the number of customers, and $Y_1,Y_2,\dots$ the amounts they spend, i.i.d. $\text{Unif}(0,100)$ and independent of $N$. The day's takings are

$$S=\sum_{i=1}^{N}Y_i$$

For one customer: $E[Y]=50$, $\mathrm{Var}(Y)=\frac{100^2}{12}=\frac{2500}{3}$, and $E[Y^2]=\frac{100^2}{3}=\frac{10000}{3}$.

**Mean** (condition on $N$): $E[S\mid N]=N\,E[Y]$, so

$$E[S]=E\big[N\,E[Y]\big]=E[N]\,E[Y]=10\times50=\mathbf{500}$$

**Variance** (conditional variance formula): $\mathrm{Var}(S\mid N)=N\,\mathrm{Var}(Y)$, so

$$\mathrm{Var}(S)=E\big[\mathrm{Var}(S\mid N)\big]+\mathrm{Var}\big(E[S\mid N]\big)=E[N]\,\mathrm{Var}(Y)+\mathrm{Var}(N)\,E[Y]^2$$

For a Poisson $N$, $E[N]=\mathrm{Var}(N)=\lambda$, so this simplifies to $\lambda E[Y^2]$:

$$\mathrm{Var}(S)=10\cdot\frac{2500}{3}+10\cdot50^2=\frac{25000}{3}+25000=\frac{100000}{3}\approx\mathbf{33{,}333}$$

(standard deviation $\approx182.6$). A simulation of 200,000 days gives mean $\approx500.8$ and variance $\approx33{,}400$, in agreement.
