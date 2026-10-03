---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Aim: an operational, behavioural definition of intelligence: a machine passes if, through a text conversation, a human interrogator cannot tell it from a human, which replaces the vague question 'can machines think?' with a testable one. Importance: it set out the capabilities AI needs (NLP, knowledge representation, reasoning, learning; vision and robotics for the total test), gave a benchmark and focused philosophical debate (Chinese Room); modern AI aims at rational agents rather than imitation."
sources: ["AIMA 3e sec. 1.1.1 and 26.1", "Turing (1950) Computing Machinery and Intelligence"]
---
**Aim of the Turing test.** Turing (1950) proposed replacing the ill-defined question "Can machines think?" with an **operational, behavioural test**. A human interrogator holds a typed conversation with a hidden human and a hidden computer. If the interrogator cannot reliably tell which is which (Turing suggested about 30% misidentification after 5 minutes), the machine is said to behave intelligently. Intelligence is thus judged by **indistinguishable behaviour**, not by internal mechanism or appearance. The text-only channel deliberately ignores physical form.

**Why it is important for AI.**

1. **A definition and a benchmark:** it gave the field a concrete, testable goal for intelligent behaviour.
2. **It identifies the core capabilities** a machine needs: natural language processing, knowledge representation, automated reasoning and machine learning. The *total* Turing test adds computer vision and robotics. These form most of the sub-fields of AI.
3. **It anticipated and answered objections** (theological, mathematical (Goedel), consciousness, the Lady Lovelace objection, and others) and framed the "weak AI versus strong AI" debate (e.g. Searle's Chinese Room).
4. **It inspired** chatbots (ELIZA, Loebner Prize contests) and, today, the evaluation of large language models.

*Caveat:* AI researchers seldom aim to pass the test directly. It rewards imitating human quirks rather than acting rationally, much as "aeronautics is not about making machines that fly so exactly like pigeons that they fool other pigeons".
