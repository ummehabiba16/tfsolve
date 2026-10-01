---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A simple reflex agent maps the current percept to an action by condition-action rules; a model-based reflex agent keeps an internal state, updated with a model of how the world evolves and how actions affect it, so it works in partially observable environments."
sources: ["AIMA 3e sec. 2.4.2-2.4.3"]
---
**Simple reflex agent.** Chooses its action using **only the current percept**, through condition-action rules ("if car-in-front-is-braking then initiate-braking"). It keeps no memory of past percepts.

```text
function SIMPLE-REFLEX-AGENT(percept):
    state  <- INTERPRET-INPUT(percept)
    rule   <- RULE-MATCH(state, rules)
    return rule.ACTION
```

It works only if the correct decision can be made from the current percept, i.e. the environment is **fully observable**. In partially observable environments it can fail or loop forever.

**Model-based reflex agent.** Keeps an **internal state** that summarises the part of the world it cannot currently see. It updates this state using a **model** of the world: (1) how the world evolves independently of the agent, and (2) how the agent's own actions change the world. It then applies condition-action rules to the *state*, not to the raw percept.

```text
function MODEL-BASED-REFLEX-AGENT(percept):
    persistent: state, model, rules, action (most recent)
    state  <- UPDATE-STATE(state, action, percept, model)
    rule   <- RULE-MATCH(state, rules)
    action <- rule.ACTION
    return action
```

| | Simple reflex | Model-based reflex |
|:--|:--|:--|
| Uses | current percept only | percept history (through internal state) |
| Memory | none | internal state + world model |
| Environment | fully observable | also partially observable |
| Failure mode | infinite loops when information is hidden | only as good as its model |

**Example (vacuum world / driving).** A vacuum robot with only a dirt sensor and a location sensor: a simple reflex agent with rules "if dirty then suck; if in A then right; if in B then left" will keep moving between A and B forever even when both are clean, because it cannot remember that it already cleaned the other square. A model-based agent remembers "A is clean, B is clean" and can stop (NoOp).

In driving, to change lanes the agent must know where the other cars are even when they are not visible in the current camera frame (blind spot); a model-based agent tracks them from previous percepts, a simple reflex agent cannot.
