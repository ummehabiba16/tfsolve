---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Bayes: $P(\text{original green}\mid\text{green drawn})=\frac{1\cdot\frac12}{1\cdot\frac12+\frac12\cdot\frac12}=\frac23$, so the remaining marble is green with probability $2/3$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (Bayes'' rule, law of total probability)']
---
Let $G$ be the event that the original marble is green, so $P(G)=P(G^c)=\frac12$. After the green marble is added, the bag contains

- green and green, if $G$ occurred;
- blue and green, if $G^c$ occurred.

Let $D$ be the event that the marble taken out is green:

$$P(D\mid G)=1,\qquad P(D\mid G^c)=\frac12$$

The remaining marble is green exactly when the original marble was green: if the original was blue, the green marble was drawn and the blue one remains. By Bayes' rule,

$$P(G\mid D)=\frac{P(D\mid G)P(G)}{P(D\mid G)P(G)+P(D\mid G^c)P(G^c)}$$

$$=\frac{1\cdot\frac12}{1\cdot\frac12+\frac12\cdot\frac12}=\frac{1/2}{3/4}=\frac23$$

**Answer:** the remaining marble is green with probability $\mathbf{2/3}$.

Intuition: given the evidence, there are three equally likely ways a green marble could have been drawn: either of the two greens from the bag (green, green), or the added green from the bag (blue, green). In two of the three, the remaining marble is green. The answer is not $1/2$, because drawing a green marble is evidence for the all-green bag.
