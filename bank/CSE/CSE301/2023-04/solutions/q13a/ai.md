---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Group $k=1,\dots,m$ by $g=\gcd(k,m)$: writing $k=gj$, the $k$ with $\gcd(k,m)=g$ correspond to $1\le j\le m/g$ with $j\perp m/g$, so there are $\varphi(m/g)$ of them. Summing over $g\mid m$: $m=\sum_{g\mid m}\varphi(m/g)=\sum_{d\mid m}\varphi(d)$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (phi and mu: identity (4.54))']
---
**Claim.** $\sum_{d\mid m}\varphi(d)=m$ for every positive integer $m$.

**Proof by counting.** Sort the $m$ integers $k=1,2,\dots,m$ according to $g=\gcd(k,m)$, which is always a divisor of $m$.

For a fixed divisor $g$ of $m$, the integers $k$ with $\gcd(k,m)=g$ are exactly $k=gj$ with $1\le j\le\frac mg$ and

$$\gcd(gj,\ m)=g\iff\gcd\left(j,\ \frac mg\right)=1$$

The number of such $j$ is $\varphi\!\left(\frac mg\right)$. Every $k$ is counted for exactly one $g$, so

$$m=\sum_{g\mid m}\varphi\!\left(\frac mg\right)=\sum_{d\mid m}\varphi(d)$$

since $d=\frac mg$ runs over all divisors of $m$ as $g$ does. $\blacksquare$

**Equivalent view (Concrete Mathematics).** Reduce the $m$ fractions $\frac0m,\frac1m,\dots,\frac{m-1}{m}$ to lowest terms. The reduced fractions with denominator $d$ are $\frac jd$ with $0\le j<d$, $j\perp d$: there are $\varphi(d)$ of them, and every divisor $d$ of $m$ occurs. So $m=\sum_{d\mid m}\varphi(d)$.

**Example $m=12$.** $\varphi(1)+\varphi(2)+\varphi(3)+\varphi(4)+\varphi(6)+\varphi(12)=1+1+2+2+2+4=12$.

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
