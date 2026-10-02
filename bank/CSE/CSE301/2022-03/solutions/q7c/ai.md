---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Binomial theorem: $B_1=\sum_k\binom nk2^k1^{n-k}=(2+1)^n=3^n$; $B_2=3^{-n}\sum_k\binom nk3^k=3^{-n}(3+1)^n=\left(\frac43\right)^n$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (the binomial theorem)']
---
Both sums are instances of the binomial theorem $(x+y)^n=\sum_{k=0}^{n}\binom nkx^ky^{n-k}$.

**$B_1$.** With $x=2$, $y=1$:

$$B_1=\sum_{k=0}^{n}2^k\binom nk=\sum_{k=0}^{n}\binom nk2^k1^{n-k}=(2+1)^n=3^n$$

(Combinatorially: each of $n$ elements is either outside a subset, or inside it with one of 2 colours: $3^n$ ways.)

**$B_2$.** Take the constant factor $3^{-n}$ out, then use $x=3$, $y=1$:

$$B_2=\sum_{k=0}^{n}3^{k-n}\binom nk=3^{-n}\sum_{k=0}^{n}\binom nk3^k=3^{-n}(3+1)^n=\left(\frac43\right)^n$$

**Check ($n=2$).** $B_1=1+4+4=9=3^2$; $B_2=\frac19+\frac{2\cdot3}{9}+\frac{9}{9}=\frac{16}{9}=\left(\frac43\right)^2$.
