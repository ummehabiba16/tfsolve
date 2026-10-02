---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Condition on the first day: (i) $E[L_1]=p\cdot\frac{1}{1-p}+(1-p)\cdot\frac1p=\frac{p}{1-p}+\frac{1-p}{p}$; (ii) the second run is of the other weather, so $E[L_2]=p\cdot\frac1p+(1-p)\cdot\frac{1}{1-p}=2$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning)']
---
Let $L_1$ and $L_2$ be the lengths of the first and second runs, and condition on the weather $W_1$ of the first day. Days are independent: rainy (R) with probability $p$, sunny (S) with probability $1-p$.

**(i) First run.** Given $W_1=R$, the first run continues while further rainy days occur and ends at the first sunny day, so

$$P(L_1=k\mid W_1=R)=p^{k-1}(1-p),\qquad E[L_1\mid W_1=R]=\frac{1}{1-p}$$

(a geometric distribution with "stopping" probability $1-p$). Similarly $E[L_1\mid W_1=S]=\frac1p$. By the law of total expectation,

$$E[L_1]=p\cdot\frac{1}{1-p}+(1-p)\cdot\frac1p=\frac{p}{1-p}+\frac{1-p}{p}$$

**(ii) Second run.** If $W_1=R$, the first run ends with a sunny day, which starts the second run; this run of sunny days ends at the next rainy day, so its mean length is $\frac1p$. If $W_1=S$, the second run is rainy, with mean length $\frac{1}{1-p}$. Hence

$$E[L_2]=p\cdot\frac1p+(1-p)\cdot\frac{1}{1-p}=1+1=2$$

for every value of $p$.

(For $p=\frac12$ both answers are 2; otherwise $E[L_1]>2$, because the first run is more likely to be of the more common weather and so tends to be longer.)
