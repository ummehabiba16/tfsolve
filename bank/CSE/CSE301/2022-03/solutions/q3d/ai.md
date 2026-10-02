---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(X>x)=e^{-\lambda x}$, so $P(X>s+t\mid X>t)=e^{-\lambda(s+t)}/e^{-\lambda t}=e^{-\lambda s}=P(X>s)$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 5 (exponential distribution, memoryless property)', 'Ross, Introduction to Probability Models, Ch. 5']
---
**Memoryless property.** A non-negative random variable $X$ is memoryless if

$$P(X>s+t\mid X>t)=P(X>s)\qquad\text{for all }s,t\ge0$$

**Survival function of the exponential.** If $X\sim\text{Expo}(\lambda)$ with PDF $f(x)=\lambda e^{-\lambda x}$ for $x\ge0$, then for $x\ge0$

$$P(X>x)=\int_x^\infty\lambda e^{-\lambda u}\,du=\Big[-e^{-\lambda u}\Big]_x^\infty=e^{-\lambda x}$$

**Proof.** For $s,t\ge0$ the event $\{X>s+t\}$ is contained in $\{X>t\}$, so

$$P(X>s+t\mid X>t)=\frac{P(X>s+t,\ X>t)}{P(X>t)}=\frac{P(X>s+t)}{P(X>t)}$$

$$=\frac{e^{-\lambda(s+t)}}{e^{-\lambda t}}=e^{-\lambda s}=P(X>s)$$

Hence the exponential distribution is memoryless: given that the component has already survived $t$ units, its remaining life $X-t$ is again $\text{Expo}(\lambda)$. (Conversely, the exponential is the only continuous distribution with this property, because $G(s+t)=G(s)G(t)$ for the continuous survival function $G$ forces $G(x)=e^{-\lambda x}$.)
