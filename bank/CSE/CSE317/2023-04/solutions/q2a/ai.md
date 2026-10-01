---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A learning agent has a performance element (selects actions), a critic (compares behaviour with a fixed performance standard and gives feedback), a learning element (improves the performance element) and a problem generator (suggests exploratory actions). A model-based agent only uses a fixed model to track state; a learning agent improves its model and rules from experience."
sources: ["AIMA 3e sec. 2.4.6 (Figure 2.15)"]
---
**Block diagram of a general learning agent.**

```text
  Performance standard
          |
          v
      [ Critic ] <------------------------ [ Sensors ] <---- percepts
          |  feedback                           |
          v                                     v
  [ Learning element ] --- changes ---> [ Performance element ]
          |            <-- knowledge ---        |
          |  learning goals                     |
          v                                     v
  [ Problem generator ] -- exploratory --> [ Actuators ] ----> actions
                            actions
  (everything above is the agent; percepts come from and actions go to the ENVIRONMENT)
```

(In words: percepts from the sensors go to the critic and to the performance element; the critic sends feedback to the learning element; the learning element changes the performance element and sets learning goals for the problem generator; the performance element and the problem generator choose actions that the actuators carry out.)

**Components.**

1. **Performance element**: what we previously called the whole agent; it takes percepts and decides on actions (it can be a reflex, model-based, goal-based or utility-based agent).

2. **Critic**: observes the world and tells the learning element how well the agent is doing with respect to a **fixed performance standard** (outside the agent, so the agent cannot change it to suit itself). Percepts alone do not say whether the agent is doing well; e.g. checkmate is only good because the standard says so.

3. **Learning element**: responsible for making improvements. Using the critic's feedback and knowledge of the performance element, it decides how to modify the performance element (rules, model, utility estimates) so it does better in future.

4. **Problem generator**: suggests exploratory actions that lead to new, informative experiences, even if suboptimal in the short run, so that the agent discovers better actions in the long run (exploration vs exploitation).

Example: automated taxi. The performance element drives; after a sharp lane change other drivers honk, the critic reports this is bad, the learning element formulates a rule "avoid sudden lane changes"; the problem generator may suggest trying brakes on a different road surface to learn their effect.

**Learning agent vs model-based agent.**

| Model-based (reflex) agent | Learning agent |
|:--|:--|
| Keeps internal state using a world model and condition-action rules supplied by the designer | Starts with possibly incomplete knowledge and improves it from experience |
| Model and rules are fixed; mistakes are repeated | Critic and learning element modify the model, rules or utilities |
| No explicit notion of being evaluated | Has a performance standard and feedback |
| No exploration | Problem generator explores |
| Works only in environments the designer anticipated | Can operate in initially unknown environments and becomes more autonomous |

Any agent (including a model-based one) can be the performance element of a learning agent; the learning components can improve every part of it, e.g. learn "how the world evolves" and "what my actions do".
