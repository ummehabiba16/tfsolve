---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(\text{not found in file 2})=\frac13\cdot\frac23+\frac23=\frac89$, so $P(\text{in file 2}\mid\text{not found})=\frac{(1/3)(2/3)}{8/9}=\frac14$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (Bayes'' rule)', 'Ross, Introduction to Probability Models, Ch. 1 (Bayes'' formula)']
---
Let $F_i$ be the event that the word is in file $i$, so $P(F_i)=\frac13$, and let $N$ be the event that a quick examination of file 2 does **not** find the word.

$$P(N\mid F_2)=1-p_2=\frac23,\qquad P(N\mid F_1)=P(N\mid F_3)=1$$

**Law of total probability.**

$$P(N)=\frac13\cdot\frac23+\frac13\cdot1+\frac13\cdot1=\frac29+\frac69=\frac89$$

**Bayes' rule.**

$$P(F_2\mid N)=\frac{P(N\mid F_2)P(F_2)}{P(N)}=\frac{\frac13\cdot\frac23}{\frac89}=\frac{2/9}{8/9}=\frac14$$

**Answer:** the probability that the word is in file 2 is $\mathbf{1/4}$, down from the prior $\frac13$ because the search failed. (Only $p_2$ matters here, since only file 2 was examined.)
