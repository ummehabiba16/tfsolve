---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) $E[T]=0.5(2+E[T])+0.3(3+E[T])+0.2\cdot0$, so $E[T]=9.5$ days. (ii) Conditioning on the order of the doors: $E[T]=\frac13(0+3.5+4)=2.5$ days.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning: the trapped miner)']
---
Let $T$ be the number of days until the prisoner reaches freedom.

**(i) Doors chosen with probabilities 0.5, 0.3, 0.2 every time.** Condition on the first door chosen. Door 1 costs 2 days and returns him to the start, door 2 costs 3 days and returns him, door 3 frees him at once. Because his later choices do not depend on the past, after a return the expected remaining time is again $E[T]$:

$$E[T]=0.5\,(2+E[T])+0.3\,(3+E[T])+0.2\,(0)$$

$$E[T](1-0.8)=1+0.9=1.9\ \Rightarrow\ E[T]=\mathbf{9.5\ days}$$

**(ii) Equally likely among the doors not yet used.** Now the past matters, so condition on the sequence of doors.

- First door 3 (probability $\frac13$): $T=0$.
- First door 1 (probability $\frac13$): 2 days, then doors 2 and 3 are equally likely. Door 3 frees him ($T=2$); door 2 costs 3 more days, after which only door 3 is left ($T=5$). So $E[T\mid\text{door 1 first}]=2+\frac12\cdot0+\frac12\cdot3=3.5$.
- First door 2 (probability $\frac13$): 3 days, then doors 1 and 3 are equally likely. Door 3 gives $T=3$; door 1 gives $T=3+2=5$. So $E[T\mid\text{door 2 first}]=3+\frac12\cdot0+\frac12\cdot2=4$.

$$E[T]=\frac13\,(0+3.5+4)=\frac{7.5}{3}=\mathbf{2.5\ days}$$
