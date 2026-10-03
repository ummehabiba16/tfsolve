---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Only network (c): the three gene nodes are roots there. (ii) P(Gchild = l | Gf, Gm) = 1-m (l,l), 1/2 (l,r), 1/2 (r,l), m (r,r); it does not depend on s. (iii) P(Gchild = l) = (1-m)q^2 + q(1-q) + m(1-q)^2 = q + m - 2mq."
sources: ["MNM slides Uncertainty-2-BN, Uncertainty-3-BN-IND", "AIMA 3e Exercise 14.6 / 4e Exercise 13.HAND (handedness)"]
---
**(i) Which networks assert $P(G_f,G_m,G_c)=P(G_f)P(G_m)P(G_c)$?** With no evidence, the network asserts this factorization exactly when the three gene nodes are d-separated from each other (every path between them is blocked).

- (a) and (b): $G_{child}$ has parents $G_{mother}$ and $G_{father}$, so $P(G_c\mid G_m,G_f)\ne P(G_c)$ in general. The equation does **not** follow.
- (c): $G_{mother}$, $G_{father}$ and $G_{child}$ are all root nodes. The only paths between them go through $H_{child}$, which is a collider (common effect) and is not observed, so the paths are blocked. Summing the joint over all $H$'s leaves $P(G_m)P(G_f)P(G_c)$.

**Only network (c)** satisfies the equation. (In (c), the child's gene ignores the parents' genes, which is genetically wrong. (a) is the realistic model.)

**(ii) CPT of $G_{child}$ in network (a).** The child gets the gene of one parent, each with probability $\frac12$. That copy mutates (flips) with probability $m$:

$$P(G_c=l\mid g_m,g_f)=\tfrac12P(l\mid g_m)+\tfrac12P(l\mid g_f),\quad P(l\mid l)=1-m,\ P(l\mid r)=m.$$

| $G_{mother}$ | $G_{father}$ | $P(G_{child}=l)$ | $P(G_{child}=r)$ |
|:-:|:-:|:-:|:-:|
| $l$ | $l$ | $1-m$ | $m$ |
| $l$ | $r$ | $\frac12(1-m)+\frac12m=\frac12$ | $\frac12$ |
| $r$ | $l$ | $\frac12$ | $\frac12$ |
| $r$ | $r$ | $m$ | $1-m$ |

The probability $s$ does not appear: it belongs to the $H$ nodes, with $P(H=l\mid G=l)=s$ and $P(H=l\mid G=r)=1-s$.

**(iii) $P(G_{child}=l)$ by conditioning on the parents.** In (a) the parents are independent roots, with $P(G_m=l)=P(G_f=l)=q$:

$$P(G_c=l)=\sum_{g_m,g_f}P(G_c=l\mid g_m,g_f)\,P(g_m)\,P(g_f)$$

$$=(1-m)q^2+\tfrac12\,q(1-q)+\tfrac12\,(1-q)q+m(1-q)^2$$

$$=q^2-mq^2+q-q^2+m-2mq+mq^2$$

$$\boxed{P(G_{child}=l)=q+m-2mq=m+(1-2m)\,q}$$

*Check:* with $m=0$, $P=q$ (no mutation, so the gene frequency is preserved). With $q=\frac12$, $P=\frac12$.
