---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Rationality maximizes expected performance given the percepts and knowledge so far; omniscience means knowing the actual outcome of actions, which is impossible. A rational agent can have a bad outcome (struck by a falling cargo door while crossing a street sensibly) without being irrational."
sources: ["AIMA 3e sec. 2.2.2 (omniscience, learning and autonomy)"]
---
- **Rationality:** choosing the action that maximizes the **expected** performance measure, given the percept sequence so far and the agent's built-in knowledge. It depends only on information available to the agent.
- **Omniscience:** knowing the **actual** outcome of every action in advance and acting accordingly. This is impossible in reality.

*Example:* I look both ways, see no traffic, and cross the street. A cargo door falls from a passing plane and hits me. Crossing was still **rational**, because nothing in my percepts predicted it. Only an omniscient agent could have avoided it. So rationality maximizes *expected*, not *actual*, performance. It may include gathering information (looking before crossing), but it does not require perfect foresight.
