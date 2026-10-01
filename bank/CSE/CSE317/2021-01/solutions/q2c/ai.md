---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A simple reflex agent maps the current percept to an action with condition-action rules; a goal-based agent keeps a model and searches/plans for actions that achieve an explicit goal, so it is more flexible. A learning agent suits dynamic environments because its critic and learning element update its knowledge when the environment changes (e.g. a taxi learning new traffic patterns or a spam filter learning new spam)."
sources: ["AIMA 3e sec. 2.4.2, 2.4.4 and 2.4.6"]
---
**Simple reflex agent vs goal-based agent.**

| Simple reflex agent | Goal-based agent |
|:--|:--|
| Acts only on the **current percept** using condition-action rules | Keeps an internal state (model) and an explicit **goal** |
| No memory, no model of the future | Considers the future: "what will happen if I do A, will it achieve my goal?" |
| No search or planning | Uses search/planning to find action sequences reaching the goal |
| Fast but inflexible: to change behaviour, rewrite the rules | Flexible: change the goal and the same agent behaves differently |
| Works only in fully observable environments | Works in partially observable environments too |

Example: at a junction a reflex taxi has a rule like "if light green then go straight"; a goal-based taxi decides to turn left, right or go straight depending on whether that brings it closer to the passenger's destination.

**"A learning agent is suitable for a dynamic environment."** In a dynamic environment the world changes over time, so knowledge built in by the designer becomes outdated. A learning agent has:

- a **performance element** that chooses actions,

- a **critic** that compares outcomes with a fixed performance standard,

- a **learning element** that changes the performance element using this feedback,

- a **problem generator** that suggests exploratory actions.

So when the environment changes, poor results are detected by the critic and the agent updates its rules/model automatically, instead of failing until a designer reprograms it. It also starts working in initially unknown environments and becomes more autonomous.

**Example.** A spam filter: spammers keep changing their messages (a dynamic, adversarial environment). A fixed rule-based filter quickly becomes useless. A learning filter treats the user's "mark as spam / not spam" actions as feedback from the critic, retrains its classifier (learning element) and so keeps up with new kinds of spam. Similarly, an automated taxi learns that a road is now congested at certain hours and changes its route choice.
