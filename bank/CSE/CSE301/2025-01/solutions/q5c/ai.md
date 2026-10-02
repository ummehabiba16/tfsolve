---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\sum_{n\ge0}(n+1)^2z^n=\frac{1+z}{(1-z)^3}$ (from $\frac{1}{1-z}$ by applying $zD$ twice); if the sequence is indexed from $n=1$ with $a_0=0$, it is $\frac{z(1+z)}{(1-z)^3}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (generating function manipulations)']
---
We want $G(z)=1+4z+9z^2+16z^3+\cdots=\sum_{n\ge0}(n+1)^2z^n$.

**Start from the geometric series** and use the rule $zG'(z)=\sum_nng_nz^n$ (multiplying the coefficients by $n$):

$$\frac{1}{1-z}=\sum_{n\ge0}z^n$$

$$z\frac{d}{dz}\frac{1}{1-z}=\frac{z}{(1-z)^2}=\sum_{n\ge0}nz^n$$

$$z\frac{d}{dz}\frac{z}{(1-z)^2}=z\cdot\frac{(1-z)^2+2z(1-z)}{(1-z)^4}=\frac{z(1+z)}{(1-z)^3}=\sum_{n\ge0}n^2z^n$$

**Shift the index.** $\sum_{n\ge0}n^2z^n=0+z+4z^2+9z^3+\cdots$, so dividing by $z$:

$$G(z)=\sum_{n\ge0}(n+1)^2z^n=\frac{1+z}{(1-z)^3}$$

**Check:** $(1+z)(1+3z+6z^2+10z^3+\cdots)=1+4z+9z^2+16z^3+\cdots$ (using $\frac{1}{(1-z)^3}=\sum\binom{n+2}{2}z^n$).

(If the sequence is meant as $g_n=n^2$ for $n\ge0$, i.e. $0,1,4,9,\dots$, the generating function is $\frac{z(1+z)}{(1-z)^3}$.)
