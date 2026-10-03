---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Turing test: a human judge, communicating only by text, cannot tell the computer from a person (needs NLP, knowledge representation, automated reasoning, machine learning). Total Turing test: adds a video signal and passing objects, so it also needs computer vision and robotics. These skills (knowing, reasoning, learning, perceiving, acting) are exactly what a rational agent needs to choose good actions. Rational-agent approach: more general than laws of thought (correct inference is only one way to act rationally) and easier to analyse scientifically (a well-defined, measurable standard)."
sources: ["AIMA 3e sec. 1.1.1 and 1.1.4"]
---
**Turing test versus total Turing test (6).**

- **Turing test** (Turing, 1950): a human interrogator asks written questions over a teletype or text channel, to a person and to a computer. The computer passes if the interrogator cannot reliably tell which is the machine. Physical simulation of a person is deliberately avoided. To pass, the computer needs **natural language processing** (to communicate), **knowledge representation** (to store what it knows or hears), **automated reasoning** (to answer questions and draw new conclusions) and **machine learning** (to adapt to new circumstances and extrapolate patterns).
- **Total Turing test:** adds a **video signal**, so the interrogator can test the subject's perceptual abilities, and the chance to **pass physical objects** through a hatch. It additionally requires **computer vision** (to perceive objects) and **robotics** (to manipulate objects and move about).

**How these skills allow an agent to act rationally (4).** A rational agent must choose the action that maximizes its expected performance given its percepts and knowledge. The Turing-test skills are exactly the components for this:

- it **perceives** the environment (vision, language);
- it **represents** what it knows about the world;
- it **reasons** about the consequences of its actions to choose good ones;
- it **learns** from experience, to improve and to handle new situations;
- it **communicates** and **acts** (language, robotics).

So the abilities needed to pass the test are the abilities needed for rational behaviour in a complex world.

**Advantages of the rational-agent approach (4).**

1. **More general** than the laws-of-thought approach. Correct logical inference is only one way to act rationally. Sometimes there is no provably correct action, yet something must be done (e.g. a reflex: pulling the hand off a hot stove).
2. **Amenable to scientific development.** Rationality is mathematically well defined (maximize expected utility, i.e. the performance measure) and completely general, so agent designs can be analysed, compared and proved to achieve it. Human behaviour, in contrast, is tuned to one specific environment and is the product, in part, of a complex and largely unknown evolutionary process.
