---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Perfect rationality would need omniscience and unlimited computation; real environments are partially observable, stochastic, dynamic and unknown, so we can only design agents that maximise expected performance (bounded rationality)."
sources: ["AIMA 3e sec. 2.2.2 (Omniscience, learning, autonomy) and 1.1.4"]
---
A *perfectly* rational agent would always choose the action that actually gives the best outcome. This is difficult (practically impossible) because:

1. **Omniscience is impossible.** Rationality maximises *expected* performance given the percepts; the agent cannot know the actual outcome of its actions in advance (e.g. a plane part falling on you while crossing the road).

2. **Partial observability and uncertainty.** Environments are partially observable, stochastic and dynamic, so the agent never has complete, certain information.

3. **Incomplete prior knowledge.** The designer cannot give the agent full knowledge of an unknown environment; it must learn, and learning takes time and mistakes.

4. **Limited computation.** Computing the optimal action exactly is often intractable (e.g. chess game tree $\approx35^{100}$ nodes); decisions must be made in real time.

Therefore we aim for **bounded (limited) rationality**: act as well as possible given the available information and computational resources.
