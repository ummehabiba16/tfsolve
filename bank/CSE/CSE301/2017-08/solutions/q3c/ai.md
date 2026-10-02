---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With $D_n$ the number of ways, $n!=\sum_k\binom nkD_{n-k}$; in exponential generating functions $\frac{1}{1-z}=e^zD(z)$, so $D(z)=\frac{e^{-z}}{1-z}$ and $D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}\approx n!/e$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5 and 7 (the football victory problem, exponential generating functions)']
---
Let $D_n$ be the number of ways in which **no** fan gets his own hat (derangements), with $D_0=1$.

**A convolution.** Classify all $n!$ ways of returning the hats by the number $k$ of fans who get their own hat: choose those fans in $\binom nk$ ways, and the other $n-k$ fans must all get wrong hats, in $D_{n-k}$ ways. So

$$n!=\sum_{k=0}^{n}\binom nkD_{n-k}$$

**Exponential generating functions.** Let $D(z)=\sum_{n\ge0}D_n\frac{z^n}{n!}$. A binomial convolution $\sum_k\binom nka_kb_{n-k}$ corresponds to the product of the EGFs of $a$ and $b$. Here $a_k=1$ (EGF $e^z$) and $b_k=D_k$, and the left side $n!$ has EGF $\sum_nz^n=\frac{1}{1-z}$:

$$\frac{1}{1-z}=e^z\,D(z)\qquad\Longrightarrow\qquad D(z)=\frac{e^{-z}}{1-z}$$

**Extract the coefficients.** $\frac{1}{1-z}$ multiplies by partial sums: $\frac{e^{-z}}{1-z}=\sum_n\Big(\sum_{k=0}^{n}\frac{(-1)^k}{k!}\Big)z^n$. Comparing with $\sum_nD_n\frac{z^n}{n!}$:

$$D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}=n!\left(1-\frac1{1!}+\frac1{2!}-\cdots+\frac{(-1)^n}{n!}\right)$$

**Answer.** There are $D_n=n!\sum_{k=0}^{n}\frac{(-1)^k}{k!}$ ways, which is the integer nearest to $n!/e$ for $n\ge1$ (e.g. $D_4=9$, $D_5=44$). The probability that nobody gets his own hat is $D_n/n!\to e^{-1}\approx0.368$.
