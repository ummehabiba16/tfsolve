---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Variables X1..X5 (squares), domains {R, G}, constraints X1 != X2, X2 != X3, X1 != X4, X2 != X5, X4 != X5. (ii) Forward checking after X1 = R: D2 = {G}, D4 = {G}; D3 and D5 unchanged {R, G}. (iii) Arc consistency after X5 = G: D2 = D4 = {R}, then D1 = {G}, D3 = {G}: the unique solution 1 = G, 2 = R, 3 = G, 4 = R, 5 = G."
sources: ["AIMA 3e sec. 6.1, 6.2.2 (arc consistency), 6.3.2 (forward checking)"]
---
**Board** (Figure 6a): squares 1, 2, 3 in the top row, and 4, 5 below 1 and 2. Horizontal or vertical adjacencies: 1-2, 2-3, 1-4, 2-5, 4-5.

**(i) CSP.**

- *Variables:* $X_1,X_2,X_3,X_4,X_5$ (the colour of each square).
- *Domains:* $D_i=\{R,G\}$ for every $i$.
- *Constraints:* $X_1\neq X_2$, $X_2\neq X_3$, $X_1\neq X_4$, $X_2\neq X_5$, $X_4\neq X_5$.

**(ii) Forward checking after $X_1=R$.** Remove $R$ from the domains of $X_1$'s unassigned neighbours, $X_2$ and $X_4$:

| | $X_1$ | $X_2$ | $X_3$ | $X_4$ | $X_5$ |
|:--|:-:|:-:|:-:|:-:|:-:|
| Before | {R,G} | {R,G} | {R,G} | {R,G} | {R,G} |
| After $X_1=R$ | **R** | {G} | {R,G} | {G} | {R,G} |

Forward checking only looks at the direct neighbours of the assigned variable, so $X_3$ and $X_5$ are unchanged, even though $X_2=G$ and $X_4=G$ will later force them.

**(iii) Arc-consistency checking after $X_5=G$.** AC-3 propagates until no domain changes:

| Step | Arc revised | Effect |
|:-:|:--|:--|
| 1 | $X_2\to X_5$ | $G$ has no support (needs $X_2\neq G$): $D_2=\{R\}$ |
| 2 | $X_4\to X_5$ | $D_4=\{R\}$ |
| 3 | $X_1\to X_2$ | $R$ has no support (since $X_2=R$): $D_1=\{G\}$ |
| 4 | $X_3\to X_2$ | $D_3=\{G\}$ |
| 5 | $X_1\to X_4$, others | consistent ($G\neq R$); no further change |

**Result:** $X_1=G$, $X_2=R$, $X_3=G$, $X_4=R$, $X_5=G$. Every domain is reduced to a single value, which is a **complete solution** found by propagation alone, without search.
