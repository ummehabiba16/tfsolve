---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Two triangles cross in at most 6 points, so the $n$-th triangle is cut into at most $6(n-1)$ arcs, each adding a region: $T_1=2$, $T_n=T_{n-1}+6(n-1)$, hence $T_n=3n^2-3n+2$ (attained, e.g., by congruent equilateral triangles with a common centre rotated by distinct angles).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (regions in the plane; exercise on triangles)']
---
**Two triangles cross in at most 6 points.** Each side of one triangle is a segment, and a line meets the boundary of a convex region (the other triangle) in at most 2 points. So each of the 3 sides crosses the other triangle at most twice: at most $3\times2=6$ crossing points.

**Recurrence.** Let $T_n$ be the maximum number of regions defined by $n$ triangles. One triangle gives 2 regions (inside and outside): $T_1=2$. Add the $n$-th triangle. It crosses each of the other $n-1$ triangles in at most 6 points, so its boundary contains at most $6(n-1)$ crossing points, which cut the boundary into at most $6(n-1)$ arcs (for $n\ge2$). Each arc splits exactly one existing region into two, so the new triangle adds at most $6(n-1)$ regions, with equality when all the crossings are distinct:

$$T_1=2,\qquad T_n=T_{n-1}+6(n-1)\quad(n\ge2)$$

**Closed form.**

$$T_n=2+6\sum_{k=1}^{n-1}k=2+6\cdot\frac{n(n-1)}{2}=3n^2-3n+2$$

Values: $T_1=2$, $T_2=8$ (the Star of David: 6 small triangles, the hexagon and the outside), $T_3=20$, $T_4=38$.

**The maximum is attained.** Take $n$ congruent equilateral triangles with the same centre, rotated by different angles in $(0^\circ,120^\circ)$. All their sides are tangent to the same incircle. Two of them overlap in a hexagon whose 6 vertices are crossings, so every pair crosses in 6 points, and no three sides pass through one point (from an outside point there are only two tangent lines to a circle). So all crossings are distinct and $T_n=3n^2-3n+2$ is achieved.

(Check with Euler's formula $V-E+F=2$: $V=3n+6\binom n2$, $E=n\big(3+6(n-1)\big)$, so $F=E-V+2=3n(n-1)+2$.)
