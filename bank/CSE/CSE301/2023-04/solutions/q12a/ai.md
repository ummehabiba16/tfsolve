---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Induction over the construction: the starting neighbours $\frac01,\frac10$ give $1\cdot1-0\cdot0=1$; inserting the mediant $\frac{m+m''}{n+n''}$ between neighbours with $m''n-mn''=1$ gives $(m+m'')n-m(n+n'')=1$ and $m''(n+n'')-(m+m'')n''=1$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (the Stern-Brocot tree, equation (4.31))']
---
**Construction.** The Stern-Brocot tree starts from the two fractions $\frac01$ and $\frac10$ and repeatedly inserts, between two neighbouring fractions $\frac mn$ and $\frac{m'}{n'}$, their mediant $\frac{m+m'}{n+n'}$.

**Invariant.** If $\frac mn<\frac{m'}{n'}$ are neighbours at any stage of the construction, then

$$m'n-mn'=1$$

*Proof by induction on the stages.* Initially the only neighbours are $\frac01$ and $\frac10$, and $1\cdot1-0\cdot0=1$. Suppose the invariant holds for the neighbours $\frac mn<\frac{m'}{n'}$, and we insert the mediant between them. The two new pairs of neighbours are $\frac mn,\frac{m+m'}{n+n'}$ and $\frac{m+m'}{n+n'},\frac{m'}{n'}$:

$$(m+m')\,n-m\,(n+n')=m'n-mn'=1$$

$$m'\,(n+n')-(m+m')\,n'=m'n-mn'=1$$

Every other pair of neighbours is unchanged, so the invariant holds at the next stage too. $\blacksquare$

This proves $m'n-mn'=1$ for any two consecutive fractions $\frac mn<\frac{m'}{n'}$ at every stage. (A consequence: every fraction in the tree is in lowest terms, since a common divisor of $m$ and $n$ would divide $m'n-mn'=1$.)

**Example.** At the stage $\frac01,\frac13,\frac12,\frac23,\frac11,\dots$: for $\frac13,\frac12$: $1\cdot3-1\cdot2=1$; for $\frac12,\frac23$: $2\cdot2-1\cdot3=1$.

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
