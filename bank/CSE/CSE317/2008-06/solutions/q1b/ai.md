---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Rationality: for each percept sequence, choosing the action expected to maximize the performance measure, given the percepts and built-in knowledge (not omniscience). (ii) Turing test: a machine is considered intelligent if a human interrogator, communicating only by typed text, cannot reliably tell it apart from a human."
sources: ["AIMA 3e sec. 1.1.1 and 2.2"]
---
**(i) Rationality.** A rational agent does "the right thing": for each possible percept sequence, it selects an action that is expected to **maximize its performance measure**, given the evidence in the percept sequence and whatever built-in knowledge it has. Rationality depends on four things: the performance measure, the agent's prior knowledge, its possible actions, and its percept sequence to date. It maximizes *expected*, not actual, performance, so it is not omniscience.

**(ii) Turing test.** Proposed by Alan Turing (1950) as an operational definition of intelligence. A human interrogator holds a typed conversation with a hidden human and a hidden computer. If the interrogator **cannot reliably tell which is the computer**, the computer passes and is considered to act intelligently. Passing requires natural language processing, knowledge representation, automated reasoning and machine learning. The *total* Turing test adds a video signal and object passing, which also require computer vision and robotics.
