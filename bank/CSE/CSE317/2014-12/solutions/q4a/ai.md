---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Intelligence: the ability to perceive, learn, reason and act effectively to achieve goals in varied situations. AI: building agents that act intelligently (rationally). Agent: perceives through sensors and acts through actuators. Rationality: choosing the action expected to maximize the performance measure given its percepts and knowledge. Logical reasoning: deriving valid conclusions from premises by sound inference rules. A model-based reflex agent keeps internal state, updated from the last action and the new percept using a model of the world, and then applies condition-action rules (pseudocode given)."
sources: ["AIMA 3e sec. 1.1, 2.1-2.2, 2.4.3 (model-based reflex agents, Fig. 2.11-2.12)"]
---
**Definitions** (5).

- **Intelligence:** the ability to perceive the environment, learn from experience, reason, solve problems and act effectively to achieve goals in new and varied situations.
- **Artificial intelligence:** the study and construction of agents (machines, programs) that behave intelligently, i.e. act rationally (or think or act like humans).
- **Agent:** anything that perceives its environment through sensors and acts on it through actuators. It is described by a mapping from percept sequences to actions.
- **Rationality:** doing the right thing, i.e. choosing the action expected to maximize the performance measure, given the percept sequence and built-in knowledge. It is not omniscience.
- **Logical reasoning:** deriving new sentences (conclusions) that **necessarily follow** from known ones (premises) by sound inference rules, such as modus ponens and resolution. Valid conclusions from true premises are true.

**Model-based reflex agent** (3). It handles **partial observability** by maintaining an **internal state** of the parts of the world it cannot currently see. The state is updated with two kinds of knowledge (a *model*): how the world evolves independently of the agent, and how the agent's own actions affect the world. At each step:

1. update the state from the old state, the last action and the new percept;
2. find the first condition-action rule that matches the state;
3. execute the rule's action.

**Pseudocode** (3).

```text
function MODEL-BASED-REFLEX-AGENT(percept) returns an action
    persistent: state, the agent's current conception of the world state
                model, how the next state depends on the current state and action
                rules, a set of condition-action rules
                action, the most recent action, initially none

    state  <- UPDATE-STATE(state, action, percept, model)
    rule   <- RULE-MATCH(state, rules)
    action <- rule.ACTION
    return action
```
