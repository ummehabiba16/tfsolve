---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$J(2^m+l)=2l+1$ is odd, so $n$ is even and $2l+1=\frac{2^m+l}{2}$, i.e. $l=\frac{2^m-2}{3}$, an integer exactly for odd $m$. Hence $n=2^m+\frac{2^m-2}{3}=\frac{2^{m+2}-2}{3}$ ($m$ odd): $n=2,10,42,170,682,\dots$'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (the Josephus problem)', 'Supplementary materials attached to the paper (recurrent problems, item 3)']
---
**Closed form.** For $n=2^m+l$ with $m\ge0$ and $0\le l<2^m$ (supplementary materials),

$$J(2^m+l)=2l+1$$

**Solve $J(n)=\frac n2$.** $J(n)$ is odd and must equal $\frac n2$, so $n$ is even and

$$2l+1=\frac{2^m+l}{2}\iff4l+2=2^m+l\iff l=\frac{2^m-2}{3}$$

**When is this allowed?** We need $l$ to be an integer with $0\le l<2^m$.

- $l<2^m$ always holds, since $\frac{2^m-2}{3}<2^m$, and $l\ge0$ needs $m\ge1$.
- $l$ is an integer iff $3\mid2^m-2$, i.e. $2^m\equiv2\pmod3$. Since $2\equiv-1\pmod3$, $2^m\equiv(-1)^m$, so this happens exactly when $m$ is **odd**.

**All solutions.** For odd $m$,

$$n=2^m+\frac{2^m-2}{3}=\frac{4\cdot2^m-2}{3}=\frac{2^{m+2}-2}{3}$$

| $m$ | $l=\frac{2^m-2}{3}$ | $n$ | $J(n)$ |
|:-:|:-:|:-:|:-:|
| 1 | 0 | 2 | 1 |
| 3 | 2 | 10 | 5 |
| 5 | 10 | 42 | 21 |
| 7 | 42 | 170 | 85 |
| 9 | 170 | 682 | 341 |

So $J(n)=\frac n2$ exactly for $n=2,10,42,170,682,\dots$, i.e. $n=\frac{2^{2k+3}-2}{3}=\frac{2\left(4^{k+1}-1\right)}{3}$ for $k=0,1,2,\dots$ (A direct check of all $n<2000$ finds exactly 2, 10, 42, 170, 682.)

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
