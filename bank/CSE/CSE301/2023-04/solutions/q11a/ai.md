---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$a_n=2$, $b_n=n$, $c_n=3n!$; summation factor $s_n=2^{n-1}/n!$ gives $S_n=\frac{2^n}{n!}T_n=S_{n-1}+3\cdot2^{n-1}$, $S_0=5$, so $S_n=3\cdot2^n+2$ and $T_n=3\cdot n!+\frac{n!}{2^{n-1}}$ ($n\ge1$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (summation factors)', 'Supplementary materials attached to the paper (sums, item 1)']
---
**Summation factor.** The recurrence has the form $a_nT_n=b_nT_{n-1}+c_n$ with

$$a_n=2,\qquad b_n=n,\qquad c_n=3\cdot n!$$

Choose $s_n$ so that $s_nb_n=s_{n-1}a_{n-1}$:

$$s_n=\frac{a_{n-1}a_{n-2}\cdots a_1}{b_nb_{n-1}\cdots b_2}=\frac{2^{n-1}}{n!}$$

Multiplying the recurrence by $s_n$ and writing $S_n=s_na_nT_n=\frac{2^n}{n!}T_n$ gives

$$S_n=S_{n-1}+s_nc_n=S_{n-1}+\frac{2^{n-1}}{n!}\cdot3\cdot n!=S_{n-1}+3\cdot2^{n-1}$$

with $S_0=T_0=5$. Hence

$$S_n=5+3\left(1+2+\cdots+2^{n-1}\right)=5+3\left(2^n-1\right)=3\cdot2^n+2$$

$$T_n=\frac{n!}{2^n}S_n=\frac{n!}{2^n}\left(3\cdot2^n+2\right)=3\cdot n!+\frac{n!}{2^{n-1}}\qquad(n\ge1)$$

(This agrees with the supplementary formula $T_n=\frac{1}{s_na_n}\big(s_1b_1T_0+\sum_{k=1}^{n}s_kc_k\big)$, since $s_1b_1T_0=1\cdot1\cdot5$.)

**Check.** $2T_1=1\cdot5+3=8$, so $T_1=4=3+1$. $2T_2=2\cdot4+6=14$, so $T_2=7=6+1$. $2T_3=3\cdot7+18=39$, so $T_3=19.5=18+\frac{6}{4}$.

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
