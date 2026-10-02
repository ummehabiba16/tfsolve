---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) $H_n=\sum_{k=1}^{n}\frac1k$: $\ln n<H_n\le1+\ln n$, $H_n\approx\ln n+\gamma$, unbounded; with cards of length 2 the maximum overhang of $n$ cards is $H_n$ ($d_{k+1}=d_k+\frac1{k+1}$). (ii) Eulerian numbers count permutations by ascents: $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (harmonic numbers, the overhang problem, Eulerian numbers)']
---
**(i) Harmonic numbers.** $H_n=1+\frac12+\frac13+\cdots+\frac1n$ ($H_0=0$). Properties:

- **Growth:** comparing with $\int\frac{dx}{x}$, $\ln(n+1)<H_n\le1+\ln n$; more precisely $H_n=\ln n+\gamma+\frac{1}{2n}-\cdots$ with $\gamma\approx0.5772$.
- **Divergence:** grouping terms, $H_{2^m}\ge1+\frac m2$, so $H_n\to\infty$ (slowly).
- **Finite calculus:** $\Delta H_x=\frac{1}{x+1}$, i.e. $H_x$ is the discrete analogue of $\ln x$; for example $\sum_{0\le k<n}H_k=nH_n-n$.
- $H_n$ is never an integer for $n>1$.

**Maximum overhang.**

**Set-up.** Number the cards $1,2,\dots,n$ from the top. Each card has length 2, so its centre of gravity is 1 unit from either end. Let $d_k$ be the horizontal distance from the right edge of the top card (the extreme point of the overhang) to the centre of gravity of the top $k$ cards.

**Stability.** The top $k$ cards are stable on card $k+1$ (or on the table, for $k=n$) as long as their common centre of gravity lies over card $k+1$. For the largest overhang, place each card so that the right edge of the card below is exactly under the centre of gravity of the cards above it.

**Recurrence.** $d_1=1$ (the centre of the top card). The right edge of card $k+1$ is at distance $d_k$, so its centre is at distance $d_k+1$. The centre of gravity of the top $k+1$ cards (all of equal weight) is therefore

$$d_{k+1}=\frac{k\,d_k+(d_k+1)}{k+1}=d_k+\frac{1}{k+1}$$

Unfolding, $d_k=1+\frac12+\cdots+\frac1k=H_k$, the $k$-th harmonic number.

**Maximum overhang.** The table edge is placed under the centre of gravity of all $n$ cards, so the top card reaches beyond the table by

$$d_n=H_n=1+\frac12+\frac13+\cdots+\frac1n$$

(card $k$ from the top sticks out $d_k-d_{k-1}=\frac1k$ beyond the card below it, and the bottom card sticks out $\frac1n$ beyond the table). Since $H_n\approx\ln n+0.5772$ grows without bound, the overhang can be made as large as we like with enough cards. For example $H_4=\frac{25}{12}>2$: with only 4 cards the top card lies completely beyond the edge of the table.

**(ii) Euler (Eulerian) numbers.** $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle$ counts the permutations of $\{1,\dots,n\}$ with exactly $k$ ascents ($\pi_i<\pi_{i+1}$). Inserting $n$ into a permutation of $\{1,\dots,n-1\}$ with $j$ ascents: placing it at the front or inside an ascent keeps $j$ ascents ($j+1$ gaps); placing it at the end or inside a descent adds one ($n-1-j$ gaps). Therefore

$$\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle,\qquad \left\langle\genfrac{}{}{0pt}{}{0}{0}\right\rangle=1$$

Rows: $1$; $1,1$; $1,4,1$; $1,11,11,1$; $1,26,66,26,1$ (row sums $n!$). They are symmetric, $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=\left\langle\genfrac{}{}{0pt}{}{n}{n-1-k}\right\rangle$, and satisfy Worpitzky's identity $x^n=\sum_k\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle\binom{x+k}{n}$.
