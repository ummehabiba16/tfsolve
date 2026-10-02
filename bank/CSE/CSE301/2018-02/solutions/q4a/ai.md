---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Eulerian number $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle$ = permutations of $\{1..n\}$ with $k$ ascents. Inserting $n$ into a permutation of $n-1$: $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle$; also symmetry, row sums $n!$ and Worpitzky''s identity $x^n=\sum_k\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle\binom{x+k}{n}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Eulerian numbers)']
---
**Definition.** The Eulerian number $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle$ is the number of permutations $\pi_1\pi_2\dots\pi_n$ of $\{1,\dots,n\}$ with exactly $k$ **ascents**, i.e. $k$ places where $\pi_i<\pi_{i+1}$. For example, among the permutations of $\{1,2,3\}$, $123$ has 2 ascents, $132,213,231,312$ have 1, and $321$ has 0, so $\left\langle\genfrac{}{}{0pt}{}{3}{0}\right\rangle=1$, $\left\langle\genfrac{}{}{0pt}{}{3}{1}\right\rangle=4$, $\left\langle\genfrac{}{}{0pt}{}{3}{2}\right\rangle=1$.

**Recurrence.** Build a permutation of $\{1,\dots,n\}$ by inserting $n$ into one of the $n$ gaps of a permutation of $\{1,\dots,n-1\}$ that has $j$ ascents (and $n-2-j$ descents):

- at the front, or inside an ascent $\pi_i<\pi_{i+1}$: the number of ascents stays $j$ ($j+1$ such gaps);
- at the end, or inside a descent $\pi_i>\pi_{i+1}$: one ascent is added ($1+(n-2-j)=n-1-j$ such gaps).

A permutation with $k$ ascents therefore comes from one with $k$ ascents ($k+1$ ways) or one with $k-1$ ascents ($n-1-(k-1)=n-k$ ways):

$$\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=(k+1)\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle+(n-k)\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle,\qquad n\ge1$$

with $\left\langle\genfrac{}{}{0pt}{}{0}{0}\right\rangle=1$ and $\left\langle\genfrac{}{}{0pt}{}{0}{k}\right\rangle=0$ for $k\ne0$.

**Table** (rows $n=1,\dots,5$, columns $k=0,1,\dots$):

| $n$ | $k=0$ | 1 | 2 | 3 | 4 | row sum |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 1 | | | | | 1 |
| 2 | 1 | 1 | | | | 2 |
| 3 | 1 | 4 | 1 | | | 6 |
| 4 | 1 | 11 | 11 | 1 | | 24 |
| 5 | 1 | 26 | 66 | 26 | 1 | 120 |

(e.g. $\left\langle\genfrac{}{}{0pt}{}{4}{1}\right\rangle=2\cdot\left\langle\genfrac{}{}{0pt}{}{3}{1}\right\rangle+3\cdot\left\langle\genfrac{}{}{0pt}{}{3}{0}\right\rangle=8+3=11$.)

**Other properties.**

- Row sums: $\sum_k\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=n!$ (every permutation has some number of ascents).
- Symmetry: $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=\left\langle\genfrac{}{}{0pt}{}{n}{n-1-k}\right\rangle$ (reversing a permutation turns ascents into descents).
- Explicit formula: $\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle=\sum_{j=0}^{k}(-1)^j\binom{n+1}{j}(k+1-j)^n$.
- Worpitzky's identity: $x^n=\sum_k\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle\binom{x+k}{n}$, e.g. $x^2=\binom x2+\binom{x+1}{2}$.

(The second-order Eulerian numbers satisfy the similar recurrence $\left\langle\!\!\left\langle\genfrac{}{}{0pt}{}{n}{k}\right\rangle\!\!\right\rangle=(k+1)\left\langle\!\!\left\langle\genfrac{}{}{0pt}{}{n-1}{k}\right\rangle\!\!\right\rangle+(2n-1-k)\left\langle\!\!\left\langle\genfrac{}{}{0pt}{}{n-1}{k-1}\right\rangle\!\!\right\rangle$.)
