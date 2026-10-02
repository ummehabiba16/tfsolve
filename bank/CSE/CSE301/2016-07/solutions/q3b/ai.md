---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Inversion: $g(n)=\sum_k\binom nkf(k)\iff f(n)=\sum_k(-1)^{n-k}\binom nkg(k)$. From $n!=\sum_k\binom nkD_k$ we get $D_n=\sum_k(-1)^{n-k}\binom nkk!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}$ ways in which everyone gets a wrong hat.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (inversion formula (5.48), the football victory problem)']
---
**Inversion formula.** For sequences $f$ and $g$,

$$g(n)=\sum_{k}\binom nk f(k)\quad\text{for all }n\qquad\Longleftrightarrow\qquad f(n)=\sum_{k}(-1)^{n-k}\binom nk g(k)\quad\text{for all }n$$

**Proof** (of $\Rightarrow$; the converse is identical with the roles exchanged). Substitute $g$ and use $\binom nk\binom kj=\binom nj\binom{n-j}{k-j}$:

$$\sum_k(-1)^{n-k}\binom nkg(k)=\sum_k(-1)^{n-k}\binom nk\sum_j\binom kjf(j)=\sum_jf(j)\binom nj\sum_k(-1)^{n-k}\binom{n-j}{k-j}$$

The inner sum is $\sum_{i=0}^{n-j}(-1)^{n-j-i}\binom{n-j}{i}=(1-1)^{n-j}=[n=j]$ (with $i=k-j$), so the whole expression equals $f(n)$.

**Hats.** Let $D_k$ be the number of ways in which $k$ men all receive wrong hats (derangements), $D_0=1$. Classify the $n!$ ways of returning $n$ hats by the set of men who receive wrong hats: if that set has $k$ men, choose it in $\binom nk$ ways and derange their hats in $D_k$ ways (the other men get their own hats). So

$$n!=\sum_{k}\binom nkD_k$$

This is $g(n)=\sum_k\binom nkf(k)$ with $g(k)=k!$ and $f(k)=D_k$. By the inversion formula,

$$D_n=\sum_k(-1)^{n-k}\binom nk\,k!=\sum_{k}(-1)^{n-k}\frac{n!}{(n-k)!}=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}$$

**Answer.** The men can all end up with wrong hats in

$$D_n=n!\left(1-\frac1{1!}+\frac1{2!}-\cdots+\frac{(-1)^n}{n!}\right)$$

ways, the integer nearest to $n!/e$ (e.g. $D_3=2$, $D_4=9$, $D_5=44$, $D_6=265$).
