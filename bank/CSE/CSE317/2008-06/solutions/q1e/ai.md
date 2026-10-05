---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Goal-based agent: keeps a model plus goal information and chooses actions (by search or planning) that achieve the goal; goals are binary (happy or unhappy). Utility-based agent: uses a utility function mapping states (or sequences) to real numbers, and chooses the action with maximum expected utility; it can trade off conflicting goals and handle uncertainty about which goals can be achieved. Goal-based is a special case (utility 1 or 0)."
sources: ["AIMA 3e sec. 2.4.4-2.4.5 (goal-based and utility-based agents, Fig. 2.13-2.14)"]
---
**Goal-based agent.**

- Keeps track of the world state (a model) and also has **goal** information describing desirable situations, e.g. "reach the destination".
- Chooses actions by considering the future: "What will happen if I do $A$? Will it achieve my goal?" It uses **search and planning** to find action sequences that reach a goal.
- **Flexible:** the knowledge that supports its decisions is explicit, so changing the goal changes the behaviour without rewriting condition-action rules.
- *Example:* a taxi that turns left at a junction because the destination is to the left.

**Utility-based agent.**

- Goals are only a crude **binary** distinction (goal reached or not). A **utility function** $U(s)$ maps a state (or a sequence of states) to a real number: the degree of "happiness".
- Chooses the action that maximizes **expected utility**: $\sum_{s'}P(s'\mid a)U(s')$. It is rational under uncertainty.
- Handles **conflicting goals** (speed versus safety) through trade-offs, and handles several goals of which none can be achieved with certainty, by weighing the likelihood of success against importance.
- *Example:* a taxi choosing among many routes that all reach the destination: the quicker, safer, cheaper and more comfortable one has higher utility.

**Comparison.**

| | Goal-based | Utility-based |
|:--|:--|:--|
| Evaluation of states | goal / not goal (binary) | real-valued utility |
| Decision | any action sequence achieving the goal | the action of maximum expected utility |
| Conflicting goals, uncertainty | cannot trade off | trades off rationally |
| Relationship | a special case ($U=1$ for goals, 0 otherwise) | a generalization |
| Complexity | simpler | needs a utility function and probabilities |
