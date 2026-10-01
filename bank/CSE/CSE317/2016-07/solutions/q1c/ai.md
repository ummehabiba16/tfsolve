---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A goal-based agent uses a model and an explicit goal to search/plan for action sequences, with fixed knowledge supplied by the designer. A learning agent adds a critic, learning element and problem generator so it improves its performance element (which can be goal-based) from experience; it is more autonomous and works in unknown or changing environments."
sources: ["AIMA 3e sec. 2.4.4 and 2.4.6"]
---
**Goal-based agent.** Keeps an internal state (model of the world) and has explicit **goal** information describing desirable situations. It considers the future ("what will happen if I do action A? will it achieve my goal?") and uses search or planning to find action sequences that reach the goal. Its knowledge (model, goal) is represented explicitly and can be modified, so it is more flexible than a reflex agent.

**Learning agent.** Consists of a **performance element** (which selects actions; can itself be a goal-based agent), a **critic** (feedback with respect to a fixed performance standard), a **learning element** (improves the performance element) and a **problem generator** (exploratory actions).

| | Goal-based agent | Learning agent |
|:--|:--|:--|
| Knowledge | Fixed model and goal given by the designer | Improves its model, rules, utilities from experience |
| Feedback | Only goal test: achieved or not | Critic compares behaviour with a performance standard |
| Exploration | No; follows its plan | Problem generator suggests informative actions |
| Environment | Works if the model is correct (known environment) | Can start in unknown/changing environments |
| Autonomy | Limited by the designer's knowledge | Becomes more autonomous over time |
| Errors | Repeats the same mistakes | Learns from mistakes |
| Complexity | Simpler | More components, needs data/time to learn |

They are not alternatives: a learning agent can use a goal-based agent as its performance element, and the learning element can then improve its world model ("what my actions do") and its search heuristics. Example: a goal-based taxi plans routes using a fixed map; a learning taxi also learns traffic patterns and which routes are actually fast.
