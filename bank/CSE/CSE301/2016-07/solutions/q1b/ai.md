---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Renumbering the skipped people gives $J_q(n)=qn+1-D$, where $D$ is the first term exceeding $(q-1)n$ of $D_0=1$, $D_k=\lceil\frac{q}{q-1}D_{k-1}\rceil$. For $q=8$, $n=1000$: first $D>7000$ is $7816$, so $J_8(1000)=8001-7816=185$ (for every 9th person, $J_9(1000)=9001-8672=329$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 3 (floors and ceilings: the Josephus problem with every q-th person)']
---
The question says "every 9th person" but asks for $J_8(1000)$, so we derive $J_q(n)$ for a general $q$ and then give both $J_8(1000)$ and $J_9(1000)$.

**Deriving $J_q(n)$.** Number the people $1,\dots,n$ and go around the circle. Every time a person is skipped (not eliminated), give him the next new number $n+1,n+2,\dots$; every $q$-th number is eliminated. So the numbers $q,2q,3q,\dots$ are eliminated, and a person with number $m$ that is not a multiple of $q$ gets the new number

$$N=n+m-\left\lfloor\frac mq\right\rfloor$$

(among $1,\dots,m$, exactly $\lfloor m/q\rfloor$ numbers were eliminations). After $n-1$ eliminations (numbers $q,2q,\dots,(n-1)q$) the survivor holds the number $qn$.

**Going backwards.** If $N>n$ is a new number, write the old number as $m=qk+j$ ($1\le j\le q-1$); then $N-n=(q-1)k+j$, so

$$m=N-n+\left\lfloor\frac{N-n-1}{q-1}\right\rfloor$$

Start from $N=qn$ and apply this until $N\le n$; that $N$ is $J_q(n)$. Substituting $D=qn+1-N$ turns the step into $D\leftarrow D+\lceil D/(q-1)\rceil$, i.e.

$$D_0=1,\qquad D_k=\left\lceil\frac{q}{q-1}D_{k-1}\right\rceil,\qquad J_q(n)=qn+1-D_k$$

where $D_k$ is the first term with $D_k>(q-1)n$. Only $O(\log n)$ steps are needed. (Equivalently, the linear recurrence $J_q(n)=\big((J_q(n-1)+q-1)\bmod n\big)+1$, $J_q(1)=1$, gives the same values.)

**$J_8(1000)$** ($q=8$, $D_k=\lceil\frac87D_{k-1}\rceil$; we need the first term above $7\times1000=7000$):

1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 19, 22, 26, 30, 35, 40, 46, 53, 61, 70, 80, 92, 106, 122, 140, 160, 183, 210, 240, 275, 315, 360, 412, 471, 539, 616, 704, 805, 920, 1052, 1203, 1375, 1572, 1797, 2054, 2348, 2684, 3068, 3507, 4008, 4581, 5236, 5984, 6839, 7816

$$J_8(1000)=8\times1000+1-7816=\mathbf{185}$$

**$J_9(1000)$** (every 9th person; first term above $8000$ of $D_k=\lceil\frac98D_{k-1}\rceil$):

1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 15, 17, 20, 23, 26, 30, 34, 39, 44, 50, 57, 65, 74, 84, 95, 107, 121, 137, 155, 175, 197, 222, 250, 282, 318, 358, 403, 454, 511, 575, 647, 728, 819, 922, 1038, 1168, 1314, 1479, 1664, 1872, 2106, 2370, 2667, 3001, 3377, 3800, 4275, 4810, 5412, 6089, 6851, 7708, 8672

$$J_9(1000)=9\times1000+1-8672=\mathbf{329}$$

Both values were also confirmed by iterating the linear recurrence up to $n=1000$.
