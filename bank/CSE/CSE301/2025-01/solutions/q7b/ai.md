---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Repertoire method on $f(1)=\alpha$, $f(2n)=2f(n)+\beta$, $f(2n+1)=2f(n)+\gamma$: $f(n)=A(n)\alpha+B(n)\beta+C(n)\gamma$ with $A(n)=2^m$, $B(n)=2^m-1-l$, $C(n)=l$ for $n=2^m+l$, $0\le l<2^m$. With $\alpha=\beta=1$, $\gamma=2$: $f(2^m+l)=2^{m+1}+l-1=n+2^m-1$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (the repertoire method for the generalized Josephus recurrence)']
---
**Generalise.** Consider

$$f(1)=\alpha,\qquad f(2n)=2f(n)+\beta,\qquad f(2n+1)=2f(n)+\gamma\qquad(n\ge1)$$

The solution is linear in the parameters: $f(n)=A(n)\alpha+B(n)\beta+C(n)\gamma$ for some functions $A,B,C$. Write $n=2^m+l$ with $0\le l<2^m$.

**Repertoire.**

1. $\alpha=1$, $\beta=\gamma=0$: then $f(2n)=f(2n+1)=2f(n)$, so $f$ doubles with each extra binary digit: $A(2^m+l)=2^m$.
2. Try $f(n)=1$: then $1=\alpha$, $1=2+\beta$, $1=2+\gamma$, so $(\alpha,\beta,\gamma)=(1,-1,-1)$ and

$$A(n)-B(n)-C(n)=1$$

3. Try $f(n)=n$: then $1=\alpha$, $2n=2n+\beta$, $2n+1=2n+\gamma$, so $(\alpha,\beta,\gamma)=(1,0,1)$ and

$$A(n)+C(n)=n$$

Solving: $C(n)=n-2^m=l$ and $B(n)=A(n)-1-C(n)=2^m-1-l$. So

$$f(2^m+l)=2^m\alpha+(2^m-1-l)\beta+l\gamma$$

**Our recurrence: $\alpha=1$, $\beta=1$, $\gamma=2$.**

$$f(2^m+l)=2^m+(2^m-1-l)+2l=2^{m+1}+l-1\qquad(m\ge0,\ 0\le l<2^m)$$

Equivalently, $f(n)=n+2^m-1$, where $2^m$ is the largest power of 2 not exceeding $n$.

**Check.**

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| recurrence | 1 | 3 | 4 | 7 | 8 | 9 | 10 | 15 |
| $n+2^m-1$ | 1 | 3 | 4 | 7 | 8 | 9 | 10 | 15 |

(e.g. $f(6)=2f(3)+1=9$ and $f(7)=2f(3)+2=10$.)
