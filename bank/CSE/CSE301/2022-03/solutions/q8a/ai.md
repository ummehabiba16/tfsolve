---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Inner sum $\sum_{j\le k}\frac1j=H_k$, so $S=\sum_{1\le k<n}\frac{H_k}{(k+1)(k+2)}=\sum_1^nH_xx^{\underline{-2}}\delta x$; summation by parts gives $\sum H_xx^{\underline{-2}}\delta x=-\frac{H_x+1}{x+1}$, so $S=1-\frac{H_n+1}{n+1}=\frac{n-H_n}{n+1}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (multiple sums, finite calculus, summation by parts)']
---
**Sum over $j$ first** (the condition is $1\le j\le k<n$):

$$S=\sum_{1\le k<n}\frac{1}{(k+1)(k+2)}\sum_{1\le j\le k}\frac1j=\sum_{1\le k<n}\frac{H_k}{(k+1)(k+2)}$$

**Finite calculus.** The negative falling power $x^{\underline{-2}}=\frac{1}{(x+1)(x+2)}$ satisfies $\Delta x^{\underline{-1}}=-x^{\underline{-2}}$, so $\sum x^{\underline{-2}}\,\delta x=-x^{\underline{-1}}=-\frac{1}{x+1}$. Then

$$S=\sum_1^nH_x\,x^{\underline{-2}}\,\delta x$$

**Summation by parts** ($\sum u\,\Delta v=uv-\sum Ev\,\Delta u$) with $u=H_x$, $\Delta v=x^{\underline{-2}}$:

$$v=-\frac{1}{x+1},\qquad Ev=-\frac{1}{x+2},\qquad\Delta u=H_{x+1}-H_x=\frac{1}{x+1}$$

$$\sum H_xx^{\underline{-2}}\,\delta x=-\frac{H_x}{x+1}+\sum\frac{1}{(x+1)(x+2)}\,\delta x=-\frac{H_x}{x+1}-\frac{1}{x+1}=-\frac{H_x+1}{x+1}$$

**Evaluate from 1 to $n$.**

$$S=\left[-\frac{H_x+1}{x+1}\right]_1^n=-\frac{H_n+1}{n+1}+\frac{H_1+1}{2}=1-\frac{H_n+1}{n+1}=\frac{n-H_n}{n+1}$$

**Check.** $n=2$: only $j=k=1$, $S=\frac{1}{1\cdot2\cdot3}=\frac16$, and $\frac{2-\frac32}{3}=\frac16$. $n=3$: $\frac16+\frac{H_2}{12}=\frac16+\frac18=\frac{7}{24}$, and $\frac{3-\frac{11}{6}}{4}=\frac{7}{24}$.
