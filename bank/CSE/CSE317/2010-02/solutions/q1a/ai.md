---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "An omniscient agent knows the actual outcomes of its actions in advance. It is not what rationality requires and is impossible in practice; rationality maximizes expected performance given the percepts. An omniscient agent would act optimally, so it would also be rational, but a rational agent need not be omniscient."
sources: ["AIMA 3e sec. 2.2.2"]
---
**Omniscient agent.** An agent that knows the **actual outcome** of every action it might take, and acts accordingly. Such an agent is impossible in reality.

**Is it a rational agent?** Rationality and omniscience are different things.

- A **rational** agent maximizes **expected** performance, given its percept sequence and built-in knowledge. It may still suffer bad outcomes it could not foresee. For example, it crosses the road after looking, and a falling cargo door hits it: the action was still rational.
- An omniscient agent would always choose the action with the best actual outcome, so its behaviour would also be rational: with perfect knowledge, the expected and actual outcomes coincide.

So **omniscience is sufficient but not necessary** for rationality. The definition of rationality deliberately does not require it. We cannot blame an agent for failing to take into account what it could not perceive. Instead, rationality requires *information gathering* (looking before crossing) and *learning*, to make the best use of what can be known.
