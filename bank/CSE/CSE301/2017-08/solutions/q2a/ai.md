---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$C_n=n+1+\frac2n\sum_{k<n}C_k$ gives $nC_n=(n+1)C_{n-1}+2n$; the summation factor $\frac{2}{n(n+1)}$ turns it into $\frac{C_n}{n+1}=\frac{C_{n-1}}{n}+\frac{2}{n+1}$, so $C_n=2(n+1)H_n-2n\approx2n\ln n=O(n\log n)$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (summation factors: quicksort)']
---
**Recurrence.** Let $C_n$ be the average number of comparisons quicksort makes on $n$ distinct keys in random order. Partitioning around the pivot costs $n+1$ comparisons (the textbook model), and the pivot is equally likely to be the $k$-th smallest for each $k$, leaving subproblems of sizes $k-1$ and $n-k$:

$$C_0=0,\qquad C_n=n+1+\frac1n\sum_{k=1}^{n}\big(C_{k-1}+C_{n-k}\big)=n+1+\frac2n\sum_{k=0}^{n-1}C_k\quad(n\ge1)$$

**Remove the sum.** Multiply by $n$ and subtract the same equation for $n-1$:

$$nC_n-(n-1)C_{n-1}=2n+2C_{n-1}\ \Rightarrow\ nC_n=(n+1)C_{n-1}+2n\qquad(n\ge2)$$

(it also holds for $n=1$, since $C_1=2$).

**Summation factor.** This has the form $a_nT_n=b_nT_{n-1}+c_n$ with $a_n=n$, $b_n=n+1$, $c_n=2n$. The summation factor is

$$s_n=\frac{a_{n-1}a_{n-2}\cdots a_1}{b_nb_{n-1}\cdots b_2}=\frac{(n-1)!}{(n+1)!/2}=\frac{2}{n(n+1)}$$

Multiplying the recurrence by $s_n$ gives a telescoping form:

$$\frac{C_n}{n+1}=\frac{C_{n-1}}{n}+\frac{2}{n+1}$$

$$\frac{C_n}{n+1}=\sum_{k=1}^{n}\frac{2}{k+1}=2\big(H_{n+1}-1\big)$$

$$C_n=2(n+1)H_{n+1}-2(n+1)=2(n+1)H_n-2n$$

**Average case complexity.** Since $H_n=\ln n+\gamma+O(1/n)$,

$$C_n=2n\ln n-(4-2\gamma)n+O(\log n)\approx1.39\,n\log_2n=\Theta(n\log n)$$

(If partitioning is counted as $n-1$ comparisons instead, the same steps give $C_n=2(n+1)H_n-4n$, also $\Theta(n\log n)$.)
