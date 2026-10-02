---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$g(n)=\sum_k\binom nkf(k)$ for all $n\iff f(n)=\sum_k(-1)^{n-k}\binom nkg(k)$ for all $n$. Proof: substitute and use $\binom nk\binom kj=\binom nj\binom{n-j}{k-j}$ and $\sum_i(-1)^{n-j-i}\binom{n-j}{i}=(1-1)^{n-j}=[n=j]$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 (inversion formula (5.48))']
---
**Inversion formula.** For sequences $f$ and $g$,

$$g(n)=\sum_{k}\binom nk f(k)\quad\text{for all }n\qquad\Longleftrightarrow\qquad f(n)=\sum_{k}(-1)^{n-k}\binom nk g(k)\quad\text{for all }n$$

**Proof** (of $\Rightarrow$; the converse is identical with the roles exchanged). Substitute $g$ and use $\binom nk\binom kj=\binom nj\binom{n-j}{k-j}$:

$$\sum_k(-1)^{n-k}\binom nkg(k)=\sum_k(-1)^{n-k}\binom nk\sum_j\binom kjf(j)=\sum_jf(j)\binom nj\sum_k(-1)^{n-k}\binom{n-j}{k-j}$$

The inner sum is $\sum_{i=0}^{n-j}(-1)^{n-j-i}\binom{n-j}{i}=(1-1)^{n-j}=[n=j]$ (with $i=k-j$), so the whole expression equals $f(n)$.

**Example (derangements).** Every arrangement of $n$ hats has some set of $k$ men who get wrong hats, so $n!=\sum_k\binom nkD_k$. Inversion gives

$$D_n=\sum_k(-1)^{n-k}\binom nkk!=n!\sum_{j=0}^{n}\frac{(-1)^j}{j!}$$

the number of derangements of $n$ objects.
