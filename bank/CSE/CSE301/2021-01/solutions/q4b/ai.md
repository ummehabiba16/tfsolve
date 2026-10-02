---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The coefficient of $x^n$ counts solutions of $e_1+e_2+e_3+e_4=n$ with $0\le e_1\le2$, $e_2\in\{0,2,4,6\}$, $e_3$ even, $e_4\ge1$: e.g. the number of ways to buy $n$ fruits with at most 2 apples, an even number (at most 6) of bananas, an even number of oranges and at least one pear.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 7 (generating functions)']
---
**Reading the factors.** In a product of generating functions, the coefficient of $x^n$ counts the ways of writing $n=e_1+e_2+e_3+e_4$, where $e_i$ is an exponent taken from the $i$-th factor:

| Factor | Allowed values of $e_i$ |
|:--|:--|
| $1+x+x^2$ | $e_1\in\{0,1,2\}$ |
| $1+x^2+x^4+x^6$ | $e_2\in\{0,2,4,6\}$ |
| $1+x^2+x^4+\cdots$ | $e_3$ any even number $\ge0$ |
| $x+x^2+x^3+\cdots$ | $e_4\ge1$ |

**A combinatorial problem.** *A fruit basket is to contain $n$ pieces of fruit, chosen from apples, bananas, oranges and pears (fruits of one kind are identical). The basket may contain at most 2 apples, an even number of bananas but no more than 6, an even number of oranges, and at least one pear. In how many ways can the basket be filled?*

With $e_1,e_2,e_3,e_4$ the numbers of apples, bananas, oranges and pears, the answer $a_n$ is the coefficient of $x^n$ in

$$(1+x+x^2)(1+x^2+x^4+x^6)(1+x^2+x^4+\cdots)(x+x^2+x^3+\cdots)$$

(Equivalently: the number of non-negative integer solutions of $e_1+e_2+e_3+e_4=n$ with these restrictions, or ways to distribute $n$ identical balls into four distinct boxes with these capacities.) In closed form the generating function is

$$\frac{x\,(1+x+x^2)(1-x^8)}{(1-x)(1-x^2)^2}$$

Expanding, $a_1,a_2,\dots,a_6=1,2,5,7,12,15$; for instance $a_2=2$: two pears, or one apple and one pear.
