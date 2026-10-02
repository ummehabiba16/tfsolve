---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The number $X$ of the 52 ticket holders who show up is $\text{Bin}(52,\ 0.95)$; there is a seat for everyone iff $X\le50$: $P=1-P(X=51)-P(X=52)=1-52(0.95)^{51}(0.05)-(0.95)^{52}\approx1-0.1901-0.0694=0.7405$.'
sources: ['Ross, Introduction to Probability Models, Ch. 2 (binomial random variables)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 3-4']
---
Each of the 52 ticket holders shows up with probability $0.95$, independently (5% do not show up). So the number who show up is

$$X\sim\text{Bin}(52,\ 0.95)$$

The plane holds 50 passengers, so everyone who shows up gets a seat exactly when $X\le50$:

$$P(X\le50)=1-P(X=51)-P(X=52)$$

$$P(X=51)=\binom{52}{51}(0.95)^{51}(0.05)=52(0.95)^{51}(0.05)\approx0.1901$$

$$P(X=52)=(0.95)^{52}\approx0.0694$$

$$P(\text{a seat for every passenger who shows up})\approx1-0.1901-0.0694=\mathbf{0.7405}$$

(The Poisson approximation for the number of no-shows, $\text{Pois}(52\times0.05=2.6)$, gives $P(\text{at least 2 no-shows})=1-e^{-2.6}(1+2.6)\approx0.733$, close to the exact value.)
