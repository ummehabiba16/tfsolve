---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The $k$-th term is $\frac{2k-1}{2^kk!}=\frac{1}{2^{k-1}(k-1)!}-\frac{1}{2^kk!}$, so the sum telescopes: $\sum_{k=1}^{n}=1-\frac{1}{2^nn!}=1-\frac{1}{2\cdot4\cdot6\cdots(2n)}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (telescoping sums)']
---
**General term.** The $k$-th term has numerator $2k-1$ and denominator $2\times4\times6\times\cdots\times(2k)=2^kk!$:

$$t_k=\frac{2k-1}{2\cdot4\cdots(2k)}=\frac{2k-1}{2^k\,k!}$$

**Telescoping.** Since $\frac{1}{2^{k-1}(k-1)!}=\frac{2k}{2^kk!}$,

$$\frac{1}{2^{k-1}(k-1)!}-\frac{1}{2^kk!}=\frac{2k}{2^kk!}-\frac{1}{2^kk!}=\frac{2k-1}{2^kk!}=t_k$$

So with $u_k=\frac{1}{2^kk!}$ we have $t_k=u_{k-1}-u_k$, and

$$\sum_{k=1}^{n}t_k=\sum_{k=1}^{n}\left(u_{k-1}-u_k\right)=u_0-u_n=1-\frac{1}{2^nn!}$$

$$\frac12+\frac{3}{2\times4}+\frac{5}{2\times4\times6}+\cdots\ (n\text{ terms})=1-\frac{1}{2\times4\times6\times\cdots\times(2n)}$$

**Check.** $n=1$: $\frac12=1-\frac12$. $n=2$: $\frac12+\frac38=\frac78=1-\frac18$. $n=3$: $\frac78+\frac{5}{48}=\frac{47}{48}=1-\frac{1}{48}$. (As $n\to\infty$ the sum tends to 1.)
