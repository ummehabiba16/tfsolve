---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "alpha = 1/P(e) = 1 / sum_x P(x, e), the normalization constant that makes the entries of P(X | e) sum to 1. With a hidden variable y: P(X | e) = alpha P(X, e) = alpha sum_y P(X, e, y)."
sources: ["MNM slides Uncertainty-1-(quantifying) (normalization, marginalization)", "AIMA 4e sec. 12.3 (inference using full joint distributions)"]
---
**$\alpha$, the normalization constant (5).** By the definition of conditional probability,

$$P(X\mid e)=\frac{P(X,e)}{P(e)}=\alpha\,P(X,e),\qquad \alpha=\frac{1}{P(e)}=\frac{1}{\sum_xP(x,e)}.$$

$P(e)$ does not depend on $X$, so it is one constant. We never need it in advance: compute the unnormalized values $P(x,e)$ for every $x$, then divide by their sum, so that the distribution sums to 1.

*Example:* $P(\text{cavity},\text{toothache})=0.12$ and $P(\neg\text{cavity},\text{toothache})=0.08$. Then $\alpha=1/0.2$, and $P(\text{Cavity}\mid\text{toothache})=\langle0.6,\ 0.4\rangle$.

**With a third (hidden) variable $y$ (5).** If we know the joint $P(X,e,y)$, marginalize (sum out) $y$:

$$P(X\mid e)=\alpha\,P(X,e)=\alpha\sum_{y}P(X,e,y),\qquad \alpha=\frac{1}{\sum_x\sum_yP(x,e,y)}.$$

In general, with query $X$, evidence $\mathbf{e}$ and hidden variables $\mathbf{Y}$: $P(X\mid\mathbf{e})=\alpha\sum_{\mathbf{y}}P(X,\mathbf{e},\mathbf{y})$. This is inference by enumeration.
