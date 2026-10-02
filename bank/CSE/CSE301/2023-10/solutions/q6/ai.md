---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$C_0=0$, $C_n=n+1+\frac1n\sum_{k=1}^{n}(C_{k-1}+C_{n-k})=n+1+\frac2n\sum_{k=0}^{n-1}C_k$ (average comparisons; pivot rank uniform). Solution $C_n=2(n+1)H_n-2n=\Theta(n\log n)$; worst case $T(n)=T(n-1)+\Theta(n)$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (summation factors: quicksort)']
---
**Model.** Quicksort on $n$ distinct keys picks a pivot, partitions the other keys into those smaller and those larger than the pivot, and sorts the two parts recursively. Let $C_n$ be the **average** number of comparisons when all $n!$ orderings of the input are equally likely.

- Partitioning around the pivot costs $n+1$ comparisons (the textbook count; $n-1$ in some versions).
- The pivot is equally likely to be the $k$-th smallest key, $k=1,\dots,n$ (probability $\frac1n$ each), leaving parts of sizes $k-1$ and $n-k$, which are again in random order.

**Recurrence.**

$$C_0=0,\qquad C_n=n+1+\frac1n\sum_{k=1}^{n}\big(C_{k-1}+C_{n-k}\big)\quad(n\ge1)$$

Since $\sum_{k=1}^{n}C_{k-1}=\sum_{k=1}^{n}C_{n-k}=\sum_{k=0}^{n-1}C_k$, this is

$$C_0=0,\qquad C_n=n+1+\frac2n\sum_{k=0}^{n-1}C_k\quad(n\ge1)$$

(For the running time $T(n)$ in general: $T(0)=T(1)=\Theta(1)$ and $T(n)=T(k-1)+T(n-k)+\Theta(n)$ when the pivot has rank $k$. The worst case, $k=1$ or $k=n$ every time, gives $T(n)=T(n-1)+\Theta(n)=\Theta(n^2)$; the best case, a median pivot, gives $T(n)=2T(n/2)+\Theta(n)=\Theta(n\log n)$.)

**Solution** (not required): multiplying by $n$ and subtracting the equation for $n-1$ gives $nC_n=(n+1)C_{n-1}+2n$; the summation factor $\frac{2}{n(n+1)}$ then gives $C_n=2(n+1)H_n-2n\approx2n\ln n$.
