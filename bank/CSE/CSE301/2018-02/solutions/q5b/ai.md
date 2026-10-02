---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(X=5)=\frac25$, $P(X=-3)=\frac35$, so $M(t)=\frac25e^{5t}+\frac35e^{-3t}$; $E[X]=M^{\prime}(0)=1/5$, $E[X^2]=M^{\prime\prime}(0)=77/5$, $\mathrm{Var}(X)=384/25=15.36$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 6 (moment generating functions)', 'Ross, Introduction to Probability Models, Ch. 2 (moment generating functions)']
---
**Distribution of $X$.** There are $\binom52=10$ equally likely pairs of chips. The sum is even when both chips are odd (from $\{1,3,5\}$: $\binom32=3$ pairs) or both are even (from $\{2,4\}$: $\binom22=1$ pair):

$$P(X=5)=P(\text{sum even})=\frac{3+1}{10}=\frac25,\qquad P(X=-3)=\frac{6}{10}=\frac35$$

**(i) Moment-generating function.**

$$M(t)=E[e^{tX}]=\frac25e^{5t}+\frac35e^{-3t}$$

**(ii) First and second moments** from the derivatives at $t=0$:

$$M'(t)=2e^{5t}-\frac95e^{-3t},\qquad E[X]=M'(0)=2-\frac95=\frac15$$

$$M''(t)=10e^{5t}+\frac{27}{5}e^{-3t},\qquad E[X^2]=M''(0)=10+\frac{27}{5}=\frac{77}{5}$$

**(iii) Expected value and variance** (the paper prints "variable"; the variance is meant).

$$E[X]=\frac15=0.2$$

$$\mathrm{Var}(X)=E[X^2]-(E[X])^2=\frac{77}{5}-\frac{1}{25}=\frac{384}{25}=15.36$$

(Check directly: $E[X]=5\cdot\frac25-3\cdot\frac35=\frac15$ and $E[X^2]=25\cdot\frac25+9\cdot\frac35=\frac{77}{5}$.)
