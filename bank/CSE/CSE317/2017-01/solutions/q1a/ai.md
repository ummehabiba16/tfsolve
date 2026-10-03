---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Two dimensions, thought vs behaviour and human vs rational, give four categories: thinking humanly, thinking rationally, acting humanly, acting rationally. A rational agent acts to maximize its expected performance measure, given its percept sequence and built-in knowledge."
sources: ["AIMA 3e sec. 1.1, 2.2"]
---
**Two dimensions.** Definitions of AI differ in whether they concern (1) **thought processes and reasoning** or **behaviour**, and (2) whether success is measured against **human performance** (fidelity) or against an ideal of **rationality**. Crossing them gives four categories:

| | Human-like | Rational |
|:--|:--|:--|
| **Thinking** | **Thinking humanly**: the cognitive-modelling approach ("machines with minds"; GPS, cognitive science) | **Thinking rationally**: the "laws of thought" approach (logic, correct inference) |
| **Acting** | **Acting humanly**: the Turing-test approach (NLP, knowledge representation, reasoning, learning; vision and robotics for the total test) | **Acting rationally**: the **rational agent** approach |

**Rational agent.** An *agent* perceives its environment through sensors and acts on it through actuators. A **rational agent** chooses, for each possible percept sequence, the action expected to **maximize its performance measure**, given the evidence in the percept sequence and its built-in knowledge.

Rationality is not omniscience: the agent maximizes *expected* performance with the information it has, and it may gather information and learn. This approach is more general than the laws of thought and is mathematically well defined, which is why AIMA (and most modern AI) adopts it.
