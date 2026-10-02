---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Pair consecutive terms: $(2k-1)-(2k+1)=-2$. For even $n$ the sum is $-2\cdot\frac n2=-n$; for odd $n$ it is $-(n-1)+(2n-1)=n$. So $\sum_{k=1}^{n}(-1)^{k+1}(2k-1)=(-1)^{n+1}n$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (manipulation of sums)']
---
$$S_n=\sum_{k=1}^{n}(-1)^{k+1}(2k-1)=1-3+5-7+\cdots+(-1)^{n+1}(2n-1)$$

**Pairing.** Group the terms in pairs $(1-3)+(5-7)+\cdots$; each pair is $(2k-1)-(2k+1)=-2$.

- $n$ even: there are $\frac n2$ pairs, so $S_n=-2\cdot\frac n2=-n$.
- $n$ odd: the first $n-1$ terms form $\frac{n-1}{2}$ pairs and the last term $+(2n-1)$ remains, so $S_n=-(n-1)+(2n-1)=n$.

$$\sum_{k=1}^{n}(-1)^{k+1}(2k-1)=(-1)^{n+1}\,n$$

**Check by the perturbation method.** $S_n+(-1)^{n+2}(2n+1)=1+\sum_{k=1}^{n}(-1)^{k+2}(2k+1)=1-S_n-2\sum_{k=1}^{n}(-1)^{k+1}$, and $\sum_{k=1}^{n}(-1)^{k+1}=\frac{1+(-1)^{n+1}}{2}$; solving gives $2S_n=(-1)^{n+1}(2n+1)+1-\big(1+(-1)^{n+1}\big)=(-1)^{n+1}2n$, the same answer. Values: $1,-2,3,-4,5,\dots$

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
