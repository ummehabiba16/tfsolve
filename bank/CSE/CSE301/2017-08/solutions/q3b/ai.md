---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Second kind: $\genfrac\{\}{0pt}{}{n}{k}=k\genfrac\{\}{0pt}{}{n-1}{k}+\genfrac\{\}{0pt}{}{n-1}{k-1}$ (element $n$ alone or added to one of $k$ blocks). First kind: $\genfrac[]{0pt}{}{n}{k}=(n-1)\genfrac[]{0pt}{}{n-1}{k}+\genfrac[]{0pt}{}{n-1}{k-1}$ (element $n$ in its own cycle or inserted after one of $n-1$ elements).'
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
