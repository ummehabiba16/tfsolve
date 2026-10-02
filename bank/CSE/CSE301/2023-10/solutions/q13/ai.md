---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$C_0=1$, $C_1=2$ (1 bounded + 1 unbounded); the $n$-th circle meets each earlier one in at most 2 points, giving $2(n-1)$ arcs that each add a region: $C_n=C_{n-1}+2(n-1)$, so $C_n=n^2-n+2$ ($n\ge1$): $n^2-n+1$ bounded regions and 1 unbounded.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (regions in the plane)']
---
**Bounded and unbounded regions.** With no circles there is exactly one region, the whole plane (unbounded). One circle gives 2 regions: one bounded (inside) and one unbounded (outside). Adding circles never creates another unbounded region, since every circle is bounded: there is always exactly **one** unbounded region, and all the others are bounded.

**Two circles meet in at most 2 points**, so the $n$-th circle can cross the earlier $n-1$ circles in at most $2(n-1)$ points.

**Recurrence.** Let $C_n$ be the maximum number of regions; $C_0=1$, $C_1=2$. When the $n$-th circle ($n\ge2$) crosses each earlier circle twice, at points that are all distinct, these $2(n-1)$ points cut it into $2(n-1)$ arcs. Each arc runs through one existing region and splits it into two, so the new circle adds exactly $2(n-1)$ regions; with fewer or coinciding crossings it adds fewer. Hence

$$C_1=2,\qquad C_n=C_{n-1}+2(n-1)\quad(n\ge2)$$

**Closed form.**

$$C_n=2+\sum_{k=2}^{n}2(k-1)=2+n(n-1)=n^2-n+2\qquad(n\ge1)$$

so there are $n^2-n+1$ bounded regions and 1 unbounded region. Values: $C_1=2$, $C_2=4$, $C_3=8$, $C_4=14$.

**The bound can be reached.** Take $n$ circles of radius 1 with centres $(0,0),(\varepsilon,0),(2\varepsilon,0),\dots,((n-1)\varepsilon,0)$ where $(n-1)\varepsilon<2$. Any two centres are less than 2 apart, so every two circles cross in 2 points; circles $i$ and $j$ cross on the vertical line $x=\frac{(i+j)\varepsilon}{2}$, so no three circles pass through a common point. Hence the $n$-th circle really does cross all the others in $2(n-1)$ distinct points.

(Check with Euler's formula: $V=2\binom n2$ crossing points, $E=2n(n-1)$ arcs, so $F=E-V+2=n(n-1)+2$.)
