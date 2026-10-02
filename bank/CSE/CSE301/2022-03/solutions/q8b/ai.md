---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For $K=\lfloor\sqrt[3]n\rfloor$, $K^3\le n<(K+1)^3$ and the multiples of $K$ in $[K^3,\ K^3+3K^2+3K]$ number $3K+4$. For $K=1..11$ that gives $\sum(3K+4)=242$; for $K=12$, $n\in[1728,2000]$ gives multiples $12\cdot144,\dots,12\cdot166$: 23. Total: $265$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 3 (floor/ceiling applications: counting with cube roots)']
---
Let $K=\lfloor\sqrt[3]n\rfloor$, so $K^3\le n\le(K+1)^3-1=K^3+3K^2+3K$. We count, for each $K$, the multiples of $K$ in this range, and then add.

**A full range ($1\le K\le11$, since $12^3=1728\le2000<13^3=2197$).** The multiples of $K$ from $K^3$ to $K^3+3K^2+3K$ are

$$K^3,\ K^3+K,\ \dots,\ K^3+(3K+3)K$$

that is, $3K+4$ numbers. Summing,

$$\sum_{K=1}^{11}(3K+4)=3\cdot66+44=242$$

**The last, partial range ($K=12$, $1728\le n\le2000$).** The multiples of 12 are $12\cdot144=1728$ up to $12\cdot166=1992$ (since $12\cdot167=2004>2000$): $166-144+1=23$ numbers.

**Total.**

$$242+23=\mathbf{265}$$

integers $n$ with $1\le n\le2000$ have $\lfloor\sqrt[3]n\rfloor\mid n$. (A direct computer check agrees; up to 1000 the same method gives the textbook value 172.)
