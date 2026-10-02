---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Vertices = variables (live ranges); an edge joins two variables that are live at the same point, so they cannot share a register. Register allocation = colour the RIG with k = 3 colours. Every node has degree 4, so Chaitin removes a (troublesome), then c (troublesome), then b, d, e, f; popping gives f = R0, e = R1, d = R0, b = R1, c = R2, a = R2, with no spill (classes {a,c}, {b,e}, {d,f}). A spill is a variable that gets no register: it is kept in memory, with a store after each definition and a load before each use; the RIG is rebuilt and colouring repeated."
sources: ["KMS Global Register Allocation slides 72-166 (Register Interference Graph, Chaitin, Chaitin Reloaded, Improvements)", "Dragon book 2e sec. 8.8.4"]
---
**Meaning of the RIG.**

- **Vertex:** a variable (more precisely, a live range: a temporary or program variable that should be kept in a register).
- **Edge** between two variables: they are **live at the same program point** (they interfere), so they **cannot be placed in the same register**.

**Formulation as graph colouring.** Each physical register is a colour. Assigning registers so that interfering variables get different registers is exactly **colouring** the RIG with $k$ colours ($k$ = number of registers, here 3) so that adjacent vertices have different colours. If no $k$-colouring is found, some variables must be **spilled** to memory. $k$-colouring is NP-hard for $k \ge 3$, so Chaitin's heuristic is used.

**Chaitin's algorithm ($k = 3$):**

1. **Simplify:** repeatedly find a node with **fewer than $k$ neighbours** and remove it (push it on a stack). It can always be coloured later, since its neighbours use at most $k - 1$ colours.
2. If every remaining node has degree $\ge k$, pick one node (heuristic: e.g. highest degree or lowest spill cost), mark it **troublesome** (potential spill), and remove it anyway.
3. **Select:** pop nodes one by one and give each a colour not used by its already-coloured neighbours. A troublesome node may still find a free colour; if not, it is **actually spilled**.

**The given RIG** has edges a-b, a-d, a-e, a-f, b-c, b-d, b-f, c-d, c-e, c-f, d-e, e-f. Every vertex has degree **4** (each vertex is non-adjacent to exactly one other: a/c, b/e, d/f).

**Simplify** (ties broken by highest degree, then alphabetically):

| Step | Remaining degrees | Removed | Stack (bottom to top) |
|:-:|:--|:--|:--|
| 1 | a4 b4 c4 d4 e4 f4 | **a** (no node with degree < 3: troublesome) | a |
| 2 | b3 c4 d3 e3 f3 | **c** (still none < 3; highest degree: troublesome) | a, c |
| 3 | b2 d2 e2 f2 | **b** (degree 2 < 3) | a, c, b |
| 4 | d1 e2 f1 | **d** | a, c, b, d |
| 5 | e1 f1 | **e** | a, c, b, d, e |
| 6 | f0 | **f** | a, c, b, d, e, f |

**Select** (registers R0, R1, R2):

| Pop | Coloured neighbours | Register |
|:-:|:--|:-:|
| f | none | **R0** |
| e | f = R0 | **R1** |
| d | e = R1 | **R0** |
| b | d = R0, f = R0 | **R1** |
| c | b = R1, d = R0, e = R1, f = R0 | **R2** |
| a | b = R1, d = R0, e = R1, f = R0 | **R2** |

**Allocation:** a, c $\to$ R2; b, e $\to$ R1; d, f $\to$ R0. **No variable is spilled.** The two troublesome nodes found free colours, because a and c are not adjacent (and likewise b/e, d/f). A pessimistic version that spills as soon as no node of degree < 3 exists would have spilled `a` unnecessarily.

**Spill.** A *spill* is a variable that cannot be given a register: when a troublesome node is popped, all $k$ colours are used by its neighbours. Handling:

1. Keep the spilled variable in **memory** (a stack slot in the activation record).
2. Insert a **store** after every definition of it and a **load** into a fresh temporary just before every use. Each new temporary has a very short live range.
3. **Rebuild** the RIG (liveness changes) and run the colouring again. Repeat until no further spill is needed.

Spill candidates are chosen by heuristics such as lowest (use count / degree), avoiding variables used inside loops.
