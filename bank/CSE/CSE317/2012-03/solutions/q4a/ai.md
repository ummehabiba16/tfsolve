---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "STACK(X,Y): pre CLEAR(Y), HOLDING(X); add ON(X,Y), ARMEMPTY; del CLEAR(Y), HOLDING(X). UNSTACK(X,Y): pre ON(X,Y), CLEAR(X), ARMEMPTY; add HOLDING(X), CLEAR(Y); del ON(X,Y), ARMEMPTY. PICKUP(X): pre CLEAR(X), ONTABLE(X), ARMEMPTY; add HOLDING(X); del ONTABLE(X), ARMEMPTY. PUTDOWN(X): pre HOLDING(X); add ONTABLE(X), ARMEMPTY; del HOLDING(X)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.2 (blocks world operators)"]
---
Operators in the STRIPS style used for goal stack planning (Rich & Knight):

| Action | Precondition | Add list | Delete list |
|:--|:--|:--|:--|
| STACK(X,Y) | CLEAR(Y), HOLDING(X) | ARMEMPTY, ON(X,Y) | CLEAR(Y), HOLDING(X) |
| UNSTACK(X,Y) | ON(X,Y), CLEAR(X), ARMEMPTY | HOLDING(X), CLEAR(Y) | ON(X,Y), ARMEMPTY |
| PICKUP(X) | CLEAR(X), ONTABLE(X), ARMEMPTY | HOLDING(X) | ONTABLE(X), ARMEMPTY |
| PUTDOWN(X) | HOLDING(X) | ONTABLE(X), ARMEMPTY | HOLDING(X) |

(Preconditions are conjunctions: all listed literals must hold.)

(In this formulation $CLEAR(X)$ stays true while X is held, since nothing is on top of it. Some texts also delete $CLEAR(X)$ on PICKUP and UNSTACK and add it back on STACK and PUTDOWN; either is acceptable if used consistently.)
