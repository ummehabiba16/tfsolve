---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Agent: anything that perceives its environment through sensors and acts on it through actuators. Agent program: the concrete implementation of the agent function running on the architecture. Rationality: choosing actions that maximise expected performance given percepts and knowledge. Autonomy: behaviour determined by the agent's own experience, not only by built-in knowledge."
sources: ["AIMA 3e sec. 2.1, 2.2 and 2.4"]
---
**Agent.** Anything that can be viewed as **perceiving** its environment through **sensors** and **acting** upon that environment through **actuators**. Mathematically, its behaviour is described by the *agent function*, a mapping from every possible percept sequence to an action. Examples: a human (eyes, ears / hands, legs), a robot (cameras / motors), a software agent (keystrokes, files / screen output, network packets).

**Agent program.** The concrete implementation of the agent function that runs on the agent's physical architecture: agent = architecture + program. It takes the current percept as input (the agent function takes the whole percept history), keeps any memory it needs, and returns an action, e.g. a table-driven, simple reflex or model-based program.

**Rationality.** For each possible percept sequence, a rational agent selects an action that is expected to maximise its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge it has. What is rational depends on the performance measure, prior knowledge, available actions and the percept sequence to date. Rationality is not omniscience: it maximises expected, not actual, outcome.

**Autonomy.** An agent is autonomous to the extent that its behaviour is determined by **its own percepts and experience** (learning) rather than relying only on the prior knowledge built in by its designer. A rational agent should be autonomous, learning to compensate for partial or incorrect prior knowledge (e.g. a vacuum cleaner that learns where dirt usually appears).
