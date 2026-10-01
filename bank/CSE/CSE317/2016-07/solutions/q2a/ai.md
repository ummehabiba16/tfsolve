---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Map colouring: state = assignment of colours to regions; initial: no region coloured; successor: colour an uncoloured region with a colour not used by its neighbours; goal: all regions coloured; cost 1 per assignment. Monkey and bananas: state = positions of monkey and crates, crate stacking, monkey on floor/crate, holding bananas; actions walk, push, stack, climb, grasp; goal: monkey has bananas; cost 1 per action."
sources: ["AIMA 3e sec. 3.2 and Exercise 3.6"]
---
**(i) Four-colouring a planar map.**

- *States*: a partial assignment of colours from {1, 2, 3, 4} to the regions $R_1,\dots,R_n$ (each region coloured or uncoloured).

- *Initial state*: no region coloured.

- *Successor function*: pick the next uncoloured region (e.g. $R_{k+1}$ in a fixed order) and assign it a colour different from the colours of all its already-coloured neighbours. (Fixing the order keeps the branching factor at most 4.)

- *Goal test*: all regions are coloured (adjacent regions differ, guaranteed by the successor function).

- *Path cost*: 1 per assignment (all solutions have cost $n$, so cost is irrelevant).

**(ii) Monkey and bananas.** The bananas hang from an 8-foot ceiling; the monkey is 3 ft tall and two crates are 3 ft high each, so the monkey must stack both crates under the bananas and climb on top ($3+3+3$ ft $\ge$ reach of 8 ft).

- *States*: (position of monkey, position of crate 1, position of crate 2, crate stacking (crate 1 on crate 2 or vice versa or none), monkey's height: floor / on one crate / on stack, whether the monkey has the bananas). Positions are discrete locations in the room, including "under the bananas".

- *Initial state*: monkey, crates at their initial positions on the floor; monkey on the floor; no bananas.

- *Successor function (actions)*:

- Walk(x): monkey on the floor moves to location x;

- Push(crate, x): monkey and a crate (not under another crate, monkey on floor next to it) move to x;

- Stack(c1, c2): when the monkey is at the location of both crates, put c1 on c2;

- ClimbUp(c) / ClimbDown: get on top of a crate or stack at the monkey's location;

- Grasp(bananas): only if the monkey is on top of the two-crate stack under the bananas.

- *Goal test*: the monkey has the bananas.

- *Path cost*: 1 per action (or effort per action).

A solution: Push(crate1, under-bananas), Walk(crate2), Push(crate2, under-bananas), Stack(crate2, crate1), ClimbUp(stack), Grasp(bananas).
