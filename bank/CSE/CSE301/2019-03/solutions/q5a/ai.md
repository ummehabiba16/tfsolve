---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Characteristic roots of $r^2-17r+70=0$ are $7$ and $10$; a constant particular solution $c$ needs $54c=6$, $c=\frac19$. With $a_0=1$, $a_1=9$: $a_n=\frac89\,10^n+\frac19=\frac{8\cdot10^n+1}{9}$ ($=88\dots89$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (solving recurrences)', 'Brualdi, Introductory Combinatorics, Ch. 7 (linear recurrences with constant coefficients)']
---
We read the recurrence as holding for all $n\ge0$ (with "$n\ge2$" the terms $a_2,a_3$ would not be determined):

$$a_{n+2}-17a_{n+1}+70a_n=6,\qquad a_0=1,\ a_1=9$$

**Homogeneous part.** The characteristic equation is

$$r^2-17r+70=0\iff(r-7)(r-10)=0$$

so the homogeneous solutions are $A\cdot7^n+B\cdot10^n$.

**Particular solution.** Try a constant $a_n=c$: $c-17c+70c=54c=6$, so $c=\frac19$.

**General solution and initial conditions.**

$$a_n=A\cdot7^n+B\cdot10^n+\frac19$$

$$a_0=1:\quad A+B=\frac89$$

$$a_1=9:\quad7A+10B=9-\frac19=\frac{80}{9}$$

From the first equation $A=\frac89-B$; then $\frac{56}{9}+3B=\frac{80}{9}$, so $B=\frac89$ and $A=0$.

$$a_n=\frac{8\cdot10^n+1}{9}$$

**Check.** $a_2=17\cdot9-70\cdot1+6=89=\frac{801}{9}$, $a_3=17\cdot89-70\cdot9+6=889$. In decimal, $a_n=\underbrace{88\cdots8}_{n-1}9$ for $n\ge1$.
