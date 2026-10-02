---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The $n$-th circle meets each of the other $n-1$ circles in 2 points, giving $2(n-1)$ arcs that each split a region: $h_1=2$, $h_n=h_{n-1}+2(n-1)$, so $h_n=n^2-n+2$ ($n\ge1$).'
sources: ['Brualdi, Introductory Combinatorics, Ch. 7 (recurrence relations)', 'Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (regions in the plane)']
---
"General position" means every two circles meet in exactly two points and no three circles pass through a common point.

**Recurrence.** One circle divides the plane into 2 regions: $h_1=2$. Now add the $n$-th circle to $n-1$ circles in general position. It meets each of the other $n-1$ circles in 2 points, all distinct, so it has $2(n-1)$ intersection points, which cut it into $2(n-1)$ arcs (for $n\ge2$). Each arc runs through an existing region and splits it into two, so each arc adds exactly one region:

$$h_1=2,\qquad h_n=h_{n-1}+2(n-1)\quad(n\ge2)$$

**Formula.** Unfolding the recurrence,

$$h_n=2+\sum_{k=2}^{n}2(k-1)=2+2\cdot\frac{(n-1)n}{2}=n^2-n+2\qquad(n\ge1)$$

Check: $h_1=2$, $h_2=4$, $h_3=8$, $h_4=14$. (With no circles there is 1 region, so the formula holds for $n\ge1$.)
