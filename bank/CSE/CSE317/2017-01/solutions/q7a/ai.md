---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) States: partial colourings of the regions; initial: none coloured; action: give an uncoloured region a colour (of 4) different from its coloured neighbours; goal: all regions coloured; cost 1 per step. (ii) States: positions of the monkey, the two crates and the bananas, the stacking, and whether the monkey is on a crate or holds the bananas; actions: Walk, Push(crate), Stack(crate1, crate2), Climb, Grasp; goal: Has(Monkey, Bananas); cost 1 per action."
sources: ["AIMA 3e sec. 3.1.1 (well-defined problems), Exercise 3.6"]
---
**(i) Four-colouring a planar map.**

- *States:* an assignment of colours from $\{c_1,c_2,c_3,c_4\}$ to some (or all) of the regions $R_1..R_n$, i.e. a partial colouring.
- *Initial state:* no region coloured.
- *Actions:* choose an uncoloured region (e.g. the next in a fixed order) and assign it a colour that differs from the colours of all its already-coloured neighbours.
- *Transition model:* the new state is the old colouring plus that region's colour.
- *Goal test:* all regions coloured, with no two adjacent regions the same colour.
- *Path cost:* 1 per assignment (irrelevant: all solutions have length $n$).

(As a CSP: variables $R_i$, domains $\{c_1..c_4\}$, constraints $R_i\neq R_j$ for adjacent $i,j$.)

**(ii) Monkey and bananas** (a 3-ft monkey, bananas at 8 ft, two 3-ft crates).

- *States:* the location of the monkey, of crate $C_1$, of crate $C_2$, and of the bananas (fixed: under the bananas = position $B$); whether $C_1$ is on $C_2$ (or vice versa); the monkey's height (on the floor, on one crate, on two crates); whether the monkey holds the bananas.
- *Initial state:* monkey, $C_1$ and $C_2$ at their starting positions on the floor; nothing stacked; the monkey on the floor and empty-handed.
- *Actions* (with preconditions):

$Go(x)$: the monkey walks to $x$, if it is on the floor.

$Push(C,x)$: push crate $C$ to $x$, if the monkey and $C$ are at the same place, the monkey is on the floor and nothing is on $C$.

$Stack(C_i,C_j)$: lift $C_i$ onto $C_j$, if both are at the same place and the monkey is on the floor.

$ClimbUp$ / $ClimbDown$: onto the (top) crate at the monkey's location.

$Grasp(Bananas)$: if the monkey is at $B$ and its height + 3 ft (reach) $\ge$ 8 ft, i.e. standing on the stack of two crates ($3+3+3=9\ge8$).
- *Goal test:* $Has(Monkey,Bananas)$.
- *Path cost:* 1 per action.

A solution: $Go(C_1)$, $Push(C_1,B)$, $Go(C_2)$, $Push(C_2,B)$, $Stack(C_1,C_2)$, $ClimbUp$, $ClimbUp$, $Grasp(Bananas)$.
