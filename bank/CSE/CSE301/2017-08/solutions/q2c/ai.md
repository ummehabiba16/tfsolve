---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\sum_{0\le k\le n}\binom km=\binom{n+1}{m+1}$: classify the $(m+1)$-subsets of $\{0,1,\dots,n\}$ by their largest element $k$; there are $\binom km$ ways to choose the other $m$ elements from $\{0,\dots,k-1\}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (upper summation, identity (5.10))', 'Brualdi, Introductory Combinatorics, Ch. 5']
---
**Claim (upper summation).**

$$\sum_{0\le k\le n}\binom km=\binom{n+1}{m+1}\qquad(m,n\ge0)$$

**Combinatorial argument.** The right side counts the $(m+1)$-element subsets of $\{0,1,2,\dots,n\}$, a set with $n+1$ elements. Classify each such subset by its **largest** element $k$ ($m\le k\le n$). The remaining $m$ elements must be chosen from $\{0,1,\dots,k-1\}$, which has $k$ elements, in $\binom km$ ways. Different values of $k$ give disjoint classes that together contain every subset, so

$$\binom{n+1}{m+1}=\sum_{k=m}^{n}\binom km=\sum_{0\le k\le n}\binom km$$

(the terms with $k<m$ are zero).

**Example.** $m=1$: $\sum_{k\le n}k=\binom{n+1}{2}=\frac{n(n+1)}{2}$. $m=2$, $n=4$: $0+0+1+3+6=10=\binom53$.
