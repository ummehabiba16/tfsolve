---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With $D_0=1$, $D_n=\lceil\frac54D_{n-1}\rceil$, the first $D>4\cdot10000$ is $49355$, so $J_5(10000)=5\cdot10000+1-49355=646$ (the recurrence $J_5(n)=((J_5(n-1)+4)\bmod n)+1$ gives the same).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 3 (floors and ceilings: the Josephus problem with every q-th person)']
---
Here every 5th man is eliminated ($q=5$) among $n=10{,}000$.

**Method (Concrete Mathematics, Ch. 3).** For every $q$-th person,

$$J_q(n)=qn+1-D_k$$

where $D_k$ is the smallest term greater than $(q-1)n$ of the sequence

$$D_0=1,\qquad D_n=\left\lceil\frac{q}{q-1}D_{n-1}\right\rceil$$

Only about $\log_{q/(q-1)}n$ terms are needed. (Check $q=2$: $D_n=2^n$ and $J(n)=2n+1-2^{m+1}$ for $2^m\le n<2^{m+1}$, the familiar answer.)

**Computation for $q=5$.** $D_n=\lceil\frac54D_{n-1}\rceil$:

1, 2, 3, 4, 5, 7, 9, 12, 15, 19, 24, 30, 38, 48, 60, 75, 94, 118, 148, 185, 232, 290, 363, 454, 568, 710, 888, 1110, 1388, 1735, 2169, 2712, 3390, 4238, 5298, 6623, 8279, 10349, 12937, 16172, 20215, 25269, 31587, 39484, 49355

We need the first term greater than $(q-1)n=4\times10{,}000=40{,}000$. Since $D_{43}=39{,}484\le40{,}000<D_{44}=49{,}355$,

$$J_5(10{,}000)=5\times10{,}000+1-49{,}355=\mathbf{646}$$

**Check with the direct recurrence.** $J_5(1)=1$ and $J_5(n)=\big((J_5(n-1)+4)\bmod n\big)+1$; iterating it up to $n=10{,}000$ (a short program) also gives $J_5(10{,}000)=646$.
