---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Inserting $n$ into a permutation of $n-1$ letters at $j$ places from the right creates exactly $j$ new inversions ($0\le j\le n-1$), so $b(n,k)=\sum_{j=0}^{n-1}b(n-1,k-j)$ ($=b(n-1,k)+\cdots+b(n-1,0)$ when $k\le n-1$), with $b(1,0)=1$ and $b(n,k)=0$ for $k<0$. Then $B_n(x)=(1+x+\cdots+x^{n-1})B_{n-1}(x)$ and $B_1=1$ give $B_n(x)=(1+x)(1+x+x^2)\cdots(1+\cdots+x^{n-1})$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (generating functions; inversions)', 'Brualdi, Introductory Combinatorics, Ch. 4 (inversions of permutations)']
---
**The recurrence.** Every permutation $P$ of $\{1,\dots,n\}$ is obtained in exactly one way by inserting the largest letter $n$ into a permutation $P'$ of $\{1,\dots,n-1\}$. Since $n$ is larger than every other letter, it forms an inversion exactly with the letters to its right. If $n$ is inserted with $j$ letters to its right ($j=0,1,\dots,n-1$), then

$$\text{inv}(P)=\text{inv}(P')+j$$

and inversions among the other letters are unchanged. So $P$ has $k$ inversions exactly when $P'$ has $k-j$:

$$b(n,k)=\sum_{j=0}^{n-1}b(n-1,k-j)=b(n-1,k)+b(n-1,k-1)+\cdots+b(n-1,k-n+1)$$

where $b(n-1,i)=0$ for $i<0$. When $k\le n-1$ the last non-zero term is $b(n-1,0)$, which is the form printed in the question.

**Base cases.** $b(1,0)=1$ (the permutation "1" has no inversions) and $b(1,k)=0$ for $k\ne0$; also $b(n,k)=0$ for $k<0$ or $k>\binom n2$, and $b(n,0)=1$ (only the identity has no inversions).

**The generating function.** Let $B_n(x)=\sum_kb(n,k)x^k$. Multiply the recurrence by $x^k$ and sum over $k$:

$$B_n(x)=\sum_k\sum_{j=0}^{n-1}b(n-1,k-j)x^{k}=\sum_{j=0}^{n-1}x^j\sum_kb(n-1,k-j)x^{k-j}=\left(1+x+\cdots+x^{n-1}\right)B_{n-1}(x)$$

Starting from $B_1(x)=1$ and applying this repeatedly,

$$B_n(x)=(1+x)(1+x+x^2)(1+x+x^2+x^3)\cdots(1+x+\cdots+x^{n-1})$$

**Check.** $B_3(x)=(1+x)(1+x+x^2)=1+2x+2x^2+x^3$: of the 6 permutations of $\{1,2,3\}$, one has 0 inversions (123), two have 1 (132, 213), two have 2 (231, 312) and one has 3 (321). (The example in the question, $\{5,3,4,1,2\}$, indeed has 8 inversions; a computer check of all permutations for $n\le6$ confirms the product formula.)
