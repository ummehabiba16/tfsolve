---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "AI agent: anything that perceives its environment through sensors and acts on it through actuators (implemented by an agent program). Rationality: choosing actions that maximise the expected performance measure given the percept sequence and built-in knowledge. Autonomy: behaviour determined by the agent's own experience rather than only by the designer's prior knowledge."
sources: ["AIMA 3e sec. 2.1-2.2"]
---
**AI agent.** An agent is anything that can be viewed as **perceiving its environment through sensors** and **acting upon that environment through actuators**. Its behaviour is the *agent function*, mapping percept sequences to actions; an AI agent implements this function with an *agent program* running on some architecture (agent = architecture + program). Example: a robot with cameras and motors; a software agent receiving network packets and sending messages.

**Rationality of an agent.** For each possible percept sequence, a rational agent selects an action that is **expected to maximise its performance measure**, given the evidence of the percept sequence and its built-in knowledge. It depends on (1) the performance measure, (2) prior knowledge of the environment, (3) the available actions, (4) the percept sequence to date. Rational is not omniscient: it maximises expected, not actual, outcome.

**Autonomy of an agent.** An agent is autonomous to the extent that its behaviour is determined by **its own percepts and experience** (learning) rather than relying solely on prior knowledge built in by the designer. A rational agent should learn to compensate for partial or incorrect prior knowledge; e.g. a vacuum cleaner that learns where and when extra dirt appears performs better than one that does not.
