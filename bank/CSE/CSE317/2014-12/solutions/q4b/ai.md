---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Internal state: remembers unobservable aspects (e.g. a car in the blind spot). Goals: the agent can choose between alternatives by searching or planning for actions that achieve the goal (a taxi at a junction chooses the turn towards the destination). Utility: a numeric measure of desirability, for trading off conflicting goals and uncertainty (faster, safer, cheaper route). Learning: the agent improves its performance from experience, adapting to unknown environments (it learns that braking hard on wet roads skids)."
sources: ["AIMA 3e sec. 2.4.3-2.4.6 (agent types)"]
---
**1. Internal states (memory).** A simple reflex agent reacts only to the current percept. With internal state, the agent keeps track of the parts of the world it **cannot currently see**, using a model of how the world changes.

*Example:* a taxi remembers that a car entered its blind spot, so it does not change lanes even though the car is not visible now.

**2. Goals.** Knowing the current state is not enough to decide what to do. A goal describes desirable situations, so the agent can **search or plan** for action sequences that achieve it, and it can adapt when the goal changes, without rewriting rules.

*Example:* at a road junction, the taxi turns left, right or goes straight depending on where the passenger wants to go.

**3. Utility functions.** Goals are binary (achieved or not). A utility function assigns a **numeric degree of desirability** to states. It allows **trade-offs** between conflicting goals and between likelihood and importance under uncertainty: the agent maximizes expected utility.

*Example:* many routes reach the airport. The utility-based taxi prefers the one that is faster, safer and cheaper, weighing the risk of a traffic jam against the distance.

**4. Learning.** A learning element uses feedback from a critic to improve the performance element over time, so the agent can operate in **initially unknown environments** and become better than its initial knowledge allowed.

*Example:* the taxi learns that braking hard on wet roads causes skidding and starts to brake earlier, or a spam filter learns new spam words from the user's corrections.
