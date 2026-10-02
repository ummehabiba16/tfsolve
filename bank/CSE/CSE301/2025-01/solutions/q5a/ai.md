---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$17$ is prime and $17\nmid3$, so $3^{16}\equiv1\pmod{17}$ (Fermat). $2024=16\cdot126+8$, so $3^{2024}\equiv3^8=(3^4)^2\equiv13^2=169\equiv16\pmod{17}$. Answer: $16$ (i.e. $-1$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (Fermat''s theorem, congruences)']
---
$17$ is prime and $3\perp17$, so by Fermat's little theorem

$$3^{16}\equiv1\pmod{17}$$

Since $2024=16\times126+8$,

$$3^{2024}=\left(3^{16}\right)^{126}\cdot3^8\equiv3^8\pmod{17}$$

By repeated squaring:

$$3^2=9,\qquad3^4=81=4\cdot17+13\equiv13,\qquad3^8\equiv13^2=169=9\cdot17+16\equiv16\pmod{17}$$

$$3^{2024}\bmod17=\mathbf{16}\qquad(\text{i.e. }3^{2024}\equiv-1\pmod{17})$$
