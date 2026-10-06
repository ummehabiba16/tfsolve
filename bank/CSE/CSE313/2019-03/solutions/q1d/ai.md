---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Overhead s*e/p + p/2 is minimised at p = sqrt(2 s e)."
sources: ["Tanenbaum MOS 4e, sec. 3.5.1 (page size)"]
---
Let $s$ be the average process size (bytes), $p$ the page size and $e$ the page-table entry size.

- Page table: $s/p$ entries, so $\dfrac{s\,e}{p}$ bytes.
- Internal fragmentation: on average half of the last page, $\dfrac{p}{2}$ bytes.

$$\text{overhead}(p)=\frac{s\,e}{p}+\frac{p}{2}$$

$$\frac{d}{dp}\text{overhead}=-\frac{s\,e}{p^{2}}+\frac12=0\ \Rightarrow\ p^{2}=2\,s\,e$$

$$\boxed{p_{\text{opt}}=\sqrt{2\,s\,e}}$$

The second derivative $2se/p^{3}>0$, so this is the minimum.
