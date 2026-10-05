---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Goal formulation first fixes which outcomes are desired, which limits the objectives and the actions worth considering; problem formulation then decides which states and actions, and at what abstraction, to consider in order to reach that goal. Without a goal, there is no basis for choosing relevant states, actions, goal test or path cost."
sources: ["AIMA 3e sec. 3.1 (problem-solving agents)"]
---
A problem-solving agent first performs **goal formulation**: based on the current situation and its performance measure, it decides what it wants (for example, "be in Bucharest tomorrow" while on holiday in Arad). Goals organize behaviour by **limiting the objectives** and hence the actions the agent needs to consider.

Only then can **problem formulation** be done: deciding which **states and actions** to consider, and at what level of abstraction, *given that goal*. To reach Bucharest, the useful states are "in city X" and the useful actions are "drive to the next city". Moving the steering wheel by one degree is far too detailed, and the agent's own thoughts are irrelevant.

Without a goal, the agent has no criterion for what is relevant: every detail of the world would have to be modelled, and there would be no goal test or meaningful path cost. Hence problem formulation must follow goal formulation.
