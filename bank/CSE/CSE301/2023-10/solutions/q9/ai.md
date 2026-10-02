---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Let $I(n)$ be the survivor. $I(1)=1$; $I(2n)=2I(n)$; $I(2n+1)=2I(n)+2$ if $I(n)<n$, and $I(2n+1)=2$ if $I(n)=n$. (Closed form: $I(2^m+l)=2l$ for $0<l<2^m$ and $I(2^m)=2^m$, e.g. $I(10)=4$.)'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (the Josephus problem)']
---
Let $I(n)$ be the number of the survivor when the first person of each consecutive pair is eliminated, starting with person 1 (so persons $1,3,5,\dots$ go first).

**Base case.** $I(1)=1$.

**Even number of people, $2n$.** In the first trip around the circle persons $1,3,5,\dots,2n-1$ are eliminated. We are left with the $n$ persons $2,4,\dots,2n$, and the next pair to be considered starts with person 2. This is the same problem for $n$ people, except that the person in position $k$ now has number $2k$:

$$I(2n)=2I(n)\qquad(n\ge1)$$

**Odd number of people, $2n+1$.** The first trip eliminates $1,3,\dots,2n-1$, and then person $2n+1$ is the first of the pair $(2n+1,\,2)$, so he is eliminated too. The $n$ survivors are $2,4,\dots,2n$, and the next pair starts with person 4. In the new circle, position $k$ ($1\le k\le n-1$) is person $2k+2$, and position $n$ is person 2. So

$$I(2n+1)=\begin{cases}2I(n)+2,&\text{if }I(n)<n\\2,&\text{if }I(n)=n\end{cases}\qquad(n\ge1)$$

(compactly, $I(2n+1)=\big((2I(n)+1)\bmod2n\big)+1$).

**Check with $n=10$.** $I(10)=2I(5)$, $I(2)=2I(1)=2$, and $I(5)=I(2\cdot2+1)=2$ because $I(2)=2$ equals the number of people (2). Hence $I(10)=2\cdot2=4$, matching the elimination order $1,3,5,7,9,2,6,10,8$ and survivor 4 given in the question.

**Closed form** (not required). The table $I(1),\dots,I(12)=1,2,2,4,2,4,6,8,2,4,6,8$ suggests, for $n=2^m+l$ with $0\le l<2^m$,

$$I(2^m+l)=\begin{cases}2l,&0<l<2^m\\2^m,&l=0\end{cases}$$

This is the classical $J(n)=2l+1$ shifted back by one position (here person $n$ plays the role of the first person skipped), and a simulation for all $n<300$ agrees with both the recurrences and the closed form.
