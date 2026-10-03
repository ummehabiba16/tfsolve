---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) True: L-R-T-T' is blocked at the observed T, and L-C-D-R is blocked at the unobserved collider D. (ii) False: L-R-T-B is active, because T is an observed collider. (iii) True: observing R blocks it. (iv) False: L-C-D is active. (v) False: L-R-D is still active."
sources: ["MNM slides Uncertainty-3-BN-IND (active and inactive triples, d-separation)", "Berkeley CS188 Bayes nets: independence (same network)"]
---
**Edges.** $L\to C$, $L\to R$, $C\to D$, $R\to D$, $R\to T$, $B\to T$, $T\to T'$.

**Rules for triples.**

- *Causal chain* $X\to Y\to Z$ and *common cause* $X\leftarrow Y\to Z$ are active iff $Y$ is **not** observed.
- *Common effect* $X\to Y\leftarrow Z$ is active iff $Y$ **or a descendant** of $Y$ is observed.
- $X\perp Y\mid Z$ is guaranteed iff every path between them has at least one inactive triple.

**(i) $L\perp T'\mid T$: True.**

- $L\to R\to T\to T'$: the chain $R\to T\to T'$ with $T$ observed is inactive, so the path is blocked.
- $L\to C\to D\leftarrow R\to T\to T'$: $D$ is a collider with neither it nor its descendants observed, so the path is blocked.

**(ii) $L\perp B\mid T$: False.**

- $L\to R\to T\leftarrow B$: the chain $L\to R\to T$ is active ($R$ is not observed), and the collider $R\to T\leftarrow B$ is active because $T$ is observed. The path is active, so independence is not guaranteed.

**(iii) $L\perp B\mid T,R$: True.**

- $L\to R\to T\leftarrow B$: the chain $L\to R\to T$ with $R$ observed is inactive, so the path is blocked.
- $L\to C\to D\leftarrow R\to T\leftarrow B$: the collider $D$ is not observed, so the path is blocked. (Also, $R$ is observed in the common cause $D\leftarrow R\to T$.)

**(iv) $L\perp D$: False.** $L\to C\to D$ is a chain with $C$ not observed, so it is active.

**(v) $L\perp D\mid C$: False.** $L\to C\to D$ is now blocked, but $L\to R\to D$ is a chain with $R$ not observed, so it is active.

| Statement | Guaranteed? |
|:--|:-:|
| (i) $L\perp T'\mid T$ | **True** |
| (ii) $L\perp B\mid T$ | **False** |
| (iii) $L\perp B\mid T,R$ | **True** |
| (iv) $L\perp D$ | **False** |
| (v) $L\perp D\mid C$ | **False** |

(Checked numerically on the network with random CPTs: (i) and (iii) hold exactly; (ii), (iv) and (v) fail.)
