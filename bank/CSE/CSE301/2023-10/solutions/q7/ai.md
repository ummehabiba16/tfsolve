---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Euclid: if $p_1,\dots,p_k$ were all the primes, $N=p_1p_2\cdots p_k+1>1$ would have a prime factor $p$; $p$ is not any $p_i$ because $N\bmod p_i=1$. Contradiction, so there are infinitely many primes.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (primes, Euclid''s proof)']
---
**Proof (Euclid).** Suppose, for contradiction, that there are only finitely many primes, $p_1,p_2,\dots,p_k$. Consider

$$N=p_1p_2\cdots p_k+1$$

- $N>1$, so $N$ has at least one prime factor $p$ (its smallest divisor greater than 1 is prime).
- For each $i$, $N=p_i\cdot\big(\prod_{j\ne i}p_j\big)+1$, so $N\bmod p_i=1$ and $p_i\nmid N$.

Hence $p$ is a prime that is not in the list $p_1,\dots,p_k$, contradicting the assumption that the list contains all primes. Therefore there are infinitely many primes. $\blacksquare$

(Note that $N$ itself need not be prime: $2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\times509$. The argument only needs some prime factor of $N$ outside the list.)

**Variant (Euclid numbers).** $e_1=2$ and $e_n=e_1e_2\cdots e_{n-1}+1$ gives $2,3,7,43,1807,\dots$; any two of them are relatively prime, so their prime factors are all different, and they produce infinitely many primes.
