---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Physical states: [. X], [X .], [X V], [V X]. Initial belief {[. X], [X .]}. Left gives {[X .], [X V]}; Right gives {[. X], [V X]}. From {[X .], [X V]}, Right gives {[V X]} (goal); from {[. X], [V X]}, Left gives {[X V]} (goal). 5 reachable belief states; the plans Left, Right and Right, Left both guarantee every cell is visited."
sources: ["AIMA 3e sec. 4.4.1 (sensorless vacuum world, Fig. 4.14)"]
---
**Physical states** of the 2-by-1 grid (X = agent, V = visited, . = unvisited): $[.\ X]$, $[X\ .]$, $[X\ V]$, $[V\ X]$. The goal is for both cells to be visited: $[X\ V]$ or $[V\ X]$.

**Initial belief state** (Figure 7(c)): $B_0=\{[.\ X],\ [X\ .]\}$. The agent does not know which cell it started in.

**Reachable belief states and transitions** (L = Left, R = Right; moving into the wall changes nothing):

| Belief state | Left | Right |
|:--|:--|:--|
| $B_0=\{[.\ X],[X\ .]\}$ | $B_1=\{[X\ .],[X\ V]\}$ | $B_2=\{[.\ X],[V\ X]\}$ |
| $B_1=\{[X\ .],[X\ V]\}$ | $B_1$ | $B_3=\{[V\ X]\}$ **goal** |
| $B_2=\{[.\ X],[V\ X]\}$ | $B_4=\{[X\ V]\}$ **goal** | $B_2$ |
| $B_3=\{[V\ X]\}$ | $B_4$ | $B_3$ |
| $B_4=\{[X\ V]\}$ | $B_4$ | $B_3$ |

```text
                    B0 {[. X], [X .]}
                L /                  \ R
                 v                    v
   (L)  B1 {[X .],[X V]}        B2 {[. X],[V X]}  (R)
                 | R                  | L
                 v                    v
           B3 {[V X]}  <---R---  B4 {[X V]}
             (R)       ---L--->    (L)
```

$B_3$ and $B_4$ are **goal belief states**: in every possible world, all cells have been visited.

**Plans:** $[Left, Right]$ ($B_0\to B_1\to B_3$) or $[Right, Left]$ ($B_0\to B_2\to B_4$). Each guarantees success without any sensing: the first move pushes the agent against a wall from either start, and the second move visits the other cell.
