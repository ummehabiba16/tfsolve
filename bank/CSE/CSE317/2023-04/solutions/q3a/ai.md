---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "State (m, c, b) on the start bank, start (3,3,1), goal (0,0,0), five boat loads, legality constraint on both banks; 16 reachable states; BFS finds the optimal 11-crossing solution, and repeated-state checking is a good idea because all moves are reversible."
sources: ["AIMA 3e sec. 3.2, 3.4.1 and Exercise 3.9"]
---
**(i) Formulation.**

- *States*: $(m,c,b)$ = number of missionaries and cannibals on the starting bank, $b=1$ if the boat is on the starting bank, 0 otherwise. The far bank has $(3-m,3-c)$.

- *Initial state*: $(3,3,1)$; *goal test*: state $=(0,0,0)$.

- *Actions*: move 1M, 2M, 1C, 2C or 1M+1C across in the boat, from the bank where the boat is (so $b$ flips).

- *Legal states*: on each bank the missionaries are either absent or not outnumbered: $(m=0 \lor m\ge c)$ and $(3-m=0 \lor 3-m\ge 3-c)$.

- *Path cost*: 1 per crossing.

**State space** (16 reachable legal states; each edge is reversible):

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

**(ii) Search algorithm.** All actions cost 1, so **breadth-first graph search** (or UCS/IDS) finds an optimal solution. It returns an 11-crossing plan:

$(3,3,1)\to(2,2,0)\to(3,2,1)\to(3,0,0)\to(3,1,1)\to(1,1,0)\to(2,2,1)\to(0,2,0)\to(0,3,1)\to(0,1,0)\to(1,1,1)\to(0,0,0)$

(1M1C over, 1M back, 2C over, 1C back, 2M over, 1M1C back, 2M over, 1C back, 2C over, 1M back, 1M1C over.)

Checking repeated states **is a good idea**: every move can be undone by sending the same people back, so tree search keeps regenerating previous states (infinite loops for DFS, exponential blow-up for BFS). With an explored set, each of the 16 states is expanded once.
