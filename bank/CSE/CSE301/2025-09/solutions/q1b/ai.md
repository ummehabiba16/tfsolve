---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Memoryless: $P(X>s+t\mid X>t)=P(X>s)$, i.e. $G(s+t)=G(s)G(t)$ for $G(x)=P(X>x)$. The exponential distribution ($G(x)=e^{-\lambda x}$) is memoryless, and it is the only continuous one: the functional equation forces $G(x)=G(1)^x=e^{-\lambda x}$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 5 (exponential distribution and the memoryless property)', 'Ross, Introduction to Probability Models, Ch. 5 (properties of the exponential distribution)']
---
**Memoryless property.** A non-negative random variable $X$ (a waiting time or a lifetime) is *memoryless* if, for all $s,t\ge0$,

$$P(X>s+t\mid X>t)=P(X>s)$$

Having already waited $t$ units without the event happening changes nothing: the remaining waiting time has the same distribution as a fresh one ("a used item is as good as new"). Since $P(X>s+t\mid X>t)=P(X>s+t)/P(X>t)$, the property is a condition on the survival function $G(x)=P(X>x)$:

$$G(s+t)=G(s)\,G(t)\quad\text{for all }s,t\ge0$$

**The exponential distribution is memoryless.** If $X\sim\text{Expo}(\lambda)$, then $G(x)=\int_x^\infty\lambda e^{-\lambda u}\,du=e^{-\lambda x}$, so

$$P(X>s+t\mid X>t)=\frac{e^{-\lambda(s+t)}}{e^{-\lambda t}}=e^{-\lambda s}=P(X>s)$$

**It is the only memoryless continuous distribution.** Let $X$ be a positive continuous random variable with $G(s+t)=G(s)G(t)$.

- Applying the property repeatedly: $G(2t)=G(t)^2$ and, in general, $G(mt)=G(t)^m$ for every positive integer $m$.
- With $t=1/n$: $G(1)=G(1/n)^n$, so $G(1/n)=G(1)^{1/n}$ and therefore $G(m/n)=G(1)^{m/n}$ for every positive rational $m/n$.
- $G$ is continuous (because $X$ is continuous) and the rationals are dense, so $G(x)=G(1)^x$ for all real $x\ge0$.
- $0<G(1)<1$ for a genuine positive random variable, so put $\lambda=-\ln G(1)>0$. Then $G(x)=e^{-\lambda x}$, the survival function of $\text{Expo}(\lambda)$.

So a continuous distribution is memoryless **if and only if it is exponential**. (Among distributions on $\{0,1,2,\dots\}$ the geometric distribution plays the same role.)

**Other continuous distributions are not memoryless.** For example, for $X\sim\text{Unif}(0,1)$:

$$P(X>0.5\mid X>0.25)=\frac{0.5}{0.75}=\frac23\ne P(X>0.25)=0.75$$

This is why the time to the next event of a Poisson process, the lifetime of a component with a constant failure rate, and the service times of an M/M/1 queue are modelled as exponential.
