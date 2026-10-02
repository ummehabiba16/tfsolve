---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Summation by parts (with $\Delta(-1)^x=-2(-1)^x$) gives $\sum_{0\le k\le n}(-1)^kk^{\underline2}=\frac{(-1)^n(2n^2-1)+1}{4}$, so $\sum_{k=0}^{n}(-1)^{n-k}k(k-1)=\frac{2n^2-1+(-1)^n}{4}=\left\lfloor\frac{n^2}{2}\right\rfloor$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (finite calculus, summation by parts)']
---
Let $S_n=\sum_{k=0}^{n}(-1)^{n-k}k(k-1)=(-1)^n\sum_{k=0}^{n}(-1)^kk^{\underline2}$, where $k^{\underline2}=k(k-1)$.

**Method 1: pairing terms.** Consecutive terms combine nicely: $k(k-1)-(k-1)(k-2)=2(k-1)$.

- $n$ even: $S_n=\big[n(n-1)-(n-1)(n-2)\big]+\big[(n-2)(n-3)-(n-3)(n-4)\big]+\cdots+\big[2\cdot1-1\cdot0\big]+0$

$$=2(n-1)+2(n-3)+\cdots+2\cdot1=2\left(\frac n2\right)^2=\frac{n^2}{2}$$

- $n$ odd: the pairs run down to $\big[3\cdot2-2\cdot1\big]$, followed by $1\cdot0-0=0$:

$$S_n=2(n-1)+2(n-3)+\cdots+2\cdot2=2\cdot\frac{n-1}{2}\cdot\frac{n+1}{2}=\frac{n^2-1}{2}$$

**Method 2: summation by parts.** Use $\Delta(-1)^x=(-1)^{x+1}-(-1)^x=-2(-1)^x$, so $\sum(-1)^x\delta x=\frac{(-1)^{x+1}}{2}$.

With $u=x^{\underline2}$, $\Delta v=(-1)^x$: $v=\frac{(-1)^{x+1}}{2}$, $Ev=\frac{(-1)^{x}}{2}$, $\Delta u=2x$:

$$\sum(-1)^xx^{\underline2}\,\delta x=\frac{(-1)^{x+1}x^{\underline2}}{2}-\sum(-1)^xx\,\delta x$$

and in the same way $\sum(-1)^xx\,\delta x=\frac{(-1)^{x+1}x}{2}-\sum\frac{(-1)^x}{2}\delta x=\frac{(-1)^{x+1}(2x-1)}{4}$. Hence

$$\sum(-1)^xx^{\underline2}\,\delta x=\frac{(-1)^{x+1}\big(2x(x-1)-(2x-1)\big)}{4}=\frac{(-1)^{x+1}(2x^2-4x+1)}{4}$$

Evaluating from $0$ to $n+1$:

$$\sum_{0\le k\le n}(-1)^kk^{\underline2}=\frac{(-1)^n(2n^2-1)}{4}+\frac14$$

$$S_n=(-1)^n\sum_{0\le k\le n}(-1)^kk^{\underline2}=\frac{2n^2-1+(-1)^n}{4}$$

which is $\frac{n^2}{2}$ for even $n$ and $\frac{n^2-1}{2}$ for odd $n$, i.e.

$$\sum_{k=0}^{n}(-1)^{n-k}k(k-1)=\left\lfloor\frac{n^2}{2}\right\rfloor$$

**Check.** $n=3$: $6-2+0-0=4$; $n=4$: $12-6+2-0+0=8$; $n=5$: $20-12+6-2+0=12$.
