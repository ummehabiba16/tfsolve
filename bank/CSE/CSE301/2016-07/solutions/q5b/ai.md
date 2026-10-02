---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(\text{fair}\mid H)=\frac{\frac12\cdot\frac12}{\frac12\cdot\frac12+\frac12\cdot1}=\frac13$. A tail is impossible with the two-headed coin, so after H then T the coin is certainly fair: probability $1$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (Bayes'' rule)', 'Ross, Introduction to Probability Models, Ch. 1 (Bayes'' formula)']
---
Let $F$ be the event that the fair coin was chosen, so $P(F)=P(F^c)=\frac12$, and let $H_1$ be "the first flip shows heads".

$$P(H_1\mid F)=\frac12,\qquad P(H_1\mid F^c)=1$$

**After one head.** By Bayes' rule,

$$P(F\mid H_1)=\frac{P(H_1\mid F)P(F)}{P(H_1\mid F)P(F)+P(H_1\mid F^c)P(F^c)}=\frac{\frac12\cdot\frac12}{\frac12\cdot\frac12+1\cdot\frac12}=\frac{1/4}{3/4}=\frac13$$

**After a head and then a tail.** Let $T_2$ be "the second flip shows tails". The two-headed coin can never show tails, so $P(T_2\mid F^c)=0$, while $P(H_1T_2\mid F)=\frac14$:

$$P(F\mid H_1T_2)=\frac{\frac14\cdot\frac12}{\frac14\cdot\frac12+0\cdot\frac12}=1$$

So after the tail the gambler knows for certain that it is the fair coin: the probability is $\mathbf1$.
