---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Turing test: a human interrogator questions a hidden human and a hidden computer in writing; the computer passes if the interrogator cannot tell them apart. It needs natural language processing, knowledge representation, automated reasoning and machine learning; the total Turing test adds computer vision and robotics."
sources: ["AIMA 3e sec. 1.1.1"]
---
**Turing test.** Proposed by Alan Turing (1950) as an operational definition of intelligence, avoiding a philosophical definition. A human interrogator communicates by typed messages with two hidden parties, one a human and one a computer. The interrogator may ask any questions. If, after the conversation, the interrogator cannot reliably tell which is the computer, the computer passes the test and is considered to be "thinking". Turing predicted that by 2000 a machine could fool a judge 30% of the time in 5 minutes.

There is deliberately no physical interaction, because physically simulating a person is not needed for intelligence.

**Capacities a computer needs to pass the test.**

1. **Natural language processing**: understand questions and produce fluent replies in a human language.

2. **Knowledge representation**: store what it knows and what it learns during the conversation (facts, common sense, context).

3. **Automated reasoning**: use the stored information to answer questions and draw new conclusions consistently.

4. **Machine learning**: adapt to new circumstances and detect and extrapolate patterns.

The **total Turing test** also includes a video signal (to test perceptual abilities) and passing physical objects through a hatch, so the computer also needs:

5. **Computer vision**: to perceive objects.

6. **Robotics**: to manipulate objects and move.

These six areas make up most of AI. In addition, to be indistinguishable from a human, the machine would need human-like limitations (realistic typing speed, occasional mistakes, emotions and opinions), since answering too fast or too accurately would reveal it.
