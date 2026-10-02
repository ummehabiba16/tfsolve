---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Coprimality to $m^k$ is the same as coprimality to $m$, and depends only on the residue mod $m$. The range $1,\dots,m^k$ consists of $m^{k-1}$ blocks of $m$ consecutive integers, each containing exactly $\varphi(m)$ integers coprime to $m$; so $\phi(m^k)=m^{k-1}\phi(m)$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (phi and mu)', 'Supplementary materials (Euler''s totient function)']
---
**Two facts.**

1. An integer $a$ is relatively prime to $m^k$ iff it is relatively prime to $m$ ($m$ and $m^k$ have the same prime divisors).
2. Whether $a\perp m$ depends only on $a\bmod m$, since $\gcd(a,m)=\gcd(a\bmod m,\ m)$.

**Counting.** $\phi(m^k)$ counts the integers $a$ with $1\le a\le m^k$ and $a\perp m^k$, i.e. (fact 1) $a\perp m$. Split $1,2,\dots,m^k$ into $m^{k-1}$ consecutive blocks of length $m$:

$$\{1,\dots,m\},\ \{m+1,\dots,2m\},\ \dots,\ \{m^k-m+1,\dots,m^k\}$$

Each block contains every residue modulo $m$ exactly once, so (fact 2) each block contains exactly $\phi(m)$ integers relatively prime to $m$. Therefore

$$\phi(m^k)=m^{k-1}\cdot\phi(m)\qquad\blacksquare$$

**Alternative (product formula).** $\phi(N)=N\prod_{p\mid N}\left(1-\frac1p\right)$ and $m^k$ has the same primes as $m$, so $\phi(m^k)=m^k\prod_{p\mid m}\left(1-\frac1p\right)=m^{k-1}\cdot m\prod_{p\mid m}\left(1-\frac1p\right)=m^{k-1}\phi(m)$.

**Example.** $\phi(6^2)=\phi(36)=12=6\cdot\phi(6)=6\cdot2$.
