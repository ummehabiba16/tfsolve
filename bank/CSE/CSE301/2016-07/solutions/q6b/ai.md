---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Condition on the last vote: $P_{n,m}=\frac{n}{n+m}P_{n-1,m}+\frac{m}{n+m}P_{n,m-1}$; induction on $n+m$ gives $P_{n,m}=\frac{n-m}{n+m}$ (also by the reflection argument: bad orderings are twice those starting with a B vote, $2m/(n+m)$).'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing probabilities by conditioning: the ballot problem)']
---
Let $P_{n,m}$ be the probability that $A$ is always strictly ahead during the count when $A$ gets $n$ votes, $B$ gets $m$ votes and $n>m$ (all $\binom{n+m}{n}$ orderings equally likely). We prove $P_{n,m}=\frac{n-m}{n+m}$ by induction on $n+m$. It is convenient to allow $n=m$, where $P_{m,m}=0$ (at the end the count is tied), which also agrees with the formula.

**Base case.** $m=0$: $A$ gets every vote, so $P_{n,0}=1=\frac{n-0}{n+0}$. In particular $P_{1,0}=1$ ($n+m=1$).

**Conditioning on the last vote.** The last vote counted is for $A$ with probability $\frac{n}{n+m}$ and for $B$ with probability $\frac{m}{n+m}$. Given the last vote, the first $n+m-1$ votes are a uniformly random ordering of the remaining votes. Since $n>m$, $A$ is ahead after the last vote anyway, so $A$ is always ahead if and only if $A$ was always ahead during the first $n+m-1$ votes:

$$P_{n,m}=\frac{n}{n+m}P_{n-1,m}+\frac{m}{n+m}P_{n,m-1}$$

**Induction step.** Assume the formula for all pairs with total $n+m-1$ (with $n-1\ge m$). Then

$$P_{n,m}=\frac{n}{n+m}\cdot\frac{n-1-m}{n+m-1}+\frac{m}{n+m}\cdot\frac{n-m+1}{n+m-1}$$

$$=\frac{n^2-n-nm+mn-m^2+m}{(n+m)(n+m-1)}=\frac{(n^2-m^2)-(n-m)}{(n+m)(n+m-1)}$$

$$=\frac{(n-m)(n+m-1)}{(n+m)(n+m-1)}=\frac{n-m}{n+m}$$

which completes the induction.

**Alternative (reflection) argument.** Call an ordering *bad* if the count is tied at some point. Every ordering whose first vote is for $B$ is bad (A is behind at once). For a bad ordering that starts with an $A$ vote, swap the $A$ and $B$ labels of all votes up to the first tie: this gives a bad ordering starting with $B$, and the map is a bijection. So bad orderings are twice as many as those starting with $B$:

$$P(\text{bad})=2\cdot\frac{m}{n+m},\qquad P(A\text{ always ahead})=1-\frac{2m}{n+m}=\frac{n-m}{n+m}$$
