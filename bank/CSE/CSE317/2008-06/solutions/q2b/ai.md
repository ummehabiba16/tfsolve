---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A contingency problem arises when the environment is non-deterministic and/or partially observable, so the agent cannot know in advance the exact results of its actions, but can get percepts during execution; the solution is a conditional plan (a tree with branches depending on percepts), not a fixed sequence, e.g. the erratic vacuum world: [Suck, if State = 5 then [Right, Suck] else []]."
sources: ["AIMA 2e sec. 3.6 / AIMA 3e sec. 4.3 (searching with non-deterministic actions, AND-OR search)"]
---
**Contingency problem.** The agent **cannot predict** exactly which state its actions will lead to, because:

- the environment is **non-deterministic** (an action has several possible outcomes), and/or
- it is **partially observable**,

but the agent **receives percepts during execution** that reveal what actually happened.

A fixed sequence of actions is therefore not enough. The solution is a **contingency (conditional) plan**: a tree of actions with **branches that depend on percepts** ("if the square is still dirty, then suck again"). It is found by AND-OR search: OR nodes are the agent's choices, and AND nodes cover every possible outcome. Planning and acting are often interleaved.

*Example: the erratic vacuum world.* $Suck$ sometimes also cleans the adjacent square, or deposits dirt on a clean square. From state 1 (agent in the left square, both squares dirty), a solution is:

$$[\,Suck,\ \textbf{if }State=5\textbf{ then }[Right,\ Suck]\ \textbf{else }[\,]\,]$$

That is: suck, and if the right square is still dirty, move right and suck there.
