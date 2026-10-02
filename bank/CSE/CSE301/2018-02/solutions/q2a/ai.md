---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\binom{m+n+1}{n}=\sum_{k=0}^{n}\binom{m+k}{k}$: count the $(m+1)$-subsets of $\{1,\dots,m+n+1\}$ by their largest element $m+1+k$ ($\binom{m+k}{m}$ subsets each).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (parallel summation, identity (5.9))', 'Brualdi, Introductory Combinatorics, Ch. 5']
---
**The series.**

$$\binom{m+n+1}{n}=\sum_{k=0}^{n}\binom{m+k}{k}=\binom m0+\binom{m+1}{1}+\binom{m+2}{2}+\cdots+\binom{m+n}{n}$$

**Combinatorial argument.** Choosing $n$ things from $m+n+1$ is the same as choosing the $m+1$ things that are left out, so $\binom{m+n+1}{n}=\binom{m+n+1}{m+1}$ counts the $(m+1)$-element subsets of $\{1,2,\dots,m+n+1\}$. Classify such a subset by its **largest** element, which must be one of $m+1,m+2,\dots,m+n+1$; write it as $m+1+k$ with $0\le k\le n$. The other $m$ elements are then chosen from $\{1,\dots,m+k\}$ in $\binom{m+k}{m}=\binom{m+k}{k}$ ways. The cases $k=0,\dots,n$ are disjoint and exhaustive, so

$$\binom{m+n+1}{m+1}=\sum_{k=0}^{n}\binom{m+k}{m}\quad\Longleftrightarrow\quad\binom{m+n+1}{n}=\sum_{k=0}^{n}\binom{m+k}{k}$$

**Check with Pascal's rule.** Repeatedly splitting the last term, $\binom{m+n+1}{n}=\binom{m+n}{n}+\binom{m+n}{n-1}=\binom{m+n}{n}+\binom{m+n-1}{n-1}+\binom{m+n-1}{n-2}=\cdots$, which gives the same series. Example: $m=2$, $n=3$: $\binom63=20=1+3+6+10$.
