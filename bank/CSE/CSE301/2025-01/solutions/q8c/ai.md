---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A permutation with $n-1$ cycles has one 2-cycle: $\genfrac[]{0pt}{}{n}{n-1}=\binom n2$. With $n-2$ cycles it has one 3-cycle ($2\binom n3$ ways) or two 2-cycles ($3\binom n4$ ways): $\genfrac[]{0pt}{}{n}{n-2}=2\binom n3+3\binom n4=\frac{3n-1}{4}\binom n3$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Stirling numbers of the first kind)']
---
$\genfrac[]{0pt}{}{n}{k}$ counts the permutations of $\{1,\dots,n\}$ with exactly $k$ cycles (equivalently, arrangements of $n$ objects into $k$ cycles). The cycle lengths add up to $n$.

**$k=n-1$.** $n-1$ cycles with total length $n$ means one cycle of length 2 and $n-2$ fixed points. A 2-cycle is determined by its two elements:

$$\genfrac[]{0pt}{}{n}{n-1}=\binom n2=\frac{n(n-1)}{2}$$

**$k=n-2$.** For a permutation with $k$ cycles, $\sum_{\text{cycles}}(\text{length}-1)=n-k$. With $k=n-2$ this sum is 2, so either

- one 3-cycle and $n-3$ fixed points: choose the 3 elements ($\binom n3$ ways) and one of the $(3-1)!=2$ cyclic orders: $2\binom n3$; or
- two 2-cycles and $n-4$ fixed points: choose the 4 elements ($\binom n4$ ways) and split them into 2 pairs (3 ways): $3\binom n4$.

$$\genfrac[]{0pt}{}{n}{n-2}=2\binom n3+3\binom n4=\binom n3\left(2+\frac{3(n-3)}{4}\right)=\frac{3n-1}{4}\binom n3$$

**Check with the recurrence** $\genfrac[]{0pt}{}{n}{k}=(n-1)\genfrac[]{0pt}{}{n-1}{k}+\genfrac[]{0pt}{}{n-1}{k-1}$: for $k=n-1$ it gives $\genfrac[]{0pt}{}{n}{n-1}=(n-1)+\genfrac[]{0pt}{}{n-1}{n-2}$, whose solution is $1+2+\cdots+(n-1)=\binom n2$. Values: $\genfrac[]{0pt}{}{4}{2}=11=2\cdot4+3\cdot1$ and $\genfrac[]{0pt}{}{5}{3}=35=2\cdot10+3\cdot5$.
