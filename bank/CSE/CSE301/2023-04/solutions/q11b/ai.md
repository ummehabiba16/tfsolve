---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\frac{1}{n(n+k)}=\frac1k\left(\frac1n-\frac{1}{n+k}\right)$; the partial sums telescope to $\frac1k\big(H_k-(H_{N+k}-H_N)\big)\to\frac{H_k}{k}$ since $H_{N+k}-H_N\le\frac{k}{N+1}\to0$. So $\sum_{n\ge1}\frac{1}{n(n+k)}=\frac{H_k}{k}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (telescoping, harmonic numbers)']
---
**Partial fractions.**

$$\frac{1}{n(n+k)}=\frac1k\left(\frac1n-\frac{1}{n+k}\right)$$

**Partial sums.** For $N\ge k$,

$$\sum_{n=1}^{N}\left(\frac1n-\frac{1}{n+k}\right)=\sum_{n=1}^{N}\frac1n-\sum_{n=k+1}^{N+k}\frac1n=H_N-\big(H_{N+k}-H_k\big)=H_k-\big(H_{N+k}-H_N\big)$$

**Limit.** $H_{N+k}-H_N=\frac{1}{N+1}+\cdots+\frac{1}{N+k}\le\frac{k}{N+1}\to0$ as $N\to\infty$. Hence

$$\sum_{n=1}^{\infty}\frac{1}{n(n+k)}=\frac{1}{k}\lim_{N\to\infty}\Big(H_k-\big(H_{N+k}-H_N\big)\Big)=\frac{H_k}{k}$$

**Check.** $k=1$: $\sum\frac{1}{n(n+1)}=1=\frac{H_1}{1}$. $k=2$: $\frac{H_2}{2}=\frac34$ (numerically $\frac{1}{3}+\frac18+\frac1{15}+\cdots=0.75$).

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
