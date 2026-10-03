---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Fully observable: chess, crossword puzzle, 8-puzzle. (ii) Episodic: assembly-line part inspection, image classification. (iii) Dynamic: taxi driving, robot soccer. (iv) Stochastic: backgammon (dice), taxi driving, medical diagnosis. (v) Multi-agent: chess (competitive), taxi driving (partly cooperative), soccer."
sources: ["AIMA 3e sec. 2.3.2 (properties of task environments, Fig. 2.6)"]
---
| Property | Meaning | Examples |
|:--|:--|:--|
| **(i) Fully observable** | the sensors give the complete relevant state at each time | chess (with a clock), crossword puzzle, 8-puzzle |
| **(ii) Episodic** | experience is divided into independent episodes; the current decision does not affect future ones | a robot inspecting defective parts on an assembly line; image or spam classification |
| **(iii) Dynamic** | the environment can change while the agent is deliberating | taxi driving, robot soccer, an air-traffic controller |
| **(iv) Stochastic** | the next state is not completely determined by the current state and action | backgammon (dice), taxi driving (traffic), medical diagnosis |
| **(v) Multi-agent** | other agents whose behaviour affects the agent's performance | chess and poker (competitive), taxi driving (partly cooperative: avoiding collisions), soccer (both) |
