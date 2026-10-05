---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Initial: On(C,B), OnTable(A), OnTable(B), Clear(A), Clear(C), HandEmpty. Goal: On(B,C), On(C,A), OnTable(A). (ii) pickup(x): pre OnTable(x), Clear(x), HandEmpty; add Holding(x); del OnTable(x), Clear(x), HandEmpty. putdown(x): pre Holding(x); add OnTable(x), Clear(x), HandEmpty; del Holding(x). unstack(x,y): pre On(x,y), Clear(x), HandEmpty; add Holding(x), Clear(y); del On(x,y), Clear(x), HandEmpty. stack(x,y): pre Holding(x), Clear(y); add On(x,y), Clear(x), HandEmpty; del Holding(x), Clear(y)."
sources: ["AIMA 3e sec. 10.1 (STRIPS / PDDL, blocks world)"]
---
**(i) STRIPS states** (4). Initial state (from the figure: A on the table, C on B, B on the table):

$$On(C,B)\land OnTable(A)\land OnTable(B)\land Clear(A)\land Clear(C)\land HandEmpty$$

Goal state (B on C on A, A on the table):

$$On(B,C)\land On(C,A)\land OnTable(A)$$

**(ii) STRIPS actions** (8).

| Action | Precondition | Add list | Delete list |
|:--|:--|:--|:--|
| $pickup(x)$ | $OnTable(x)\land Clear(x)\land HandEmpty$ | $Holding(x)$ | $OnTable(x)$, $Clear(x)$, $HandEmpty$ |
| $putdown(x)$ | $Holding(x)$ | $OnTable(x)$, $Clear(x)$, $HandEmpty$ | $Holding(x)$ |
| $unstack(x,y)$ | $On(x,y)\land Clear(x)\land HandEmpty$ | $Holding(x)$, $Clear(y)$ | $On(x,y)$, $Clear(x)$, $HandEmpty$ |
| $stack(x,y)$ | $Holding(x)\land Clear(y)$ | $On(x,y)$, $Clear(x)$, $HandEmpty$ | $Holding(x)$, $Clear(y)$ |
