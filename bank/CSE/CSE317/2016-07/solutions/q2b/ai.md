---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Real-world states are too detailed to search; abstraction removes irrelevant detail from states and actions, giving a smaller, tractable state space whose solutions can be expanded into real solutions. Example: route finding in Romania uses only the current city, not weather, fuel or steering."
sources: ["AIMA 3e sec. 3.1.2 (Formulating problems)"]
---
**Why abstraction is needed.** The real world is absurdly complex: a complete description of the state would include the weather, the radio, every pedestrian, every steering-wheel angle, etc. Searching such a state space is impossible. **Abstraction** is removing detail from the representation of states and actions, keeping only what is needed to solve the problem. It makes the state space small enough to search.

A good abstraction is **valid** (every abstract solution can be expanded into a solution in the detailed world) and **useful** (carrying out the abstract actions is easier than the original problem).

**Example: driving from Arad to Bucharest.**

- *State abstraction*: the state is just "In(Arad)", "In(Sibiu)", ...: 20 cities instead of everything about the car and its surroundings.

- *Action abstraction*: "drive from Arad to Sibiu" instead of thousands of low-level actions (turn the wheel 1 degree, press accelerator ...).

The search then has only 20 states; any abstract route (Arad, Sibiu, Rimnicu Vilcea, Pitesti, Bucharest) can be carried out in reality by a driver without further planning.
