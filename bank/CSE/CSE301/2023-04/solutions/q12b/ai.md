---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$p^3=q^2-1=(q-1)(q+1)$. $q=2$ fails ($p^3=3$), so $q$ is odd and $q\pm1$ are both even, making $p^3$ even: $p=2$, $q^2=9$, $q=3$. Only solution: $p=2$, $q=3$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (primes, factorization)']
---
Rewrite the equation as

$$p^3=q^2-1=(q-1)(q+1)$$

**Case $q=2$.** Then $p^3=3$, which has no integer solution.

**Case $q$ odd.** Then $q-1$ and $q+1$ are both even, so $4\mid(q-1)(q+1)=p^3$. Hence $p^3$ is even, so the prime $p$ is $2$. Then $q^2=2^3+1=9$, so $q=3$, which is prime.

**Answer.** The only solution is $p=2$, $q=3$: $2^3+1=9=3^2$.

(Alternative argument: since $p$ is prime and $(q-1)(q+1)=p^3$, both factors are powers of $p$, $q-1=p^a$ and $q+1=p^b$ with $a<b$, $a+b=3$. Then $p^b-p^a=2$; $(a,b)=(0,3)$ gives $p^3=3$, impossible, and $(a,b)=(1,2)$ gives $p(p-1)=2$, so $p=2$, $q=3$.)

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
