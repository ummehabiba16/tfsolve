---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$F(z)=\sum F_nz^n$ satisfies $F(z)-zF(z)-z^2F(z)=z$, so $F(z)=\frac{z}{1-z-z^2}=\frac{1}{\sqrt5}\Big(\frac{1}{1-\phi z}-\frac{1}{1-\hat\phi z}\Big)$ and $F_n=\frac{\phi^n-\hat\phi^n}{\sqrt5}$, $\phi=\frac{1+\sqrt5}{2}$, $\hat\phi=\frac{1-\sqrt5}{2}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Fibonacci numbers) and Ch. 7 (solving recurrences with generating functions)']
---
**Recurrence.** $F_0=0$, $F_1=1$ and $F_n=F_{n-1}+F_{n-2}$ for $n\ge2$. One equation valid for all integers $n$ (with $F_n=0$ for $n<0$) is

$$F_n=F_{n-1}+F_{n-2}+[n=1]$$

**Generating function.** Let $F(z)=\sum_{n\ge0}F_nz^n$. Multiply by $z^n$ and sum over $n$:

$$F(z)=zF(z)+z^2F(z)+z\qquad\Longrightarrow\qquad F(z)=\frac{z}{1-z-z^2}$$

**Partial fractions.** $1-z-z^2=(1-\phi z)(1-\hat\phi z)$ with $\phi=\frac{1+\sqrt5}{2}$ and $\hat\phi=\frac{1-\sqrt5}{2}$ (the roots of $t^2=t+1$; $\phi+\hat\phi=1$, $\phi\hat\phi=-1$, $\phi-\hat\phi=\sqrt5$). Then

$$\frac{z}{(1-\phi z)(1-\hat\phi z)}=\frac{1}{\sqrt5}\left(\frac{1}{1-\phi z}-\frac{1}{1-\hat\phi z}\right)$$

(check: the difference of the two fractions is $\frac{(\phi-\hat\phi)z}{(1-\phi z)(1-\hat\phi z)}$).

**Values.** Expanding each fraction as a geometric series, $\frac{1}{1-\phi z}=\sum\phi^nz^n$:

$$F_n=\frac{\phi^n-\hat\phi^n}{\sqrt5}=\frac{1}{\sqrt5}\left[\left(\frac{1+\sqrt5}{2}\right)^n-\left(\frac{1-\sqrt5}{2}\right)^n\right]$$

Since $|\hat\phi|<1$, $F_n$ is the integer nearest to $\phi^n/\sqrt5$. Check: $F_2=\frac{\phi^2-\hat\phi^2}{\sqrt5}=\phi+\hat\phi=1$, and the series begins $z+z^2+2z^3+3z^4+5z^5+8z^6+\cdots$
