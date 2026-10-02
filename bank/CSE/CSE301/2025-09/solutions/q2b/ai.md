---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With indicators of empty boxes and linearity: $E[\#\text{empty boxes}]=n(1-1/n)^k=(n-1)^k/n^{k-1}$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 4 (indicator random variables, linearity of expectation)']
---
Number the boxes $1,\dots,n$ and let $I_j$ be the indicator that box $j$ is empty. The number of empty boxes is

$$X=I_1+I_2+\cdots+I_n$$

All $n^k$ placements are equally likely, which is the same as each ball independently landing in each box with probability $1/n$. Box $j$ is empty exactly when each of the $k$ balls misses it:

$$E[I_j]=P(\text{box }j\text{ empty})=\left(1-\frac1n\right)^k=\frac{(n-1)^k}{n^k}$$

By linearity of expectation (which needs no independence; the $I_j$ are in fact dependent),

$$E[X]=\sum_{j=1}^{n}E[I_j]=n\left(1-\frac1n\right)^k=\frac{(n-1)^k}{n^{k-1}}$$

**Check.** $n=2$, $k=1$: one ball leaves exactly one box empty, and the formula gives $2\cdot\frac12=1$. For large $n$ the expected fraction of empty boxes is about $e^{-k/n}$.
