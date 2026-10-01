---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Four approaches along two dimensions (thinking vs acting, human vs rational): acting humanly (Turing test), thinking humanly (cognitive modelling), thinking rationally (laws of thought), acting rationally (rational agent)."
sources: ["AIMA 3e sec. 1.1 (What is AI?)"]
---
Definitions of AI differ along two dimensions: whether they concern **thought processes/reasoning** or **behaviour**, and whether success is measured against **human performance** or against an ideal standard of **rationality**. This gives four approaches.

| | Human-like | Rational |
|:--|:--|:--|
| **Thinking** | Thinking humanly | Thinking rationally |
| **Acting** | Acting humanly | Acting rationally |

**1. Acting humanly: the Turing test approach.** A computer is intelligent if a human interrogator, communicating in writing, cannot tell whether the answers come from a person or a machine. Passing it needs natural language processing, knowledge representation, automated reasoning and machine learning (and for the *total* Turing test, computer vision and robotics). Criticism: it measures imitation of humans, not intelligence itself.

**2. Thinking humanly: the cognitive modelling approach.** Build programs whose internal steps match how humans think, determined by introspection, psychological experiments and brain imaging. If the program's input-output behaviour *and* timing match human behaviour, it is evidence about human mechanisms. This is the field of cognitive science (e.g. Newell and Simon's GPS compared its reasoning traces to humans').

**3. Thinking rationally: the "laws of thought" approach.** Based on logic (Aristotle's syllogisms): represent knowledge in formal logic and derive correct conclusions by inference. Obstacles: informal, uncertain knowledge is hard to state in logic, and solving a problem "in principle" is very different from doing it efficiently in practice.

**4. Acting rationally: the rational agent approach.** An agent perceives and acts; a *rational agent* acts so as to achieve the best (expected) outcome given its percepts and knowledge. This is more general than the laws-of-thought approach (correct inference is only one way to act rationally; reflexes can also be rational) and more amenable to scientific development than human-based approaches, because rationality is mathematically well defined. Most of modern AI, and AIMA, follows this approach.
