---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Condition on the order of doors (each unused door equally likely): $E[T]=\frac13\big[0+(2+\frac12\cdot0+\frac12\cdot3)+(3+\frac12\cdot0+\frac12\cdot2)\big]=\frac13(0+3.5+4)=2.5$ days.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning: the trapped miner)']
---
Let $T$ be the number of days until the prisoner is free. He never reuses a door, so condition on the order in which he tries the doors.

- First door 3 (probability $\frac13$): $T=0$.
- First door 1 (probability $\frac13$): 2 days, then doors 2 and 3 are equally likely. Door 3 gives $T=2$; door 2 costs 3 more days, after which only door 3 is left, so $T=5$. Hence $E[T\mid\text{door 1 first}]=2+\frac12\cdot0+\frac12\cdot3=3.5$.
- First door 2 (probability $\frac13$): 3 days, then doors 1 and 3 are equally likely. Door 3 gives $T=3$; door 1 gives $T=3+2=5$. Hence $E[T\mid\text{door 2 first}]=3+\frac12\cdot0+\frac12\cdot2=4$.

$$E[T]=\frac13\,(0+3.5+4)=\frac{7.5}{3}=\mathbf{2.5\ days}$$

(Compare: if he chose each door with probability $\frac13$ every time, forgetting the past, $E[T]=\frac13(2+E[T])+\frac13(3+E[T])$ would give $E[T]=5$ days. Remembering the doors halves the expected time.)
