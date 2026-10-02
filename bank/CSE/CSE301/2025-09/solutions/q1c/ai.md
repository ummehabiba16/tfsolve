---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\sum_{k=1}^{n}k\binom{n}{k}=n2^{n-1}$: count (committee, chair) pairs from $n$ people either by choosing a committee of size $k$ and then its chair ($k\binom{n}{k}$ ways), or the chair first and then any subset of the other $n-1$ people ($n2^{n-1}$ ways).'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 1 (story proofs)']
---
We show

$$\sum_{k=1}^{n}k\binom{n}{k}=n\,2^{n-1}$$

by counting one set of objects in two different ways.

**Story.** From a club of $n$ people we form a committee of any non-zero size and choose one committee member to be its chair. How many (committee, chair) pairs are there?

**Count 1: committee first.** Let the committee have $k$ members, $1\le k\le n$. There are $\binom{n}{k}$ ways to choose the committee and then $k$ ways to choose its chair, so there are $k\binom{n}{k}$ pairs whose committee has size $k$. Different sizes give disjoint cases, so the total is

$$\sum_{k=1}^{n}k\binom{n}{k}$$

**Count 2: chair first.** Choose the chair first: $n$ ways. Each of the other $n-1$ people is then either on the committee or not: $2^{n-1}$ ways. Each choice gives a different (committee, chair) pair and every pair arises exactly once, so the total is

$$n\,2^{n-1}$$

Both counts count the same set, so

$$\sum_{k=1}^{n}k\binom{n}{k}=n\,2^{n-1}$$

**Check ($n=3$).** $1\cdot3+2\cdot3+3\cdot1=12=3\cdot2^{2}$.

(Algebraic confirmation: differentiating $(1+x)^n=\sum_k\binom{n}{k}x^k$ gives $n(1+x)^{n-1}=\sum_k k\binom{n}{k}x^{k-1}$; put $x=1$.)
