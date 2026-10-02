---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Finite calculus: $\Delta f=f(x+1)-f(x)$, $\Delta x^{\underline m}=mx^{\underline{m-1}}$, $\sum_a^bg\,\delta x=f(b)-f(a)$ for $\Delta f=g$, summation by parts $\sum u\Delta v=uv-\sum Ev\Delta u$. Then $\sum_{0\le k<n}k^2H_k=\frac{n(n-1)(2n-1)}{6}H_n-\frac{n(n-1)(4n+1)}{36}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (finite and infinite calculus, summation by parts)']
---
**Finite calculus** mirrors ordinary calculus with the difference operator in place of the derivative.

- **Difference and shift:** $\Delta f(x)=f(x+1)-f(x)$, $Ef(x)=f(x+1)$.
- **Falling powers** play the role of $x^m$: $x^{\underline m}=x(x-1)\cdots(x-m+1)$ and $\Delta x^{\underline m}=m\,x^{\underline{m-1}}$ (e.g. $\Delta x^{\underline2}=(x+1)x-x(x-1)=2x$).
- **Indefinite sums:** $\sum g(x)\,\delta x=f(x)+C$ if $\Delta f=g$; so $\sum x^{\underline m}\,\delta x=\frac{x^{\underline{m+1}}}{m+1}$ ($m\ne-1$) and $\sum x^{\underline{-1}}\,\delta x=H_x$.
- **Fundamental theorem:** $\sum_a^bg(x)\,\delta x=\sum_{a\le k<b}g(k)=f(b)-f(a)$. Example: $\sum_{0\le k<n}k=\frac{n^{\underline2}}{2}=\frac{n(n-1)}{2}$.
- **Exponentials:** $\Delta2^x=2^x$ and $\Delta c^x=(c-1)c^x$, so $\sum_{0\le k<n}c^k=\frac{c^n-1}{c-1}$.
- **Linearity**, and the **product rule** $\Delta(uv)=u\,\Delta v+Ev\,\Delta u$, which gives **summation by parts**:

$$\sum u\,\Delta v\,\delta x=uv-\sum Ev\,\Delta u\,\delta x$$

Example: $\sum_{0\le k<n}k\,2^k=\big[x2^x\big]_0^n-\sum_0^n2^{x+1}\delta x=n2^n-(2^{n+1}-2)=(n-2)2^n+2$.

**Now $\sum_{0\le k<n}k^2H_k$.** Write $x^2$ in falling powers: $x^2=x^{\underline2}+x^{\underline1}$.


**Summation by parts** with $u=H_x$ and $\Delta v=x^{\underline2}+x^{\underline1}$:

$$v=\frac{x^{\underline3}}{3}+\frac{x^{\underline2}}{2},\qquad\Delta u=\frac{1}{x+1},\qquad Ev=\frac{(x+1)^{\underline3}}{3}+\frac{(x+1)^{\underline2}}{2}$$

Since $(x+1)^{\underline3}=(x+1)x^{\underline2}$ and $(x+1)^{\underline2}=(x+1)x^{\underline1}$,

$$Ev\,\Delta u=\frac{x^{\underline2}}{3}+\frac{x^{\underline1}}{2}$$

$$\sum x^2H_x\,\delta x=H_x\left(\frac{x^{\underline3}}{3}+\frac{x^{\underline2}}{2}\right)-\sum\left(\frac{x^{\underline2}}{3}+\frac{x^{\underline1}}{2}\right)\delta x$$

$$=H_x\left(\frac{x^{\underline3}}{3}+\frac{x^{\underline2}}{2}\right)-\frac{x^{\underline3}}{9}-\frac{x^{\underline2}}{4}+C$$

**Simplified.** $\frac{x^{\underline3}}{3}+\frac{x^{\underline2}}{2}=\frac{x(x-1)(2x-1)}{6}$ and $\frac{x^{\underline3}}{9}+\frac{x^{\underline2}}{4}=\frac{x(x-1)(4x+1)}{36}$, so

$$\sum x^2H_x\,\delta x=\frac{x(x-1)(2x-1)}{6}\,H_x-\frac{x(x-1)(4x+1)}{36}+C$$

**Definite sum.** Evaluating from $0$ to $n$:

$$\sum_{0\le k<n}k^2H_k=\frac{n(n-1)(2n-1)}{6}\,H_n-\frac{n(n-1)(4n+1)}{36}$$

Check $n=3$: $0+1\cdot1+4\cdot\frac32=7$ and $\frac{3\cdot2\cdot5}{6}\cdot\frac{11}{6}-\frac{3\cdot2\cdot13}{36}=\frac{55}{6}-\frac{13}{6}=7$.
