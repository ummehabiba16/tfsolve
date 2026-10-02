---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For $2\le k\le n$, $k\mid n!$, so $k\mid n!+k$ and $n!+k>k$: each of the $n-1$ numbers $n!+2,n!+3,\dots,n!+n$ is composite.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (primes; factorial factors)']
---
**Claim.** For every positive integer $n$, the $n-1$ consecutive integers

$$n!+2,\quad n!+3,\quad\dots,\quad n!+n$$

(which lie between $n!$ and $n!+n$) are all composite.

**Proof.** Take any $k$ with $2\le k\le n$. Since $k$ is one of the factors of $n!=1\cdot2\cdots n$, we have $k\mid n!$, and therefore

$$k\mid n!+k$$

Moreover $1<k<n!+k$ (as $n!\ge1$), so $k$ is a proper divisor of $n!+k$ and $n!+k$ is composite. This holds for each of the $n-1$ values $k=2,3,\dots,n$, so there are at least $n-1$ composite integers between $n!$ and $n!+n$. (For $n=1$ the claim, "at least 0", is trivial.) $\blacksquare$

**Example.** $n=5$: $122=2\cdot61$, $123=3\cdot41$, $124=4\cdot31$, $125=5\cdot25$. This shows that there are arbitrarily long gaps between consecutive primes.
