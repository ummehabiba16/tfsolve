---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$M_X(t)=e^{\lambda(e^t-1)}$ for $X\sim\text{Pois}(\lambda)$; for independent $X,Y$, $M_{X+Y}=M_XM_Y=e^{(\lambda_1+\lambda_2)(e^t-1)}$, so $X+Y\sim\text{Pois}(\lambda_1+\lambda_2)$ by the uniqueness of MGFs.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 6 (MGFs, sums of independent random variables)', 'Ross, Introduction to Probability Models, Ch. 2 (moment generating functions)']
---
**MGF of a Poisson random variable.** If $X\sim\text{Pois}(\lambda)$,

$$M_X(t)=E[e^{tX}]=\sum_{k=0}^{\infty}e^{tk}\,\frac{e^{-\lambda}\lambda^k}{k!}=e^{-\lambda}\sum_{k=0}^{\infty}\frac{(\lambda e^t)^k}{k!}$$

$$=e^{-\lambda}e^{\lambda e^t}=e^{\lambda(e^t-1)},\qquad -\infty<t<\infty$$

**Sum of two independent Poissons.** Let $X\sim\text{Pois}(\lambda_1)$ and $Y\sim\text{Pois}(\lambda_2)$ be independent. Then $e^{tX}$ and $e^{tY}$ are independent, so the MGF of the sum is the product of the MGFs:

$$M_{X+Y}(t)=E[e^{tX}e^{tY}]=E[e^{tX}]\,E[e^{tY}]=M_X(t)M_Y(t)$$

$$=e^{\lambda_1(e^t-1)}\,e^{\lambda_2(e^t-1)}=e^{(\lambda_1+\lambda_2)(e^t-1)}$$

This is the MGF of a Poisson distribution with parameter $\lambda_1+\lambda_2$. An MGF that is finite in an interval around 0 determines the distribution uniquely, so

$$X+Y\sim\text{Pois}(\lambda_1+\lambda_2)$$

(Check: $M'_{X+Y}(0)=\lambda_1+\lambda_2=E[X]+E[Y]$.)
