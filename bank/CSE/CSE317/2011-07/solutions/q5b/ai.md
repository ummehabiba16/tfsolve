---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "An agent perceives its environment through sensors and acts through actuators. Learning agent: performance element (chooses actions), critic (evaluates against a fixed performance standard and gives feedback), learning element (improves the performance element), problem generator (suggests exploratory actions). Human analogues: motor and behaviour (performance), feelings of pain or pleasure and judgment (critic), learning in the brain (learning element), curiosity and play (problem generator)."
sources: ["AIMA 3e sec. 2.1 and 2.4.6 (learning agents, Fig. 2.15)"]
---
**Agent.** Anything that perceives its environment through **sensors** and acts upon it through **actuators**. It is characterized by an agent function from percept sequences to actions.

**Components of a learning agent, compared with a human being.**

| Component | Role | Human analogue |
|:--|:--|:--|
| **Performance element** | selects external actions from the percepts (the whole "agent" in other designs) | the skills and behaviour by which a person acts (walking, talking, driving) |
| **Critic** | tells the learning element how well the agent is doing with respect to a **fixed performance standard** | built-in feedback: pain and pleasure, hunger, a teacher's or parent's praise, self-evaluation against goals |
| **Learning element** | uses the critic's feedback to **improve** the performance element | learning in the brain: forming habits, updating knowledge from experience |
| **Problem generator** | suggests **exploratory** actions that lead to new, informative experiences | curiosity, play and experimentation: a child trying things out, a scientist doing experiments |

(Sensors and actuators correspond to the human senses and muscles.)
