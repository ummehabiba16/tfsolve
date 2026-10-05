---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Episodic: experience is divided into independent episodes, each one percept followed by one action, and decisions do not affect later episodes (a robot sorting defective parts on an assembly line, image classification). Strategic: the environment is deterministic except for the actions of other agents (chess, tic-tac-toe). In contrast, sequential environments (driving, chess) make the current decision affect all future ones."
sources: ["AIMA 2e sec. 2.3 / AIMA 3e sec. 2.3.2 (properties of task environments)"]
---
**Episodic task environment.** The agent's experience is divided into atomic **episodes**. In each, the agent perceives and then performs a single action, and the next episode does **not depend** on the actions taken in previous ones. The agent need not think ahead.

*Examples:* a robot on an assembly line that inspects each part and accepts or rejects it, where the current decision does not affect whether the next part is defective; spam filtering; image classification. (Opposite: **sequential**, as in chess or taxi driving, where current decisions affect all future ones.)

**Strategic task environment** (AIMA 2e). The environment is **deterministic except for the actions of other agents**. The next state depends on the current state, the agent's action, and the moves of other, often adversarial, agents, so the agent must anticipate their strategies.

*Examples:* chess, checkers and tic-tac-toe (the board is deterministic, but the opponent's moves are not known in advance); negotiation or auctions.
