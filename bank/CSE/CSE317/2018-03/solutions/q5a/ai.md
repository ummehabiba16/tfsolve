---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Two dimensions (thinking vs acting, human vs rational) give four approaches: thinking humanly (cognitive modelling), thinking rationally (laws of thought), acting humanly (Turing test), acting rationally (rational agent). Laws of thought: build intelligence on formal logic (syllogisms) to derive correct conclusions. Obstacles: informal or uncertain knowledge is hard to state formally, and solving a problem in principle differs from solving it in practice (combinatorial explosion)."
sources: ["AIMA 3e sec. 1.1 (What is AI?)"]
---
**Four approaches (4).** Definitions of AI vary along two dimensions: thought processes and reasoning versus behaviour, and success measured against **human** performance versus against **rationality** (an ideal).

| | Human-like | Rational |
|:--|:--|:--|
| **Thinking** | *Thinking humanly*: cognitive modelling; build programs that think like people (GPS, cognitive science) | *Thinking rationally*: the **laws of thought**; correct inference by logic |
| **Acting** | *Acting humanly*: the Turing test approach | *Acting rationally*: the **rational agent** approach |

**The "laws of thought" approach (4).** Aristotle's syllogisms ("Socrates is a man; all men are mortal; therefore Socrates is mortal") were the first attempt to codify "right thinking": irrefutable reasoning that always gives correct conclusions from correct premises. The **logicist** tradition in AI hopes to build intelligent systems by writing knowledge in formal logic and using logical inference to solve problems. In principle, any solvable problem described in logical notation can then be solved.

**Main obstacles (4).**

1. **Formalizing knowledge is hard.** Much real knowledge is informal or uncertain, and only partly true. Stating it in formal logical notation is difficult; logic is ill-suited to uncertainty.
2. **In principle versus in practice.** Being able to solve a problem in principle does not mean solving it in practice. Even a few hundred facts can exhaust any computer's resources unless there is guidance on which reasoning steps to try (combinatorial explosion).
3. Also, correct inference is not all of rationality. Sometimes one must act without any provable best action (reflex actions, decisions under uncertainty).
