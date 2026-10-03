---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Omniscience: knowing the actual outcome of actions (impossible); e.g. crossing the street when a cargo door falls from a plane. Autonomy: behaviour determined by the agent's own experience rather than its designer's prior knowledge; e.g. a vacuum agent that learns where dirt appears. Rationality: choosing the action that maximizes expected performance given the percepts and knowledge; e.g. looking both ways before crossing."
sources: ["AIMA 3e sec. 2.2 (rationality, omniscience, learning, autonomy)"]
---
**Omniscience.** An omniscient agent knows the *actual* outcome of its actions and can act accordingly. That is impossible in reality.

*Example:* I cross an empty street after looking both ways, and a cargo door falls from a passing airliner and flattens me. My action was not omniscient, but it was still rational: I could not have known.

**Rationality.** A rational agent selects, for each percept sequence, the action expected to **maximize its performance measure**, given the evidence in the percept sequence and its built-in knowledge. Rationality maximizes *expected* performance; omniscience maximizes *actual* performance.

*Example:* looking both ways before crossing (information gathering) is rational. A vacuum agent that cleans dirty squares and moves to the other square is rational under the "one point per clean square per time step" measure.

**Autonomy.** An agent is autonomous to the extent that its behaviour depends on its **own experience** (learning), rather than on prior knowledge built in by its designer. Autonomy lets it compensate for partial or incorrect prior knowledge.

*Example:* a vacuum agent that learns to predict where and when new dirt will appear does better than one that only follows fixed rules. A dung beetle that keeps "plugging" its nest even after the dung ball is removed shows a lack of autonomy.
