---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(a) $P(G=2)=p^2+q^2$, $P(G=3)=2pq$, so $E[G]=2+2pq$. (b) $P(G=3)=p^3+q^3$, $P(G=4)=3pq(p^2+q^2)$, $P(G=5)=6p^2q^2$, so $E[G]=3+3pq+6p^2q^2$ (with $q=1-p$).'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations; the series of games)']
---
Let $q=1-p$ and let $G$ be the number of games played.

**(a) $i=2$ (first to win 2 games).** The series lasts 2 games if one team wins both ($p^2+q^2$); otherwise the first two games are split ($2pq$) and a third game decides it:

$$P(G=2)=p^2+q^2,\qquad P(G=3)=2pq$$

$$E[G]=2(p^2+q^2)+3\cdot2pq=2(p^2+2pq+q^2)+2pq=2+2pq$$

**(b) $i=3$ (first to win 3 games).**

- $G=3$: one team wins the first three games: $p^3+q^3$.
- $G=4$: a team has exactly 2 wins in the first 3 games and wins game 4: $\binom32p^3q+\binom32q^3p=3pq(p^2+q^2)$.
- $G=5$: the first 4 games are split $2$-$2$: $\binom42p^2q^2=6p^2q^2$.

$$E[G]=3(p^3+q^3)+12pq(p^2+q^2)+30p^2q^2$$

With $s=pq$, $p^2+q^2=1-2s$ and $p^3+q^3=(p+q)^3-3pq(p+q)=1-3s$, so

$$E[G]=3(1-3s)+12s(1-2s)+30s^2=3+3pq+6p^2q^2$$

**Check $p=\frac12$:** (a) $2+\frac12=2.5$; (b) $3+\frac34+\frac38=\frac{33}{8}=4.125$ (directly: $3\cdot\frac14+4\cdot\frac38+5\cdot\frac38=\frac{33}{8}$).
