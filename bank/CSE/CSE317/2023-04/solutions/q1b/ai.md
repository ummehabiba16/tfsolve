---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "In the Turing test a human interrogator chats in text with a hidden human and a hidden machine; the machine passes if the interrogator cannot reliably tell which is which. Passing needs NLP, knowledge representation, reasoning and learning (plus vision and robotics for the total test). Good questions require understanding, common sense and novelty rather than stored answers, e.g. Winograd-schema questions."
sources: ["AIMA 3e sec. 1.1.1 and 26.1"]
---
**The Turing test (Turing, 1950, "imitation game").** A human interrogator communicates by text (teletype) with two hidden respondents, one a human and one a computer. The interrogator asks any questions for a fixed time (Turing suggested 5 minutes). If the interrogator cannot reliably identify which respondent is the machine (Turing's prediction: fooled at least 30% of the time), the computer is said to pass and to be "thinking"/intelligent.

The test avoids defining intelligence directly; it uses an operational, behavioural criterion: indistinguishability from a human. To pass, a computer needs:

- **natural language processing** to communicate,

- **knowledge representation** to store what it knows or hears,

- **automated reasoning** to answer questions and draw new conclusions,

- **machine learning** to adapt and detect patterns.

The **total Turing test** adds a video signal and passing physical objects, so it also needs **computer vision** and **robotics**.

Criticisms: it tests human-likeness, not intelligence (humans make errors, machines must imitate them); it can be gamed by tricks (ELIZA, "Eugene Goostman"); Searle's Chinese room argues behaviour is not understanding. AI researchers therefore focus on underlying principles rather than on passing the test ("aeronautics is not about making machines that fool pigeons").

**Questions that separate real understanding from imitation.** Avoid questions whose answers can be looked up or memorised (facts, arithmetic: a machine could even answer too well). Ask questions that need common sense, context and genuine reasoning about novel situations, for example:

- Winograd-schema questions: "The trophy did not fit into the suitcase because *it* was too big. What was too big?" Changing "big" to "small" flips the answer; this needs real-world understanding, not word statistics.

- A novel, multi-step common-sense question: "If I put my phone in the freezer overnight and then into a bowl of warm water, what will probably happen, and why?"

- Asking it to explain a new joke or analogy, or to reason consistently about something said earlier in the conversation.

Even so, no single question can *prove* intelligence; the interrogator judges consistency of understanding over a whole conversation.
