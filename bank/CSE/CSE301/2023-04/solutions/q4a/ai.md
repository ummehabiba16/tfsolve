---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\sum_yE[X\mid Y=y]P(Y=y)=\sum_y\sum_xx\,P(X=x\mid Y=y)P(Y=y)=\sum_x x\sum_yP(X=x,Y=y)=\sum_xxP(X=x)=E[X]$, i.e. $E[X]=E\big[E[X\mid Y]\big]$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 9 (Adam''s law)']
---
**Statement.** For discrete random variables $X$ and $Y$ (with $E|X|<\infty$),

$$E[X]=E\big[E[X\mid Y]\big]=\sum_yE[X\mid Y=y]\,P(Y=y)$$

where $E[X\mid Y=y]=\sum_xx\,P(X=x\mid Y=y)$.

**Proof.**

$$\sum_yE[X\mid Y=y]\,P(Y=y)=\sum_y\sum_xx\,P(X=x\mid Y=y)\,P(Y=y)$$

$$=\sum_y\sum_xx\,P(X=x,\ Y=y)\qquad\text{(definition of conditional probability)}$$

$$=\sum_xx\sum_yP(X=x,\ Y=y)\qquad\text{(swap the order of summation)}$$

$$=\sum_xx\,P(X=x)=E[X]\qquad\text{(marginal of }X\text{)}$$

Swapping the order is allowed because the double series converges absolutely ($\sum_x|x|P(X=x)=E|X|<\infty$).
