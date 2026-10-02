---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'First kind $\genfrac[]{0pt}{}{n}{k}$: permutations of $n$ elements with $k$ cycles, $\genfrac[]{0pt}{}{n}{k}=(n-1)\genfrac[]{0pt}{}{n-1}{k}+\genfrac[]{0pt}{}{n-1}{k-1}$. Second kind $\genfrac\{\}{0pt}{}{n}{k}$: partitions of an $n$-set into $k$ blocks, $\genfrac\{\}{0pt}{}{n}{k}=k\genfrac\{\}{0pt}{}{n-1}{k}+\genfrac\{\}{0pt}{}{n-1}{k-1}$. They convert between powers: $x^n=\sum_k\genfrac\{\}{0pt}{}{n}{k}x^{\underline k}$, $x^{\overline n}=\sum_k\genfrac[]{0pt}{}{n}{k}x^k$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Stirling numbers)']
---
**Stirling numbers of the second kind.** $\genfrac\{\}{0pt}{}{n}{k}$ is the number of ways to partition an $n$-element set into $k$ non-empty subsets. Look at element $n$:

- it is alone in a block: the other $n-1$ elements form $k-1$ blocks, $\genfrac\{\}{0pt}{}{n-1}{k-1}$ ways;
- it shares a block: partition the other $n-1$ elements into $k$ blocks ($\genfrac\{\}{0pt}{}{n-1}{k}$ ways) and put $n$ into one of the $k$ blocks ($k$ ways).

$$\genfrac\{\}{0pt}{}{n}{k}=k\genfrac\{\}{0pt}{}{n-1}{k}+\genfrac\{\}{0pt}{}{n-1}{k-1},\qquad n\ge1;\qquad\genfrac\{\}{0pt}{}{0}{0}=1,\ \genfrac\{\}{0pt}{}{0}{k}=0\ (k\ne0)$$

**Stirling numbers of the first kind.** $\genfrac[]{0pt}{}{n}{k}$ is the number of ways to arrange $n$ elements into $k$ cycles (permutations of $n$ elements with exactly $k$ cycles). Look at element $n$:

- it forms a cycle by itself: the other $n-1$ elements form $k-1$ cycles, $\genfrac[]{0pt}{}{n-1}{k-1}$ ways;
- it is inserted into a cycle of an arrangement of the other $n-1$ elements into $k$ cycles ($\genfrac[]{0pt}{}{n-1}{k}$ ways): it can be placed right after any of the $n-1$ elements, so $n-1$ ways.

$$\genfrac[]{0pt}{}{n}{k}=(n-1)\genfrac[]{0pt}{}{n-1}{k}+\genfrac[]{0pt}{}{n-1}{k-1},\qquad n\ge1;\qquad\genfrac[]{0pt}{}{0}{0}=1,\ \genfrac[]{0pt}{}{0}{k}=0\ (k\ne0)$$

**Small values** (rows $n=1,\dots,5$, columns $k=1,\dots,5$):

| $n$ | $\genfrac\{\}{0pt}{}{n}{1}$ | $\genfrac\{\}{0pt}{}{n}{2}$ | $\genfrac\{\}{0pt}{}{n}{3}$ | $\genfrac\{\}{0pt}{}{n}{4}$ | $\genfrac\{\}{0pt}{}{n}{5}$ | $\genfrac[]{0pt}{}{n}{1}$ | $\genfrac[]{0pt}{}{n}{2}$ | $\genfrac[]{0pt}{}{n}{3}$ | $\genfrac[]{0pt}{}{n}{4}$ | $\genfrac[]{0pt}{}{n}{5}$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 1 | | | | | 1 | | | | |
| 2 | 1 | 1 | | | | 1 | 1 | | | |
| 3 | 1 | 3 | 1 | | | 2 | 3 | 1 | | |
| 4 | 1 | 7 | 6 | 1 | | 6 | 11 | 6 | 1 | |
| 5 | 1 | 15 | 25 | 10 | 1 | 24 | 50 | 35 | 10 | 1 |

(For example $\genfrac\{\}{0pt}{}{4}{2}=2\cdot\genfrac\{\}{0pt}{}{3}{2}+\genfrac\{\}{0pt}{}{3}{1}=6+1=7$ and $\genfrac[]{0pt}{}{4}{2}=3\cdot\genfrac[]{0pt}{}{3}{2}+\genfrac[]{0pt}{}{3}{1}=9+2=11$. Row sums: $\sum_k\genfrac[]{0pt}{}{n}{k}=n!$.)

**Further properties.**

- Special values: $\genfrac\{\}{0pt}{}{n}{1}=\genfrac\{\}{0pt}{}{n}{n}=1$, $\genfrac\{\}{0pt}{}{n}{2}=2^{n-1}-1$, $\genfrac[]{0pt}{}{n}{1}=(n-1)!$, $\genfrac[]{0pt}{}{n}{n}=1$, $\genfrac[]{0pt}{}{n}{n-1}=\genfrac\{\}{0pt}{}{n}{n-1}=\binom n2$.
- Ordinary powers in terms of falling powers: $x^n=\sum_k\genfrac\{\}{0pt}{}{n}{k}x^{\underline k}$, e.g. $x^3=x^{\underline3}+3x^{\underline2}+x^{\underline1}$.
- Rising powers in terms of ordinary powers: $x^{\overline n}=\sum_k\genfrac[]{0pt}{}{n}{k}x^k$, e.g. $x(x+1)(x+2)=x^3+3x^2+2x$.
- Hence $\sum_k\genfrac[]{0pt}{}{n}{k}=n!$, and the number of onto functions from an $n$-set to a $k$-set is $k!\,\genfrac\{\}{0pt}{}{n}{k}$.
