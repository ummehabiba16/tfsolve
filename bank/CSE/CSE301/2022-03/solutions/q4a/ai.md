---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Given $N(1)=3$, the arrival times are i.i.d. uniform on the hour, so the number in the first 20 minutes is $\text{Bin}(3,\frac13)$: $P=\binom32(\frac13)^2\frac23=\frac29\approx0.222$ (independent of $\lambda$).'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (conditional distribution of the arrival times)']
---
Measure time in hours and let $N(t)$ be the number of arrivals by time $t$. We want $P\{N(\tfrac13)=2\mid N(1)=3\}$.

$$P\{N(\tfrac13)=2\mid N(1)=3\}=\frac{P\{N(\tfrac13)=2,\ N(1)-N(\tfrac13)=1\}}{P\{N(1)=3\}}$$

The two increments are independent, Poisson with means $\frac\lambda3$ and $\frac{2\lambda}{3}$:

$$=\frac{e^{-\lambda/3}\frac{(\lambda/3)^2}{2!}\cdot e^{-2\lambda/3}\frac{2\lambda}{3}}{e^{-\lambda}\frac{\lambda^3}{3!}}=\frac{3!}{2!\,1!}\left(\frac13\right)^2\left(\frac23\right)=3\cdot\frac19\cdot\frac23=\frac29$$

**Answer:** $\mathbf{2/9\approx0.222}$, whatever the rate $\lambda$.

(Equivalently: given $N(1)=3$, the three arrival times are independent and uniform on $(0,1)$, so the number in the first $\frac13$ hour is $\text{Bin}(3,\frac13)$.)
