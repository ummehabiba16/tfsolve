---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "For agent i in {1, 2}: STACK(X,Y,i): pre CLEAR(Y), HOLDING(X,i); add ON(X,Y), CLEAR(X), ARMEMPTY(i); del CLEAR(Y), HOLDING(X,i). UNSTACK(X,Y,i): pre ON(X,Y), CLEAR(X), ARMEMPTY(i); add HOLDING(X,i), CLEAR(Y); del ON(X,Y), CLEAR(X), ARMEMPTY(i). PICKUP(X,i): pre ONTABLE(X), CLEAR(X), ARMEMPTY(i); add HOLDING(X,i); del ONTABLE(X), CLEAR(X), ARMEMPTY(i). PUTDOWN(X,i): pre HOLDING(X,i); add ONTABLE(X), CLEAR(X), ARMEMPTY(i); del HOLDING(X,i)."
sources: ["Rich & Knight, Artificial Intelligence, sec. 13.2-13.4 (blocks world, goal stack planning)", "AIMA 3e sec. 10.1 (STRIPS-style action schemas)"]
---
For each agent $i\in\{1,2\}$:

| Action | Precondition | Add list | Delete list |
|:--|:--|:--|:--|
| **STACK(X, Y, i)** (agent $i$ puts the held X on Y) | $CLEAR(Y)\land HOLDING(X,i)$ | $ON(X,Y)$, $CLEAR(X)$, $ARMEMPTY(i)$ | $CLEAR(Y)$, $HOLDING(X,i)$ |
| **UNSTACK(X, Y, i)** (agent $i$ lifts X off Y) | $ON(X,Y)\land CLEAR(X)\land ARMEMPTY(i)$ | $HOLDING(X,i)$, $CLEAR(Y)$ | $ON(X,Y)$, $CLEAR(X)$, $ARMEMPTY(i)$ |
| **PICKUP(X, i)** (agent $i$ lifts X from the table) | $ONTABLE(X)\land CLEAR(X)\land ARMEMPTY(i)$ | $HOLDING(X,i)$ | $ONTABLE(X)$, $CLEAR(X)$, $ARMEMPTY(i)$ |
| **PUTDOWN(X, i)** (agent $i$ puts X on the table) | $HOLDING(X,i)$ | $ONTABLE(X)$, $CLEAR(X)$, $ARMEMPTY(i)$ | $HOLDING(X,i)$ |

Notes:

- A block that is being held is **not** $CLEAR$: $CLEAR$ is deleted when it is lifted and added back when it is put down. So the other agent cannot stack onto it or lift it, and the two agents cannot interfere.
- Each agent's arm is independent: $ARMEMPTY(1)$ and $ARMEMPTY(2)$ are separate predicates, so both agents can hold one block each at the same time.
