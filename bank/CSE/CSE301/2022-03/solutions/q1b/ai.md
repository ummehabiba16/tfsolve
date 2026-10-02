---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\mathrm{Cov}(X,X^2)=E[X^3]-E[X]E[X^2]=\frac14-\frac12\cdot\frac13=\frac1{12}>0$: positively correlated (correlation $\sqrt{15}/4\approx0.968$).'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 7 (covariance and correlation)']
---
For $X\sim\text{Unif}(0,1)$, $E[X^k]=\int_0^1x^k\,dx=\frac{1}{k+1}$, so

$$E[X]=\frac12,\qquad E[X^2]=\frac13,\qquad E[X^3]=\frac14,\qquad E[X^4]=\frac15$$

**Covariance.** With $Y=X^2$,

$$\mathrm{Cov}(X,Y)=E[XY]-E[X]E[Y]=E[X^3]-E[X]E[X^2]=\frac14-\frac12\cdot\frac13=\frac14-\frac16=\frac{1}{12}$$

**Sign.** $\mathrm{Cov}(X,Y)=\frac1{12}>0$, so $X$ and $Y$ are **positively correlated** (larger $X$ goes with larger $X^2$ on $(0,1)$).

For the strength, $\mathrm{Var}(X)=\frac13-\frac14=\frac1{12}$ and $\mathrm{Var}(Y)=E[X^4]-(E[X^2])^2=\frac15-\frac19=\frac{4}{45}$, so

$$\rho(X,Y)=\frac{1/12}{\sqrt{\frac1{12}\cdot\frac4{45}}}=\frac{\sqrt{15}}{4}\approx0.968$$

a strong but not perfect linear relationship ($Y$ is a non-linear function of $X$). Note that $X$ and $Y$ are of course dependent; a covariance of zero would not have shown independence anyway.
