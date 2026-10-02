---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Use $D_n=nD_{n-1}+(-1)^n$ and $D_n=(n-1)(D_{n-1}+D_{n-2})$: for even $n$, $D_n=nD_{n-1}+1$ is odd; for odd $n$, $n-1$ is even so $D_n=(n-1)(D_{n-1}+D_{n-2})$ is even. Hence $D_n$ is even iff $n$ is odd.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (derangements)']
---
Recall $D_0=1$, $D_1=0$, and for $n\ge1$

$$D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$$

**Two recurrences.**

1. Splitting off the last term of the sum: $D_n=n\cdot(n-1)!\sum_{k=0}^{n-1}\frac{(-1)^k}{k!}+n!\frac{(-1)^n}{n!}$, i.e.

$$D_n=nD_{n-1}+(-1)^n\qquad(n\ge1)$$

2. Using it twice: $D_n-nD_{n-1}=(-1)^n=-\big(D_{n-1}-(n-1)D_{n-2}\big)$, which rearranges to

$$D_n=(n-1)\big(D_{n-1}+D_{n-2}\big)\qquad(n\ge2)$$

**If $n$ is odd, $D_n$ is even.** For $n=1$, $D_1=0$ is even. For odd $n\ge3$, $n-1$ is even, so $D_n=(n-1)(D_{n-1}+D_{n-2})$ is even.

**If $n$ is even, $D_n$ is odd.** For even $n\ge2$, the first recurrence gives $D_n=nD_{n-1}+1$; $nD_{n-1}$ is even, so $D_n$ is odd. (Also $D_0=1$ is odd.)

The two cases together show that $D_n$ is even **if and only if** $n$ is odd. (Check: $D_1,\dots,D_6=0,1,2,9,44,265$.)
