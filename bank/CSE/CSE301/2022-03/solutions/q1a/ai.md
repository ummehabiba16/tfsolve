---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Bayes: $P(\text{original red}\mid\text{red drawn})=\frac{1\cdot\frac12}{1\cdot\frac12+\frac12\cdot\frac12}=\frac23$, so the other pill is red with probability $2/3$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (Bayes'' rule, law of total probability)']
---
Let $R$ be the event that the original pill is red, so $P(R)=P(R^c)=\frac12$. After the second red pill is added, the palm holds

- red and red, if $R$ occurred;
- blue and red, if $R^c$ occurred.

Let $D$ be the event that the pill taken out is red:

$$P(D\mid R)=1,\qquad P(D\mid R^c)=\frac12$$

The other pill is red exactly when the original pill was red. By Bayes' rule,

$$P(R\mid D)=\frac{P(D\mid R)P(R)}{P(D\mid R)P(R)+P(D\mid R^c)P(R^c)}=\frac{1\cdot\frac12}{1\cdot\frac12+\frac12\cdot\frac12}=\frac{1/2}{3/4}=\frac23$$

**Answer:** the other pill is also red with probability $\mathbf{2/3}$ (not $\frac12$: drawing a red pill is evidence for the red-red case).
