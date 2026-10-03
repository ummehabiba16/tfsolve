---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Goal formulation first decides which states are desirable, which tells the agent which actions and states matter; problem formulation then chooses the states and actions at the right level of abstraction for reaching that goal; without a goal there is no criterion for what to model. Definitions: agent (perceives through sensors, acts through actuators), agent program (implements the agent function on the architecture), autonomy (behaviour determined by its own experience rather than built-in knowledge), learning agent (performance element + learning element + critic + problem generator)."
sources: ["AIMA 3e sec. 3.1 (problem-solving agents), sec. 2.1-2.4"]
---
**Why problem formulation must follow goal formulation.** **Goal formulation** decides which world states are desirable (e.g. "be in Bucharest tomorrow"), based on the current situation and the performance measure. The goal limits what the agent is trying to achieve, and so which actions it needs to consider. **Problem formulation** then decides which states and actions to model, and at what level of abstraction, for *reaching that goal*: for example, driving between cities rather than turning the steering wheel by one degree.

Without a goal, the agent has no basis for choosing a relevant state space, action set, goal test or path cost. Every detail of the world would be equally relevant. So the goal must come first, and the problem is formulated around it.

**Definitions.**

- **Agent:** anything that perceives its environment through **sensors** and acts on it through **actuators**. Its behaviour is described by the *agent function*, a mapping from percept sequences to actions.
- **Agent program:** the concrete implementation of the agent function, running on the physical **architecture** (agent = architecture + program). It takes the current percept as input and returns an action.
- **Autonomy:** the extent to which an agent's behaviour is determined by its **own experience** (learning) rather than by its designer's built-in knowledge. An autonomous agent learns to compensate for partial or incorrect prior knowledge.
- **Learning agent:** an agent that improves with experience. It has four components: the **performance element** (selects actions), the **learning element** (makes improvements), the **critic** (gives feedback on how well the agent is doing against a fixed performance standard) and the **problem generator** (suggests exploratory actions that lead to new, informative experiences).
