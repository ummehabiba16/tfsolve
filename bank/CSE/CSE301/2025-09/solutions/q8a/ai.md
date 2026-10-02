---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Markov: if $X\ge0$ and $a>0$ then $P(X\ge a)\le E[X]/a$. Proof: $a\,I\{X\ge a\}\le X$; take expectations to get $aP(X\ge a)\le E[X]$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 10 (inequalities)', 'Ross, Introduction to Probability Models, Ch. 2 (limit theorems: Markov''s inequality)']
---
**Statement (Markov's inequality).** If $X$ is a non-negative random variable, then for every $a>0$

$$P(X\ge a)\le\frac{E[X]}{a}$$

**Proof.** Let $I=I\{X\ge a\}$ be the indicator of the event $X\ge a$. We claim $a\,I\le X$ always:

- if $X\ge a$, then $aI=a\le X$;
- if $X<a$, then $aI=0\le X$ (because $X\ge0$).

Taking expectations (expectation preserves inequalities) and using $E[I]=P(X\ge a)$:

$$a\,P(X\ge a)=E[aI]\le E[X]\qquad\Longrightarrow\qquad P(X\ge a)\le\frac{E[X]}{a}$$

(For a continuous $X$ with density $f$: $E[X]=\int_0^\infty xf(x)\,dx\ge\int_a^\infty xf(x)\,dx\ge a\int_a^\infty f(x)\,dx=aP(X\ge a)$.) $\blacksquare$

**Remark.** The bound uses only the mean, so it is often crude, but it is the basis of Chebyshev's inequality, $P(|X-\mu|\ge k)\le\sigma^2/k^2$ (apply Markov to $(X-\mu)^2$). Example: if the mean waiting time is 5 minutes, at most $\frac{5}{20}=25\%$ of waits can be 20 minutes or longer.
