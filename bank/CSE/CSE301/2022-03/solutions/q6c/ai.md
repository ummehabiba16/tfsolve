---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Insert $n$ into a permutation of $n-1$ with $j$ ascents: the front and the $j$ ascent gaps keep $j$ ascents ($j+1$ gaps); the end and the $n-2-j$ descent gaps add one ($n-1-j$ gaps). Hence $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Eulerian numbers, equation (6.35))']
---
**Definition.** The Eulerian number $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle$ is the number of permutations $\pi_1\pi_2\dots\pi_n$ of $\{1,2,\dots,n\}$ with exactly $k$ **ascents**, i.e. $k$ indices $i$ with $\pi_i<\pi_{i+1}$.

**Proof of the recurrence.** Every permutation of $\{1,\dots,n\}$ arises in exactly one way by inserting the largest element $n$ into one of the $n$ gaps (before the first element, between two elements, or after the last) of a permutation $\rho$ of $\{1,\dots,n-1\}$. Suppose $\rho$ has $j$ ascents; it then has $n-2-j$ descents ($\rho_i>\rho_{i+1}$). How does inserting $n$ change the number of ascents?

- **At the front:** $n\,\rho_1\dots$ starts with a descent; the number of ascents stays $j$.
- **Inside an ascent** $\rho_i<\rho_{i+1}$: it becomes $\rho_i<n>\rho_{i+1}$, one ascent replaced by one ascent and one descent: still $j$.
- **Inside a descent** $\rho_i>\rho_{i+1}$: it becomes $\rho_i<n>\rho_{i+1}$: one ascent is added, $j+1$.
- **At the end:** $\dots\rho_{n-1}<n$ adds one ascent, $j+1$.

So, from a permutation with $j$ ascents, $1+j$ gaps keep $j$ ascents and $(n-2-j)+1=n-1-j$ gaps give $j+1$ ascents.

A permutation of $n$ elements with $k$ ascents therefore comes either from one with $k$ ascents, using one of $k+1$ gaps, or from one with $k-1$ ascents, using one of $n-1-(k-1)=n-k$ gaps:

$$\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle\qquad(n\ge1)$$

with $\left\langle\genfrac{}{}{0pt}{}{0}{0}\right\rangle=1$ and $\left\langle\genfrac{}{}{0pt}{}{0}{k}\right\rangle=0$ for $k\ne0$. $\blacksquare$

**Check.** Row $n=3$ is $1,4,1$ and row $n=4$ is $1,11,11,1$; e.g. $\left\langle\genfrac{}{}{0pt}{}{4}{2}\right\rangle=3\cdot \left\langle\genfrac{}{}{0pt}{}{3}{2}\right\rangle+2\cdot \left\langle\genfrac{}{}{0pt}{}{3}{1}\right\rangle=3+8=11$.
