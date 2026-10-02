---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Two ellipses meet in at most 4 points, so the $n$-th ellipse is cut into at most $4(n-1)$ arcs, each adding a region: (i) $E(1)=2$, $E(n)=E(n-1)+4(n-1)$; (ii) $E(n)=2+2n(n-1)=2n^2-2n+2$ (attained by congruent concentric ellipses at distinct angles).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (regions in the plane)']
---
**Two ellipses meet in at most 4 points** (they are conics: by Bézout's theorem two distinct conics share at most $2\times2=4$ points). Two congruent ellipses with the same centre, one rotated by a small angle, do meet in 4 points.

**(i) Recurrence.** $E(0)=1$ and one ellipse divides the plane into 2 regions, $E(1)=2$. Add the $n$-th ellipse ($n\ge2$). It crosses each of the earlier $n-1$ ellipses in at most 4 points, so at most $4(n-1)$ crossing points lie on it; when they are all distinct they cut it into $4(n-1)$ arcs. Each arc splits one existing region into two, so the new ellipse adds exactly $4(n-1)$ regions (and never more):

$$E(1)=2,\qquad E(n)=E(n-1)+4(n-1)\quad(n\ge2)$$

**(ii) Closed form.**

$$E(n)=2+\sum_{k=2}^{n}4(k-1)=2+4\cdot\frac{n(n-1)}{2}=2n^2-2n+2\qquad(n\ge1)$$

Values: $E(1)=2$, $E(2)=6$ (centre, four lobes, outside), $E(3)=14$, $E(4)=26$.

**The maximum is attained.** Take $n$ congruent ellipses ($a>b$) with a common centre, rotated by distinct angles $\theta_1,\dots,\theta_n\in[0^\circ,180^\circ)$. Ellipses $i$ and $j$ meet where the polar angle $\varphi$ satisfies $\cos^2(\varphi-\theta_i)=\cos^2(\varphi-\theta_j)$, i.e. $\varphi\equiv\frac{\theta_i+\theta_j}{2}\pmod{90^\circ}$: four points. A third ellipse $k$ through one of these points would need $\theta_k\equiv\theta_j\pmod{180^\circ}$, so no three ellipses share a point and the bound is reached.
