---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "State (m, c, b) = missionaries, cannibals and boat on the start bank; 16 reachable safe states; BFS (or any optimal search with repeated-state checking) finds an 11-crossing solution. Checking repeated states helps because every move is reversible. People find it hard because most moves are illegal or undo the previous one, and the key step requires moving 'backwards'."
sources: ["AIMA 3e sec. 3.2 and Exercise 3.9 (Missionaries and cannibals)"]
---
**(i) Formulation.**

- *State*: $(m, c, b)$ = number of missionaries and cannibals on the **starting** bank and whether the boat is there ($b=1$) or on the far bank ($b=0$). The other bank has $(3-m, 3-c)$. Only these distinctions are needed: individual identities, the boat's position mid-river, etc. are irrelevant.

- *Initial state*: $(3,3,1)$. *Goal*: $(0,0,0)$.

- *Actions*: the boat carries 1 or 2 people across: $\{1M, 2M, 1C, 2C, 1M1C\}$, from the bank where the boat is.

- *Constraint (legal state)*: on each bank, missionaries are either 0 or $\ge$ cannibals: $(m=0 \lor m\ge c)$ and $(m=3 \lor 3-m \ge 3-c)$.

- *Path cost*: 1 per crossing.

**State space.** 20 of the 32 possible tuples are legal; 16 are reachable from the start. Every edge is reversible (the boat can carry the same people back):

```text
               (3,3,1)
             /    |     \
      (3,2,0)  (3,1,0)  (2,2,0)
     dead end       \    /
                   (3,2,1)
                      |
                   (3,0,0)
                      |
                   (3,1,1)
                      |
                   (1,1,0)
                      |
                   (2,2,1)
                      |
                   (0,2,0)
                      |
                   (0,3,1)
                      |
                   (0,1,0)
                   /      \
             (1,1,1)    (0,2,1)
                   \      /
                   (0,0,0)   goal
                      |
                   (0,1,1)   dead end
```

From the start, sending 1C gives $(3,2,0)$, from which the only move is back; 2C or 1M1C lead to $(3,1,0)$ or $(2,2,0)$, both of which lead only to $(3,2,1)$. The middle of the space is a single chain.

One optimal solution (11 crossings): $(3,3,1)\to(2,2,0)\to(3,2,1)\to(3,0,0)\to(3,1,1)\to(1,1,0)\to(2,2,1)\to(0,2,0)\to(0,3,1)\to(0,1,0)\to(1,1,1)\to(0,0,0)$,

i.e. 1M1C over, 1M back, 2C over, 1C back, 2M over, 1M1C back, 2M over, 1C back, 2C over, 1M back, 1M1C over.

**(ii) Algorithm.** All steps cost 1, so **breadth-first search** (or uniform-cost / IDS) is optimal. The space is tiny (16 states), so any complete optimal method works.

Checking for repeated states **is a good idea**: every action is reversible, so a tree search without it regenerates the parent at every step (e.g. 1C over, 1C back, ...) and the tree grows exponentially with many duplicate paths; graph search (explored set) visits each of the 16 states once. It suffices to forbid returning to states already explored.

**(iii) Why people find it hard.** Although the space has only 16 states, from almost every state there is only one move that is both legal and does not undo the previous move, so the puzzle feels like a dead end at every step. People search greedily ("move more people to the far bank"), but the key step, $(3,1,1)\to(1,1,0)$ followed by bringing a missionary *and* a cannibal back, means moving people back to the start bank, which looks like going backwards. Humans also struggle to keep track of visited states, and the perceived branching factor seems large because they do not immediately see that most moves are illegal.
