---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Write $n=(a_m\dots a_1a_0)_p$; then $\lfloor n/p^k\rfloor=\sum_{j\ge k}a_jp^{j-k}$, so $\epsilon_p(n!)=\sum_{k\ge1}\lfloor n/p^k\rfloor=\sum_ja_j\frac{p^j-1}{p-1}=\frac{n-\nu_p(n)}{p-1}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (factorial factors, exercise on digit sums)']
---
Let $\epsilon_p(n!)$ be the exponent of the prime $p$ in $n!$ and $\nu_p(n)$ the sum of the digits of $n$ in base $p$.

**Legendre's formula** (supplementary materials): $\epsilon_p(n!)=\sum_{k\ge1}\left\lfloor\frac{n}{p^k}\right\rfloor$. It holds because $\lfloor n/p^k\rfloor$ counts the multiples of $p^k$ among $1,\dots,n$, so a number divisible exactly by $p^e$ is counted once for each $k=1,\dots,e$.

**Base-$p$ digits.** Write $n=a_mp^m+\cdots+a_1p+a_0$ with digits $0\le a_j<p$. Dividing by $p^k$ and dropping the fraction removes the last $k$ digits:

$$\left\lfloor\frac{n}{p^k}\right\rfloor=\sum_{j\ge k}a_jp^{j-k}$$

**Sum over $k$.** Exchange the order of summation:

$$\epsilon_p(n!)=\sum_{k\ge1}\sum_{j\ge k}a_jp^{j-k}=\sum_{j\ge1}a_j\left(p^{j-1}+p^{j-2}+\cdots+1\right)=\sum_{j\ge0}a_j\,\frac{p^j-1}{p-1}$$

(the $j=0$ term is 0). Splitting the numerator,

$$\epsilon_p(n!)=\frac{\sum_ja_jp^j-\sum_ja_j}{p-1}=\frac{n-\nu_p(n)}{p-1}$$

**Example.** $n=100=(1100100)_2$, so $\nu_2(100)=3$ and $\epsilon_2(100!)=\frac{100-3}{1}=97$, which agrees with $50+25+12+6+3+1=97$.
