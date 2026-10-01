---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Four approaches: thinking humanly, thinking rationally, acting humanly, acting rationally. Rational agent approach: build agents that act to achieve the best expected outcome. Rationality: choosing the action that maximises expected performance given percepts and built-in knowledge. A rational agent should be autonomous so it can learn to compensate for partial or incorrect prior knowledge."
sources: ["AIMA 3e sec. 1.1 and 2.2"]
---
**Four approaches to AI** (thought vs behaviour, human vs rational):

| | Human | Rational |
|:--|:--|:--|
| Thinking | Thinking humanly (cognitive modelling) | Thinking rationally (laws of thought, logic) |
| Acting | Acting humanly (Turing test) | Acting rationally (rational agent) |

**Rational agent approach.** An agent perceives through sensors and acts through actuators. A rational agent acts so as to achieve the best outcome or, under uncertainty, the best **expected** outcome. AI is the study and construction of such agents. Advantages: (1) it is more general than the laws-of-thought approach, because correct inference is only one way of acting rationally (reflexes can be rational too); (2) it is more amenable to scientific development than human-based approaches, because rationality is mathematically well defined and general.

**Rationality.** What is rational at a given time depends on: the performance measure defining success, the agent's prior knowledge of the environment, the actions it can perform, and its percept sequence to date. Rationality maximises *expected* performance, not actual performance (it is not omniscience).

**Rational agent.** For each possible percept sequence, a rational agent selects an action that is expected to maximise its performance measure, given the evidence provided by the percept sequence and whatever built-in knowledge it has. It also gathers information (exploration) and learns from what it perceives.

**Why a rational agent should be autonomous.** An agent that relies only on its designer's prior knowledge lacks autonomy and fails as soon as the environment differs from what the designer expected (e.g. a dung beetle that keeps going through the motions of plugging its nest after the ball has been removed). Since prior knowledge is usually partial or incorrect, a rational agent must **learn** from its own percepts and experience to compensate, and so behave well in a wide range of environments. Initially it may rely on built-in knowledge, but with experience its behaviour should become effectively independent of that knowledge. Hence rationality (maximising expected performance) requires autonomy.
