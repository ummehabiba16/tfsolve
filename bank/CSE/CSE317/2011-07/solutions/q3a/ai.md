---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "STACK(X,Y): pre CLEAR(Y), HOLDING(X); add ON(X,Y), ARMEMPTY; del CLEAR(Y), HOLDING(X). UNSTACK(X,Y): pre ON(X,Y), CLEAR(X), ARMEMPTY; add HOLDING(X), CLEAR(Y); del ON(X,Y), ARMEMPTY. PICKUP(X): pre CLEAR(X), ONTABLE(X), ARMEMPTY; add HOLDING(X); del ONTABLE(X), ARMEMPTY. PUTDOWN(X): pre HOLDING(X); add ONTABLE(X), ARMEMPTY; del HOLDING(X)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.2"]
---
| Action | Precondition | Add list | Delete list |
|:--|:--|:--|:--|
| **STACK(X, Y)**: put the held block X on Y | $CLEAR(Y)\land HOLDING(X)$ | $ARMEMPTY$, $ON(X,Y)$ | $CLEAR(Y)$, $HOLDING(X)$ |
| **UNSTACK(X, Y)**: lift X off Y | $ON(X,Y)\land CLEAR(X)\land ARMEMPTY$ | $HOLDING(X)$, $CLEAR(Y)$ | $ON(X,Y)$, $ARMEMPTY$ |
| **PICKUP(X)**: lift X from the table | $CLEAR(X)\land ONTABLE(X)\land ARMEMPTY$ | $HOLDING(X)$ | $ONTABLE(X)$, $ARMEMPTY$ |
| **PUTDOWN(X)**: put the held X on the table | $HOLDING(X)$ | $ONTABLE(X)$, $ARMEMPTY$ | $HOLDING(X)$ |
