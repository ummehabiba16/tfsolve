---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "True. A natural-language agent cannot observe the speaker's mental state (intentions, beliefs, meaning), and language is ambiguous, so it must infer what is meant from incomplete evidence; the relevant state of the world is therefore only partially observable."
sources: ["AIMA 3e sec. 2.3.2 (properties of task environments), ch. 22-23 (natural language)"]
---
**True.** For an agent communicating in natural language, the relevant "state of the world" includes the **beliefs, intentions and meanings** in the minds of the other speakers. These cannot be perceived directly. The agent sees only the words (the percepts), which are:

- **ambiguous:** "I saw her duck" has several readings;
- **incomplete:** things are left implicit and depend on context or common knowledge;
- **sometimes misleading:** speakers may lie or be mistaken.

So the agent must **infer** the hidden state (what is meant, what the other agent wants) from partial evidence. Its sensors do not give complete access to the relevant state of the environment, so it is operating in a **partially observable** environment. (Typically it is also multi-agent, stochastic and sequential.)
