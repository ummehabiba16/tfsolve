---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P\{X_1<X_2\}=\int_0^\infty e^{-\lambda_2x}\lambda_1e^{-\lambda_1x}\,dx=\frac{\lambda_1}{\lambda_1+\lambda_2}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (further properties of the exponential distribution)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 7']
---
Condition on the value of $X_1$ (or integrate over the joint density). For $x>0$, $P(X_2>x)=e^{-\lambda_2x}$, and $X_1$ has density $\lambda_1e^{-\lambda_1x}$; by independence,

$$P\{X_1<X_2\}=\int_0^\infty P\{X_2>x\}\,\lambda_1e^{-\lambda_1x}\,dx=\int_0^\infty\lambda_1e^{-(\lambda_1+\lambda_2)x}\,dx$$

$$=\frac{\lambda_1}{\lambda_1+\lambda_2}$$

So the probability that $X_1$ "wins the race" is proportional to its rate. (Similarly, $\min(X_1,X_2)\sim\text{Expo}(\lambda_1+\lambda_2)$, since $P\{\min>t\}=e^{-\lambda_1t}e^{-\lambda_2t}$.)
