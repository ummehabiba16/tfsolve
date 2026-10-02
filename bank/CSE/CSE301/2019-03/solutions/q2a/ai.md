---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Condition on the first value: (i) $E[L_1]=p\cdot\frac{1}{1-p}+(1-p)\cdot\frac1p=\frac{p}{1-p}+\frac{1-p}{p}$; (ii) the second run is of the other value, so $E[L_2]=p\cdot\frac1p+(1-p)\cdot\frac{1}{1-p}=2$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning)']
---
Let $L_1$ and $L_2$ be the lengths of the first and second runs, and condition on the first value $X_1$.

**(i) First run.** If $X_1=1$ (probability $p$), the first run continues while further 1s appear, so $P(L_1=k\mid X_1=1)=p^{k-1}(1-p)$, a geometric distribution (counting the trial that ends the run) with mean $\frac{1}{1-p}$. Similarly, if $X_1=0$ the run continues while 0s appear, with mean $\frac1p$. Hence

$$E[L_1]=p\cdot\frac{1}{1-p}+(1-p)\cdot\frac1p=\frac{p}{1-p}+\frac{1-p}{p}$$

**(ii) Second run.** If $X_1=1$, the first run of 1s ends with a 0, and the second run is a run of 0s. Its length is geometric with "ending" probability $p$ (it ends when a 1 appears), so its mean is $\frac1p$. If $X_1=0$, the second run is a run of 1s with mean $\frac{1}{1-p}$. Hence

$$E[L_2]=p\cdot\frac1p+(1-p)\cdot\frac{1}{1-p}=2$$

whatever the value of $p$.

(Note that $E[L_1]\ge2$, with equality only for $p=\frac12$: a long first run is more likely to be of the more frequent value.)
