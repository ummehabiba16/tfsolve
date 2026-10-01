---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A human interrogator converses in text with a hidden human and a hidden machine; the machine passes if the interrogator cannot reliably tell them apart. Passing needs advances in natural language understanding, common-sense knowledge representation, reasoning and learning (and vision/robotics for the total Turing test)."
sources: ["AIMA 3e sec. 1.1.1 and 26.1"]
---
**The Turing test.** Proposed by Alan Turing (1950) as an operational definition of intelligence (the "imitation game"). A human interrogator exchanges typed messages with two hidden parties, a human and a computer, and may ask anything. If after the conversation the interrogator cannot reliably tell which one is the computer (Turing suggested: fooled 30% of the time in 5 minutes), the computer passes and is said to think. The *total Turing test* adds a video link and handing over objects.

**Advances needed to pass it.**

1. **Natural language processing**: robust understanding and generation of open-ended conversation, including ambiguity, idioms, humour and context over a long dialogue.

2. **Knowledge representation**: a very large body of common-sense knowledge about the everyday world, people and society, and memory of what was said earlier.

3. **Automated reasoning**: using that knowledge to answer novel questions and make consistent inferences, including about beliefs and intentions of others.

4. **Machine learning**: adapting to new topics and the interrogator during the conversation.

5. For the total test, **computer vision** and **robotics** to perceive and manipulate objects.

6. **Human-like behaviour**: modelling human limitations (typing speed, mistakes, not knowing everything), emotions, opinions and a personal history, since being too fast or too accurate reveals a machine.

Current chatbots can fool some judges in short, restricted conversations, but the hardest part remains genuine common-sense understanding (e.g. Winograd-schema questions) in unrestricted, long conversations.
