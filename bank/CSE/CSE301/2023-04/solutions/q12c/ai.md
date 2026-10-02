---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For a complete residue system mod $m$, the sum is $\equiv0+1+\cdots+(m-1)=\frac{m(m-1)}{2}\equiv\frac m2\pmod m$ when $m$ is even. If $\{a_i+b_i\}$ were complete, $\frac m2\equiv\sum(a_i+b_i)=\sum a_i+\sum b_i\equiv\frac m2+\frac m2=m\equiv0\pmod m$, a contradiction.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (residue classes)']
---
**Sum of a complete residue system.** If $\{c_1,\dots,c_m\}$ is a complete set of residues modulo $m$, its elements are congruent, in some order, to $0,1,\dots,m-1$, so

$$\sum_{i=1}^{m}c_i\equiv0+1+\cdots+(m-1)=\frac{m(m-1)}{2}\pmod m$$

**When $m$ is even**, write $m=2t$. Then

$$\frac{m(m-1)}{2}=t(2t-1)=2t^2-t\equiv-t\equiv t=\frac m2\pmod m$$

so the sum of a complete residue system is $\equiv\frac m2\not\equiv0\pmod m$.

**Proof.** Suppose, for contradiction, that $\{a_1+b_1,\dots,a_m+b_m\}$ is a complete residue system. Then

$$\frac m2\equiv\sum_{i=1}^{m}(a_i+b_i)=\sum_{i=1}^{m}a_i+\sum_{i=1}^{m}b_i\equiv\frac m2+\frac m2=m\equiv0\pmod m$$

because both $\{a_i\}$ and $\{b_i\}$ are complete residue systems. But $\frac m2\not\equiv0\pmod m$ (as $0<\frac m2<m$). This contradiction shows that $\{a_1+b_1,\dots,a_m+b_m\}$ is **not** a complete residue system. $\blacksquare$

(For odd $m$ the argument fails, and indeed $a_i=b_i=i$ gives $\{2i\}$, which is complete when $m$ is odd. A computer check of all pairings for $m=2,4,6$ finds no complete sum system, as the proof predicts.)

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
