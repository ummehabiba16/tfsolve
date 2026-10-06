---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Small pages: less internal fragmentation but bigger tables and more transfers; optimal page size p = sqrt(2 s e)."
sources: ["Tanenbaum MOS 4e, sec. 3.5.1 (page size)"]
---
**For small pages:** less internal fragmentation (on average half of the last page of each segment is wasted, so less memory is wasted); a better fit to the working set (less unused data is brought into memory).

**Against small pages:** more pages, hence a larger page table and more TLB entries needed (more TLB misses); disk transfers are inefficient because seek and rotational delay dominate, so reading many small pages costs much more than a few large ones.

**Optimal page size.** Let $s$ = average process size (bytes), $p$ = page size, $e$ = size of a page-table entry. A process needs $s/p$ pages, so

- page-table space $= \dfrac{s}{p}\,e$
- internal fragmentation $\approx \dfrac{p}{2}$ (half a page wasted on average)

$$\text{overhead}(p) = \frac{s\,e}{p} + \frac{p}{2}$$

Setting the derivative to zero:

$$\frac{d\,\text{overhead}}{dp} = -\frac{s\,e}{p^{2}} + \frac12 = 0 \;\Rightarrow\; p^{2} = 2se$$

$$\boxed{p_{\text{opt}} = \sqrt{2\,s\,e}}$$

(The second derivative $2se/p^3>0$, so this is a minimum.) Example: $s = 1$ MB, $e = 8$ B gives $p = \sqrt{2\cdot 2^{20}\cdot 8} = 4$ KB.
