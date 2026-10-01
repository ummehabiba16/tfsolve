---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The goal determines which aspects of the world matter; only then can the problem be formulated (states, actions, goal test, cost) at the right level of abstraction."
sources: ["AIMA 3e sec. 3.1 and Exercise 3.1"]
---
A problem-solving agent first **formulates a goal** (a set of desirable world states, based on the current situation and the performance measure), then **formulates the problem**: which states and actions to consider in order to reach that goal.

Problem formulation must follow goal formulation because the goal tells the agent **which aspects of the world are relevant** and which can be ignored or abstracted. Only then can it choose the state description, the actions, the goal test and the path cost at the right level of detail. Without a goal, the agent would not know what to include, so the state space could be either intractably detailed or missing what matters.

Example: with the goal "reach Bucharest", states can be just cities and actions road trips; the radio, the scenery and steering angles are irrelevant.
