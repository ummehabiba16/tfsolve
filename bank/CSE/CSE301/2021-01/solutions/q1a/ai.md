---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$m^3=6\binom m3+6\binom m2+\binom m1$ ($a=b=6$, $c=1$); summing with $\sum_{m\le n}\binom mk=\binom{n+1}{k+1}$: $\sum_{m=1}^{n}m^3=6\binom{n+1}{4}+6\binom{n+1}{3}+\binom{n+1}{2}=\frac{n^2(n+1)^2}{4}$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 5 (binomial coefficients, Pascal''s formula)', 'Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (binomial coefficients) and Ch. 2 (falling powers)']
---
**Finding $a,b,c$.** The identity must hold for every $m$, so substitute small values ($\binom m3=0$ for $m<3$, $\binom m2=0$ for $m<2$):

- $m=1$: $1=c$, so $c=1$.
- $m=2$: $8=b\binom22+c\binom21=b+2$, so $b=6$.
- $m=3$: $27=a+3b+3c=a+21$, so $a=6$.

Both sides are cubic polynomials in $m$ that agree at $m=0,1,2,3$ (four points), so they are identical:

$$m^3=6\binom m3+6\binom m2+\binom m1$$

(Equivalently $m^3=m(m-1)(m-2)+3m(m-1)+m$; check $m=4$: $6\cdot4+6\cdot6+4=64$.)

**Sum of cubes.** Use the hockey-stick (upper summation) identity $\sum_{m=0}^{n}\binom mk=\binom{n+1}{k+1}$:

$$\sum_{m=1}^{n}m^3=6\sum_{m}\binom m3+6\sum_{m}\binom m2+\sum_{m}\binom m1=6\binom{n+1}{4}+6\binom{n+1}{3}+\binom{n+1}{2}$$

$$=\frac{(n+1)n(n-1)(n-2)}{4}+(n+1)n(n-1)+\frac{(n+1)n}{2}$$

$$=\frac{(n+1)n}{4}\Big[(n-1)(n-2)+4(n-1)+2\Big]=\frac{(n+1)n}{4}\,(n^2+n)$$

$$1^3+2^3+\cdots+n^3=\frac{n^2(n+1)^2}{4}=\left(\frac{n(n+1)}{2}\right)^2$$

(Check $n=3$: $1+8+27=36=6^2$.)
