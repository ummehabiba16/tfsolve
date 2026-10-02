---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\gcd(a_{n+1},a_n)=\gcd(3a_n+a_{n-1},a_n)=\gcd(a_{n-1},a_n)$, so by induction every pair of consecutive terms has $\gcd(a_1,a_0)=\gcd(9,6)=3$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (gcd and Euclid''s algorithm)']
---
**Key fact.** For integers $x,y$ and any integer $c$, $\gcd(x+cy,\ y)=\gcd(x,y)$: a number divides both $x+cy$ and $y$ exactly when it divides both $x$ and $y$. (This is the step used in Euclid's algorithm.)

**Claim.** $\gcd(a_{n+1},a_n)=3$ for every $n\ge0$.

**Proof by induction on $n$.**

- Base case: $\gcd(a_1,a_0)=\gcd(9,6)=3$.
- Induction step: using $a_{n+1}=3a_n+a_{n-1}$ and the key fact with $c=3$,

$$\gcd(a_{n+1},a_n)=\gcd(3a_n+a_{n-1},\ a_n)=\gcd(a_{n-1},\ a_n)=3$$

by the induction hypothesis. $\blacksquare$

**Check.** The sequence is $6, 9, 33, 108, 357, 1179,\dots$; e.g. $\gcd(33,108)=3$ and $\gcd(108,357)=3$.

(Every term is a multiple of 3, since $a_0$ and $a_1$ are and the recurrence preserves this. Dividing by 3 gives $2,3,11,36,119,\dots$, consecutive terms of which are coprime by the same argument.)
