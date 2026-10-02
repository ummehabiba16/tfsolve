---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(1) Classify the $(m+1)$-subsets of $\{0,\dots,n\}$ by their largest element $k$: $\sum_{0\le k\le n}\binom km=\binom{n+1}{m+1}$. (2) Classify the $k$-subsets of $\{1,\dots,n\}$ by whether they contain $n$: $\binom{n-1}{k}+\binom{n-1}{k-1}=\binom nk$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (upper summation and the addition formula)', 'Brualdi, Introductory Combinatorics, Ch. 5']
---
**(1) Upper summation:** $\sum_{0\le k\le n}\binom km=\binom{n+1}{m+1}$.

The right side counts the $(m+1)$-element subsets of the $(n+1)$-element set $\{0,1,\dots,n\}$. Classify each subset by its **largest** element $k$. The other $m$ elements are chosen from the $k$ smaller numbers $\{0,\dots,k-1\}$, in $\binom km$ ways. Every subset falls into exactly one class ($m\le k\le n$; classes with $k<m$ are empty), so

$$\sum_{0\le k\le n}\binom km=\binom{n+1}{m+1}$$

Example: $m=1$, $n=4$: $0+1+2+3+4=10=\binom52$.

**(2) Pascal's addition formula:** $\binom{n-1}{k}+\binom{n-1}{k-1}=\binom nk$.

The right side counts the $k$-element subsets of $\{1,2,\dots,n\}$. Split them by whether they contain the element $n$:

- subsets **not** containing $n$: all $k$ elements come from $\{1,\dots,n-1\}$: $\binom{n-1}{k}$ ways;
- subsets containing $n$: the other $k-1$ elements come from $\{1,\dots,n-1\}$: $\binom{n-1}{k-1}$ ways.

The two cases are disjoint and exhaustive, so $\binom nk=\binom{n-1}{k}+\binom{n-1}{k-1}$. Example: $\binom42=6=\binom32+\binom31=3+3$.
