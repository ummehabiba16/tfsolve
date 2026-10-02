---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For every second person: $J(1)=1$, $J(2n)=2J(n)-1$, $J(2n+1)=2J(n)+1$, so $J(2^m+l)=2l+1$ ($0\le l<2^m$). For every $q$-th person: $J_q(1)=1$, $J_q(n)=\big((J_q(n-1)+q-1)\bmod n\big)+1$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (the Josephus problem) and Ch. 3 (Josephus with every q-th person)']
---
**The problem.** $n$ people numbered $1,\dots,n$ stand in a circle; every second remaining person is eliminated, starting with person 2, until one survives. $J(n)$ is the survivor's number.

**Even number of people, $2n$.** In the first trip around the circle persons $2,4,\dots,2n$ are eliminated, and we are back at person 1 with $n$ people $1,3,5,\dots,2n-1$ left. This is the original problem for $n$ people, except that the person in position $k$ is now numbered $2k-1$. Hence

$$J(2n)=2J(n)-1\qquad(n\ge1)$$

**Odd number of people, $2n+1$.** After $2,4,\dots,2n$ are eliminated, person 1 is eliminated next, leaving $3,5,\dots,2n+1$: $n$ people, the one in position $k$ being numbered $2k+1$. Hence

$$J(2n+1)=2J(n)+1\qquad(n\ge1)$$

with $J(1)=1$.

**Closed form.** Tabulating $J(1),J(2),\dots=1,1,3,1,3,5,7,1,3,\dots$ suggests: writing $n=2^m+l$ with $0\le l<2^m$,

$$J(2^m+l)=2l+1$$

Proof by induction on $m$: for $m=0$, $l=0$ and $J(1)=1$. If $l$ is even, $J(2^m+l)=2J(2^{m-1}+l/2)-1=2(l+1)-1=2l+1$; if $l$ is odd, $J(2^m+l)=2J(2^{m-1}+(l-1)/2)+1=2l+1$. (In binary, $J(n)$ is $n$ rotated left by one bit.)

**Every $q$-th person eliminated.** Number positions from 0. After the first elimination (person $q$), counting restarts from the next person, so the problem becomes the same problem with $n-1$ people, shifted by $q$ places. This gives the general recurrence

$$J_q(1)=1,\qquad J_q(n)=\big((J_q(n-1)+q-1)\bmod n\big)+1$$

(For $q=2$ it agrees with the recurrences above, e.g. $J_2(10)=5$.)
