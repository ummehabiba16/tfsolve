---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'If $m_1,\dots,m_r$ are pairwise coprime and $M=m_1\cdots m_r$, the system $x\equiv a_i\pmod{m_i}$ has a solution, unique mod $M$. Existence: $x=\sum_ia_iM_iy_i$ with $M_i=M/m_i$ and $M_iy_i\equiv1\pmod{m_i}$; uniqueness: two solutions differ by a multiple of every $m_i$, hence of $M$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (independent residues, the Chinese Remainder Theorem)']
---
**Statement.** Let $m_1,m_2,\dots,m_r$ be positive integers that are pairwise relatively prime ($m_i\perp m_j$ for $i\ne j$), let $M=m_1m_2\cdots m_r$, and let $a_1,\dots,a_r$ be any integers. Then the system

$$x\equiv a_1\pmod{m_1},\qquad x\equiv a_2\pmod{m_2},\qquad\dots,\qquad x\equiv a_r\pmod{m_r}$$

has a solution $x$, and the solution is unique modulo $M$.

**Proof of existence.** Let $M_i=M/m_i$, the product of all moduli except $m_i$. Since each $m_j$ ($j\ne i$) is relatively prime to $m_i$, so is their product: $M_i\perp m_i$. By Euclid's algorithm (Bézout) there is an integer $y_i$ with

$$M_iy_i\equiv1\pmod{m_i}$$

Put

$$x=a_1M_1y_1+a_2M_2y_2+\cdots+a_rM_ry_r$$

Modulo $m_j$, every term with $i\ne j$ vanishes because $m_j\mid M_i$, and the $j$-th term is $a_jM_jy_j\equiv a_j\cdot1$. So $x\equiv a_j\pmod{m_j}$ for every $j$.

**Proof of uniqueness.** If $x$ and $x'$ are both solutions, then $m_i\mid x-x'$ for every $i$. Since the $m_i$ are pairwise relatively prime, their product divides $x-x'$ (by induction, using $k\perp m$ and $k\perp n\Rightarrow k\perp mn$ and the fact that $m\mid z$, $n\mid z$, $m\perp n$ imply $mn\mid z$). So $x\equiv x'\pmod M$. Conversely, every $x'\equiv x\pmod M$ is a solution. $\blacksquare$

**Equivalent form.** The map $x\bmod M\mapsto(x\bmod m_1,\dots,x\bmod m_r)$ is a one-to-one correspondence between the $M$ residues modulo $M$ and the $M$ tuples of residues (the residues are "independent").

**Example.** $x\equiv2\pmod3$, $x\equiv3\pmod5$, $x\equiv2\pmod7$: $M=105$, $M_1=35$, $M_2=21$, $M_3=15$; $35\cdot2\equiv1\pmod3$, $21\cdot1\equiv1\pmod5$, $15\cdot1\equiv1\pmod7$. So $x=2\cdot35\cdot2+3\cdot21\cdot1+2\cdot15\cdot1=233\equiv23\pmod{105}$.
