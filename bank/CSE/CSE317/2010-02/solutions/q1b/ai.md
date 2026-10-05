---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Information to define a problem: initial state, actions / successor function, goal test, path cost (plus the state space they imply). Types of search problems (by knowledge and observability): single-state (fully observable and deterministic), sensorless (conformant, multiple-state), contingency (non-deterministic or partially observable, needs a conditional plan) and exploration (unknown state space, online)."
sources: ["AIMA 2e sec. 3.6 (searching with partial information) / AIMA 3e sec. 3.1, 4.3-4.5"]
---
**Information needed to define a problem** (the problem formulation):

1. **Initial state:** where the agent starts, e.g. $In(Arad)$.
2. **Actions / successor function:** the actions available in each state and the state each action leads to (the transition model). Together with the initial state this defines the **state space**.
3. **Goal test:** decides whether a state is a goal, either an explicit set of states or a property.
4. **Path cost:** a function giving a numeric cost to each path (the sum of step costs), so that solutions can be compared. The **optimal** solution has the lowest path cost.

(Also the right level of **abstraction** of states and actions.)

**Types of search problems**, depending on what the agent knows and can observe:

| Type | Environment | What the agent searches for |
|:--|:--|:--|
| **Single-state problem** | deterministic, fully observable | the agent knows exactly which state it is in, so the solution is a **sequence of actions** (e.g. route finding, 8-puzzle) |
| **Sensorless (conformant, multiple-state) problem** | deterministic but no percepts | the agent knows only a **set of possible states** (belief state), so it needs a sequence that works from all of them (e.g. the sensorless vacuum world: [Right, Suck, Left, Suck]) |
| **Contingency problem** | non-deterministic and/or partially observable | percepts give new information during execution, so the solution is a **conditional plan** (tree or policy) with branches depending on percepts (e.g. the erratic vacuum: "if the square is still dirty, suck again") |
| **Exploration problem** | unknown state space and actions | the agent must **act to learn** the environment (an online search, e.g. a robot in a new building) |
