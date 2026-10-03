---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) True: blocked at the observed T. (ii) True: the collider T is unobserved and has no observed descendant. (iii) False: observing the collider T activates L-R-T-B. (iv) False: T', a descendant of the collider T, is observed. (v) True: the observed R blocks the chain."
sources: ["MNM slides Uncertainty-3-BN-IND (d-separation)", "Berkeley CS188 Bayes nets: independence"]
---
**Edges.** $L\to R$, $R\to D$, $R\to T$, $B\to T$, $T\to T'$. The only paths between $L$ and $B$ go through $L\to R\to T\leftarrow B$ ($D$ is a dead end). Rules: a chain or common cause is active iff the middle node is unobserved; a common effect is active iff the middle node or a descendant is observed.

**(i) $L\perp T'\mid T$: True.** The only path, $L\to R\to T\to T'$, contains the chain $R\to T\to T'$ with $T$ observed, which is inactive.

**(ii) $L\perp B$: True.** In $L\to R\to T\leftarrow B$, the triple $R\to T\leftarrow B$ is a common effect. Neither $T$ nor its descendant $T'$ is observed, so it is inactive and the path is blocked.

**(iii) $L\perp B\mid T$: False.** Observing $T$ makes $R\to T\leftarrow B$ active (explaining away), and $L\to R\to T$ is active because $R$ is unobserved. The path is active.

**(iv) $L\perp B\mid T'$: False.** $T'$ is a descendant of the collider $T$, so observing it activates $R\to T\leftarrow B$. The path is active.

**(v) $L\perp B\mid T,R$: True.** The chain $L\to R\to T$ with $R$ observed is inactive, so the path is blocked.

| Statement | Answer |
|:--|:-:|
| (i) $L\perp T'\mid T$ | **True** |
| (ii) $L\perp B$ | **True** |
| (iii) $L\perp B\mid T$ | **False** |
| (iv) $L\perp B\mid T'$ | **False** |
| (v) $L\perp B\mid T,R$ | **True** |
