---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Induction: $x^{\overline n}=x^{\overline{n-1}}(x+n-1)=\sum_k\genfrac[]{0pt}{}{n-1}{k}x^{k+1}+(n-1)\sum_k\genfrac[]{0pt}{}{n-1}{k}x^k=\sum_k\big(\genfrac[]{0pt}{}{n-1}{k-1}+(n-1)\genfrac[]{0pt}{}{n-1}{k}\big)x^k=\sum_k\genfrac[]{0pt}{}{n}{k}x^k$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (Stirling numbers, identity (6.11))']
---
Here $x^{\overline n}=x(x+1)\cdots(x+n-1)$ is the rising factorial power, and $\genfrac[]{0pt}{}{n}{k}$ are the Stirling numbers of the first kind, which satisfy

$$\genfrac[]{0pt}{}{n}{k}=(n-1)\genfrac[]{0pt}{}{n-1}{k}+\genfrac[]{0pt}{}{n-1}{k-1}\quad(n\ge1),\qquad\genfrac[]{0pt}{}{0}{k}=[k=0]$$

**Claim.** $x^{\overline n}=\sum_k\genfrac[]{0pt}{}{n}{k}x^k$ for all integers $n\ge0$.

**Proof by induction on $n$.**

*Base case $n=0$:* $x^{\overline0}=1$ and $\sum_k\genfrac[]{0pt}{}{0}{k}x^k=\genfrac[]{0pt}{}{0}{0}=1$.

*Induction step.* Assume the claim for $n-1$. Then

$$x^{\overline n}=x^{\overline{n-1}}\,(x+n-1)=\sum_k\genfrac[]{0pt}{}{n-1}{k}x^{k+1}+(n-1)\sum_k\genfrac[]{0pt}{}{n-1}{k}x^k$$

Shift the index in the first sum ($k\to k-1$):

$$x^{\overline n}=\sum_k\left(\genfrac[]{0pt}{}{n-1}{k-1}+(n-1)\genfrac[]{0pt}{}{n-1}{k}\right)x^k=\sum_k\genfrac[]{0pt}{}{n}{k}x^k$$

by the recurrence. This completes the induction. $\blacksquare$

**Example.** $x^{\overline3}=x(x+1)(x+2)=x^3+3x^2+2x$, and $\genfrac[]{0pt}{}{3}{3}=1$, $\genfrac[]{0pt}{}{3}{2}=3$, $\genfrac[]{0pt}{}{3}{1}=2$. (Combinatorially: the coefficient of $x^k$ in $x(x+1)\cdots(x+n-1)$ counts permutations of $n$ elements with $k$ cycles.)
