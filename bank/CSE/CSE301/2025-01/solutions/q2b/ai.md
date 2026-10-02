---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Given the typist, $X$ is Poisson with mean $2.6$, $3$ or $3.4$ (each w.p. $1/3$). (i) $E[X]=E[E[X\mid T]]=3$. (ii) $\mathrm{Var}(X)=E[\mathrm{Var}(X\mid T)]+\mathrm{Var}(E[X\mid T])=3+0.32/3=233/75\approx3.107$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (conditional expectation and conditional variance)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 9 (Adam''s and Eve''s laws)']
---
Let $T\in\{A,B,C\}$ be the typist, each with probability $\frac13$, and let $\Lambda=E[X\mid T]$, which is $2.6$, $3$ or $3.4$. Given $T$, $X$ is Poisson, so $E[X\mid T]=\Lambda$ and $\mathrm{Var}(X\mid T)=\Lambda$.

**(i) Expected number of errors** (law of total expectation):

$$E[X]=E\big[E[X\mid T]\big]=\frac13(2.6+3+3.4)=\frac{9}{3}=3$$

**(ii) Variance** (conditional variance formula):

$$\mathrm{Var}(X)=E\big[\mathrm{Var}(X\mid T)\big]+\mathrm{Var}\big(E[X\mid T]\big)=E[\Lambda]+\mathrm{Var}(\Lambda)$$

$$E[\Lambda]=3,\qquad\mathrm{Var}(\Lambda)=\frac13\big[(2.6-3)^2+0^2+(3.4-3)^2\big]=\frac{0.32}{3}=0.1067$$

$$\mathrm{Var}(X)=3+0.1067=\frac{233}{75}\approx3.107$$

(Check via the second moment: $E[X^2\mid T]=\Lambda+\Lambda^2$, so $E[X^2]=3+\frac13(6.76+9+11.56)=12.1067$ and $\mathrm{Var}(X)=12.1067-9=3.1067$.)

The variance is a little larger than the mean, because not knowing which typist did the work adds extra variability on top of the Poisson variability.
