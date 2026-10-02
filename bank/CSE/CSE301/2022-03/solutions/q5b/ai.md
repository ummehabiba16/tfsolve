---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'From $x\cdot x^{\underline k}=x^{\underline{k+1}}+kx^{\underline k}$ (the Stirling recurrence): $x^5=x^{\underline5}+10x^{\underline4}+25x^{\underline3}+15x^{\underline2}+x^{\underline1}$. Summing with $\sum x^{\underline m}\delta x=\frac{x^{\underline{m+1}}}{m+1}$ from 0 to $n+1$: $S=\frac{n^2(n+1)^2(2n^2+2n-1)}{12}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (finite calculus) and Ch. 6 (Stirling numbers, identity (6.10))']
---
**Step 1: $x^5$ in falling powers.** The given identity says that the Stirling numbers of the second kind in row 4 are $1,7,6,1$, i.e. $x^4=\sum_k\genfrac\{\}{0pt}{}{4}{k}x^{\underline k}$. Since $x\cdot x^{\underline k}=x^{\underline{k+1}}+k\,x^{\underline k}$ (because $x^{\underline{k+1}}=x^{\underline k}(x-k)$), multiplying the identity by $x$ gives

$$x^5=\left(x^{\underline5}+4x^{\underline4}\right)+6\left(x^{\underline4}+3x^{\underline3}\right)+7\left(x^{\underline3}+2x^{\underline2}\right)+\left(x^{\underline2}+x^{\underline1}\right)$$

$$x^5=x^{\underline5}+10x^{\underline4}+25x^{\underline3}+15x^{\underline2}+x^{\underline1}$$

This is the same as applying the given recurrence $\genfrac\{\}{0pt}{}{5}{k}=\genfrac\{\}{0pt}{}{4}{k-1}+k\genfrac\{\}{0pt}{}{4}{k}$: $\genfrac\{\}{0pt}{}{5}{2}=1+2\cdot7=15$, $\genfrac\{\}{0pt}{}{5}{3}=7+3\cdot6=25$, $\genfrac\{\}{0pt}{}{5}{4}=6+4\cdot1=10$.

**Step 2: sum with finite calculus.** Using $\sum x^{\underline m}\,\delta x=\frac{x^{\underline{m+1}}}{m+1}$ and $\sum_{0\le k\le n}g(k)=\sum_0^{n+1}g(x)\,\delta x$:

$$S=\sum_{0\le k\le n}k^5=\left[\frac{x^{\underline6}}{6}+2x^{\underline5}+\frac{25}{4}x^{\underline4}+5x^{\underline3}+\frac{x^{\underline2}}{2}\right]_0^{n+1}$$

$$=\frac{(n+1)^{\underline6}}{6}+2(n+1)^{\underline5}+\frac{25}{4}(n+1)^{\underline4}+5(n+1)^{\underline3}+\frac{(n+1)^{\underline2}}{2}$$

(all terms vanish at $x=0$). Expanding and collecting,

$$\sum_{0\le k\le n}k^5=\frac{n^2(n+1)^2\left(2n^2+2n-1\right)}{12}$$

**Check.** $n=2$: $1+32=33=\frac{4\cdot9\cdot11}{12}$. $n=3$: $33+243=276=\frac{9\cdot16\cdot23}{12}$.
