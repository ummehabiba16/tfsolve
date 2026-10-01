---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Turing test: an interrogator chats in text with a hidden human and a computer; if they cannot tell which is the machine, it passes. Passing shows intelligent behaviour (weak AI: the machine acts intelligently), but not necessarily real understanding or a mind (Searle's Chinese room, consciousness, the test measures human-likeness and can be gamed)."
sources: ["AIMA 3e sec. 1.1.1, 26.1-26.2"]
---
**The Turing test.** Turing (1950) proposed replacing "Can machines think?" with a behavioural test, the imitation game. A human interrogator holds typed conversations with two hidden respondents, a human and a computer. If the interrogator cannot reliably tell which is the computer (Turing: fooled 30% of the time after 5 minutes), the computer passes. To pass it needs natural language processing, knowledge representation, automated reasoning and machine learning (plus vision and robotics for the total Turing test).

**If the test is passed, does it show that computers exhibit intelligence?**

*Arguments for yes:*

- We attribute intelligence to other people only on the basis of their behaviour (we cannot see their minds). It would be inconsistent to deny it to a machine with indistinguishable behaviour ("polite convention").

- Passing an unrestricted test requires broad language understanding, common-sense knowledge, reasoning and learning: exactly the capacities we call intelligent. So passing shows the machine **acts intelligently** (weak AI).

*Arguments for no (or not necessarily):*

- **Searle's Chinese room**: a system can manipulate symbols to produce correct answers without understanding them; behaviour is not sufficient for understanding or consciousness (strong AI).

- The test measures **human-likeness**, not intelligence: a machine must hide superhuman abilities and imitate human errors; a very intelligent non-human-like system could fail.

- It can be **gamed** in short, restricted conversations by tricks and evasions (ELIZA, "Eugene Goostman"), exploiting the judges' assumptions.

- It ignores perception and physical interaction (unless the total test is used).

**Conclusion.** Passing a demanding, unrestricted Turing test would be strong evidence that a computer exhibits intelligent behaviour, which is what AI (the weak AI position) aims at. It would not by itself prove that the machine has a mind, understanding or consciousness. AI researchers therefore focus on building rational agents rather than on passing the test.
