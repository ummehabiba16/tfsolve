---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\prod_{k\ge1}(1+x^k)=\prod_{k\ge1}\frac{1-x^{2k}}{1-x^k}=\prod_{k\text{ odd}}\frac{1}{1-x^k}$; the left side generates partitions into distinct parts and the right side partitions into odd parts, so the counts are equal for every $n$ (bijection: merge equal odd parts using binary).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 7 (generating functions for partitions)', 'Brualdi, Introductory Combinatorics, Ch. 8 (partitions of numbers)']
---
Let $D(n)$ be the number of partitions of $n$ into **distinct** parts and $O(n)$ the number of partitions of $n$ into **odd** parts.

**Generating function for distinct parts.** Each integer $k\ge1$ is either used once or not at all, contributing a factor $1+x^k$ (the exponent records how much $k$ contributes to the total). Multiplying over all $k$, the coefficient of $x^n$ counts the ways of writing $n$ as a sum of distinct parts:

$$\sum_{n\ge0}D(n)x^n=\prod_{k\ge1}\left(1+x^k\right)=(1+x)(1+x^2)(1+x^3)\cdots$$

**Generating function for odd parts.** Each odd integer $k$ may be used any number of times $j\ge0$, contributing $1+x^k+x^{2k}+\cdots=\frac{1}{1-x^k}$:

$$\sum_{n\ge0}O(n)x^n=\prod_{k\text{ odd}}\frac{1}{1-x^k}=\frac{1}{(1-x)(1-x^3)(1-x^5)\cdots}$$

**The two products are equal.** Since $1+x^k=\frac{1-x^{2k}}{1-x^k}$,

$$\prod_{k\ge1}\left(1+x^k\right)=\prod_{k\ge1}\frac{1-x^{2k}}{1-x^k}=\frac{(1-x^2)(1-x^4)(1-x^6)\cdots}{(1-x)(1-x^2)(1-x^3)(1-x^4)\cdots}$$

Every factor $1-x^{\text{even}}$ in the numerator cancels the same factor in the denominator, leaving only the odd exponents in the denominator:

$$\prod_{k\ge1}\left(1+x^k\right)=\prod_{k\text{ odd}}\frac{1}{1-x^k}$$

(All the products converge as formal power series, since only finitely many factors affect each coefficient.) Two equal power series have equal coefficients, so $D(n)=O(n)$ for every $n$. $\blacksquare$

**A bijection (Glaisher).** Given a partition into odd parts, in which the odd part $k$ occurs $j$ times, write $j$ in binary, $j=2^{a_1}+2^{a_2}+\cdots$, and replace the $j$ copies of $k$ by the distinct parts $2^{a_1}k,\ 2^{a_2}k,\dots$ The result has distinct parts, and the process can be reversed (split each part into its odd part times a power of 2), so it is a one-to-one correspondence. Example: $3+3+3+1=3\cdot(2+1)+1\mapsto6+3+1$.

**Example $n=6$.** Distinct parts: $6,\ 5+1,\ 4+2,\ 3+2+1$. Odd parts: $5+1,\ 3+3,\ 3+1+1+1,\ 1+1+1+1+1+1$. Four each.
