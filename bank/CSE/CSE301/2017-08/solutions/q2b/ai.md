---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Summation by parts with $u=H_x$, $\Delta v=x^2=x^{\underline2}+x^{\underline1}$: $\sum x^2H_x\,\delta x=H_x\big(\frac{x^{\underline3}}{3}+\frac{x^{\underline2}}{2}\big)-\frac{x^{\underline3}}{9}-\frac{x^{\underline2}}{4}+C$, so $\sum_{0\le k<n}k^2H_k=\frac{n(n-1)(2n-1)}{6}H_n-\frac{n(n-1)(4n+1)}{36}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (finite calculus, summation by parts)']
---
**Finite calculus tools.** With $\Delta f(x)=f(x+1)-f(x)$, $Ef(x)=f(x+1)$ and falling powers $x^{\underline m}=x(x-1)\cdots(x-m+1)$:

$$\Delta x^{\underline m}=m\,x^{\underline{m-1}},\qquad\sum x^{\underline m}\,\delta x=\frac{x^{\underline{m+1}}}{m+1}+C,\qquad\Delta H_x=\frac{1}{x+1}$$

and **summation by parts**: $\sum u\,\Delta v\,\delta x=uv-\sum Ev\,\Delta u\,\delta x$.

**Write $x^2$ in falling powers:** $x^2=x^{\underline2}+x^{\underline1}$.

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
