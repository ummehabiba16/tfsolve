---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$L_n=L_{n-1}+n$, $L_0=1$, so $L_n=\frac{n(n+1)}{2}+1$; $L_{12}=79<89\le L_{13}=92$, so at least 13 fences are needed.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (lines in the plane)']
---
**Regions made by $n$ lines.** Let $L_n$ be the maximum number of regions into which $n$ straight lines divide the plane. With no lines there is one region: $L_0=1$. When the $n$-th line is added it can cross each of the $n-1$ earlier lines at most once, and it does so in distinct points when no two lines are parallel and no three meet in a point. These $n-1$ crossing points cut the new line into $n$ pieces, and each piece splits one existing region into two, so the new line adds exactly $n$ regions (and can add no more):

$$L_0=1,\qquad L_n=L_{n-1}+n\quad(n\ge1)$$

Unfolding,

$$L_n=1+(1+2+\cdots+n)=1+\frac{n(n+1)}{2}$$

**Fences for 89 cows.** Each cow needs its own region, so we need the smallest $n$ with $L_n\ge89$:

$$L_{12}=1+\frac{12\cdot13}{2}=79<89,\qquad L_{13}=1+\frac{13\cdot14}{2}=92\ge89$$

Twelve fences give at most 79 regions, which is not enough, while 13 fences in general position give 92 regions.

**Answer:** the man needs at least $\mathbf{13}$ straight fences.
