---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$M_Z(t)=e^{t^2/2}$ by completing the square, so for $X=\mu+\sigma Z$: $M_X(t)=e^{\mu t+\sigma^2t^2/2}$; $M_X^{\prime}(0)=\mu$, $M_X^{\prime\prime}(0)=\mu^2+\sigma^2$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 6 (MGF of the normal distribution)', 'Ross, Introduction to Probability Models, Ch. 2 (moment generating functions)']
---
**Standard normal.** For $Z\sim N(0,1)$, complete the square in the exponent ($tz-\frac{z^2}{2}=\frac{t^2}{2}-\frac{(z-t)^2}{2}$):

$$M_Z(t)=\int_{-\infty}^{\infty}e^{tz}\frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz=e^{t^2/2}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-(z-t)^2/2}\,dz=e^{t^2/2}$$

because the last integrand is the $N(t,1)$ density, which integrates to 1.

**General normal.** If $X\sim N(\mu,\sigma^2)$, then $X=\mu+\sigma Z$, so

$$M_X(t)=E\big[e^{t(\mu+\sigma Z)}\big]=e^{\mu t}M_Z(\sigma t)=e^{\mu t+\sigma^2t^2/2},\qquad-\infty<t<\infty$$

**First two moments.**

$$M_X'(t)=(\mu+\sigma^2t)\,M_X(t)\ \Rightarrow\ E[X]=M_X'(0)=\mu$$

$$M_X''(t)=\sigma^2M_X(t)+(\mu+\sigma^2t)^2M_X(t)\ \Rightarrow\ E[X^2]=M_X''(0)=\sigma^2+\mu^2$$

Hence $\mathrm{Var}(X)=E[X^2]-(E[X])^2=\sigma^2$: the parameters $\mu$ and $\sigma^2$ are the mean and variance.
