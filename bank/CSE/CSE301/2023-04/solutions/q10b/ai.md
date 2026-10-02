---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The $n$-th plane is cut by the other $n-1$ planes in $n-1$ lines in general position, which split it into $L_{n-1}=\frac{(n-1)n}{2}+1$ pieces, each adding a region: $P_n=P_{n-1}+L_{n-1}$, $P_0=1$, so $P_n=\binom n0+\binom n1+\binom n2+\binom n3=\frac{n^3+5n+6}{6}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (regions: exercise on planes in space)', 'Supplementary materials attached to the paper (recurrent problems, item 2)']
---
**Step 1: lines in a plane.** Let $L_n$ be the maximum number of regions into which $n$ straight lines divide the plane. With no lines there is one region: $L_0=1$. When the $n$-th line is added it can cross each of the $n-1$ earlier lines at most once, and it does so in distinct points when no two lines are parallel and no three meet in a point. These $n-1$ crossing points cut the new line into $n$ pieces, and each piece splits one existing region into two, so the new line adds exactly $n$ regions (and can add no more):

$$L_0=1,\qquad L_n=L_{n-1}+n\quad(n\ge1)$$

Unfolding,

$$L_n=1+(1+2+\cdots+n)=1+\frac{n(n+1)}{2}$$

**Step 2: planes in space.** Let $P_n$ be the maximum number of regions of 3-D space cut by $n$ planes; $P_0=1$. Put the planes in general position: no two parallel, no three through a common line, no four through a common point.

When the $n$-th plane is added, it meets each of the other $n-1$ planes in a line, and these $n-1$ lines lie in the new plane in general position. So they divide the new plane into $L_{n-1}$ two-dimensional pieces. Each piece cuts one existing region of space into two, so the new plane adds exactly $L_{n-1}$ regions (and no plane can add more, since its pieces are at most $L_{n-1}$):

$$P_0=1,\qquad P_n=P_{n-1}+L_{n-1}=P_{n-1}+\frac{(n-1)n}{2}+1\quad(n\ge1)$$

**Closed form.** Unfolding,

$$P_n=1+\sum_{k=0}^{n-1}\left(1+\binom{k+1}{2}\right)=1+n+\binom{n+1}{3}$$

using $\sum_{k=0}^{n-1}\binom{k+1}{2}=\binom{n+1}{3}$. Since $\binom{n+1}{3}=\binom n3+\binom n2$,

$$P_n=\binom n0+\binom n1+\binom n2+\binom n3=\frac{n^3+5n+6}{6}$$

**Check:** $P_1=2$, $P_2=4$, $P_3=8$ (the octants), $P_4=15$, $P_5=26$.

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
