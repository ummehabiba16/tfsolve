---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For consecutive fractions $\frac mn<\frac{m''}{n''}$ in the Stern-Brocot construction, $m''n-mn''=1$. Then $m''n+1=(mn''+1)+1$: numerator and denominator are consecutive integers, so $\gcd(m''n+1,\ mn''+1)=1$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 4 (the Stern-Brocot tree)']
---
We read the first fraction as $\frac mn$ (printed $\frac mm$).


**Construction.** The Stern-Brocot tree starts from the two fractions $\frac01$ and $\frac10$ and repeatedly inserts, between two neighbouring fractions $\frac mn$ and $\frac{m'}{n'}$, their mediant $\frac{m+m'}{n+n'}$.

**Invariant.** If $\frac mn<\frac{m'}{n'}$ are neighbours at any stage of the construction, then

$$m'n-mn'=1$$

*Proof by induction on the stages.* Initially the only neighbours are $\frac01$ and $\frac10$, and $1\cdot1-0\cdot0=1$. Suppose the invariant holds for the neighbours $\frac mn<\frac{m'}{n'}$, and we insert the mediant between them. The two new pairs of neighbours are $\frac mn,\frac{m+m'}{n+n'}$ and $\frac{m+m'}{n+n'},\frac{m'}{n'}$:

$$(m+m')\,n-m\,(n+n')=m'n-mn'=1$$

$$m'\,(n+n')-(m+m')\,n'=m'n-mn'=1$$

Every other pair of neighbours is unchanged, so the invariant holds at the next stage too. $\blacksquare$

**The fraction $\frac{m'n+1}{mn'+1}$.** By the invariant, $m'n=mn'+1$, so

$$m'n+1=(mn'+1)+1$$

The numerator and denominator are consecutive integers. Any common divisor $d$ of them divides their difference, which is 1. So

$$\gcd(m'n+1,\ mn'+1)=1$$

and $\frac{m'n+1}{mn'+1}$ is in lowest terms. $\blacksquare$ (If the two fractions are taken in the other order, $mn'-m'n=1$ and the denominator exceeds the numerator by 1 instead; the conclusion is the same.)

**Example.** $\frac12$ and $\frac23$ are consecutive at the third level ($m=1$, $n=2$, $m'=2$, $n'=3$): $\frac{m'n+1}{mn'+1}=\frac{5}{4}$, in lowest terms.
