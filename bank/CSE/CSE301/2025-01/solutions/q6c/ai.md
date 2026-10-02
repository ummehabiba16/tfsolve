---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Neighbours $\frac mn<\frac{m''}{n''}$ always satisfy $m''n-mn''=1$ (true for $\frac01,\frac10$ and preserved when a mediant is inserted). For the mediant, $(m+m'')n-m(n+n'')=1$, so any common divisor of $m+m''$ and $n+n''$ divides 1: the mediant is in lowest terms.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (the Stern-Brocot tree)']
---
**Construction.** The Stern-Brocot tree starts from the two fractions $\frac01$ and $\frac10$ and repeatedly inserts, between two neighbouring fractions $\frac mn$ and $\frac{m'}{n'}$, their mediant $\frac{m+m'}{n+n'}$.

**Invariant.** If $\frac mn<\frac{m'}{n'}$ are neighbours at any stage of the construction, then

$$m'n-mn'=1$$

*Proof by induction on the stages.* Initially the only neighbours are $\frac01$ and $\frac10$, and $1\cdot1-0\cdot0=1$. Suppose the invariant holds for the neighbours $\frac mn<\frac{m'}{n'}$, and we insert the mediant between them. The two new pairs of neighbours are $\frac mn,\frac{m+m'}{n+n'}$ and $\frac{m+m'}{n+n'},\frac{m'}{n'}$:

$$(m+m')\,n-m\,(n+n')=m'n-mn'=1$$

$$m'\,(n+n')-(m+m')\,n'=m'n-mn'=1$$

Every other pair of neighbours is unchanged, so the invariant holds at the next stage too. $\blacksquare$

**Mediants are in lowest terms.** A new fraction $\frac{m+m'}{n+n'}$ is created between neighbours $\frac mn<\frac{m'}{n'}$, which satisfy the invariant. Then

$$(m+m')\cdot n-m\cdot(n+n')=m'n-mn'=1$$

Any common divisor $d$ of $m+m'$ and $n+n'$ divides the left side, hence divides 1. So $\gcd(m+m',\ n+n')=1$, i.e. $(m+m')\perp(n+n')$, and the mediant is already in lowest terms when it appears. $\blacksquare$

(Example: between $\frac12$ and $\frac23$ the tree inserts $\frac35$; the pair $\frac12,\frac23$ satisfies $2\cdot2-1\cdot3=1$, and $\gcd(3,5)=1$.)
