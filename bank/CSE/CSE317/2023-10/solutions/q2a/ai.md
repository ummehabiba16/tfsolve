---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Goal formulation decides which outcomes matter and so which aspects of the world are relevant; problem formulation then decides which actions and states to consider. Without the goal we would not know what to include or abstract away."
sources: ["AIMA 3e sec. 3.1 (Problem-solving agents) and Exercise 3.1"]
---
A problem-solving agent works in four steps: **goal formulation**, **problem formulation**, **search**, **execution**.

- In **goal formulation** the agent decides what it wants to achieve, based on the current situation and its performance measure (e.g. "be in Bucharest tomorrow"). The goal is a set of world states, and it limits the objectives the agent is trying to achieve.

- In **problem formulation** the agent decides what **states** and **actions** to consider, i.e. the level of abstraction, given the goal (e.g. driving from one town to the next, not "move the steering wheel one degree").

Problem formulation must follow goal formulation because the goal determines which aspects of the world are relevant and which can be ignored or abstracted away. Only after knowing the goal can the agent decide what to put into the state description, which actions are useful, and what the goal test and path cost are. If we formulated the problem first we would not know what to include: the state space could be either too detailed (intractable) or missing what matters.

Example: if the goal is "reach Bucharest", the state needs only the current city and actions are road trips between cities; the weather, the radio station or the scenery are irrelevant. If the goal were "arrive with a full tank and minimal toll", the state would need fuel level and toll information.

(In practice there may be a cycle: after trying to solve the problem the agent may refine the goal and reformulate.)
