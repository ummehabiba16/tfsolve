---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The diagonal sums are $s_n=\sum_{k\ge0}\binom{n-k}{k}$; Pascal''s rule gives $s_n=s_{n-1}+s_{n-2}$ with $s_0=s_1=1$, so $s_n=F_{n+1}$ (e.g. $\binom40+\binom31+\binom22=5=F_5$).'
sources: ['Brualdi, Introductory Combinatorics, Ch. 7 (Fibonacci numbers and Pascal''s triangle)', 'Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 5-6']
---
**The diagonals.** Write Pascal's triangle left-justified, with $\binom nk$ in row $n$, column $k$. The diagonal that starts at $\binom n0$ in the left column and runs upward to the right contains $\binom n0,\binom{n-1}{1},\binom{n-2}{2},\dots$ Its sum is

$$s_n=\sum_{k\ge0}\binom{n-k}{k}=\binom n0+\binom{n-1}{1}+\binom{n-2}{2}+\cdots$$

(the terms with $k>n-k$ are zero). For example

$$s_0=1,\quad s_1=1,\quad s_2=1+1=2,\quad s_3=1+2=3,\quad s_4=1+3+1=5,\quad s_5=1+4+3=8$$

**Claim:** $s_n=F_{n+1}$, where $F_1=F_2=1$ and $F_{m}=F_{m-1}+F_{m-2}$.

**Proof.** $s_0=1=F_1$ and $s_1=1=F_2$. For $n\ge2$ apply Pascal's rule $\binom{n-k}{k}=\binom{n-1-k}{k}+\binom{n-1-k}{k-1}$ to every term:

$$s_n=\sum_{k\ge0}\binom{n-1-k}{k}+\sum_{k\ge1}\binom{n-1-k}{k-1}$$

The first sum is $s_{n-1}$. In the second put $j=k-1$: it becomes $\sum_{j\ge0}\binom{(n-2)-j}{j}=s_{n-2}$. Hence

$$s_n=s_{n-1}+s_{n-2}$$

the Fibonacci recurrence, with the same starting values. By induction $s_n=F_{n+1}$ for all $n\ge0$.

**Combinatorial view.** $\binom{n-k}{k}$ is the number of ways to tile a $1\times n$ strip with $k$ dominoes and $n-2k$ squares (choose which of the $n-k$ tiles are dominoes), so $s_n$ counts all square-domino tilings of the strip, which is the Fibonacci number $F_{n+1}$.
