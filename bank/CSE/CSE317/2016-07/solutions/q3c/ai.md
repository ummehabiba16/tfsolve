---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "A contingency problem arises when percepts during execution give new information (partially observable or nondeterministic environments), so the solution is a conditional plan. Example: erratic vacuum world where Suck may deposit dirt on a clean square: [Suck, Right, if dirty then Suck]. Compared with planning blind (sensorless), it executes fewer actions on average because it skips unnecessary ones; compared with a fully observable deterministic version it may need more steps in the worst case."
sources: ["AIMA 2e sec. 3.6 (Searching with partial information)", "AIMA 3e sec. 4.3 (Nondeterministic actions, contingency plans)"]
---
**Contingency problem.** The agent cannot predict exactly what will happen (the environment is partially observable and/or actions are nondeterministic), but it can obtain new information from its sensors **during execution**. The solution is therefore a **contingency (conditional) plan**, a tree of actions with if-then-else branches on percepts, and planning is often interleaved with acting.

**Example: erratic vacuum world.** Two squares A and B, the agent is in A and both are dirty. Action Suck cleans the current square but, when applied to a dirty square, sometimes also cleans the adjacent one, and when applied to a **clean** square sometimes **deposits** dirt (Murphy's law). The agent can sense whether its current square is dirty. A solution:

```text
[Suck, Right, if Dirty(B) then [Suck] else []]
```

After the first Suck, B may already be clean, so whether to suck again in B is decided only after perceiving B.

**Does it require fewer steps than the original problem?** Compare it with the original (fully observable, deterministic) problem and with the sensorless (conformant) version:

- Versus the **sensorless** formulation (which must guarantee success without any percepts), yes: the conformant plan must contain every action that might be needed in any outcome, e.g. [Suck, Right, Suck] and, with Murphy's law, it can never safely suck an already clean square, so in some versions no conformant plan exists at all. The contingency plan executes an action only when the percept shows it is needed, so on average fewer actions are executed (in the outcome where Suck cleaned both squares, it executes only Suck, Right).

- Versus the fully observable **deterministic** problem: not fewer. In the worst case it needs the same number of actions ([Suck, Right, Suck]) or more, since unexpected outcomes may require extra repair actions, and the plan itself (a tree) is larger and more expensive to compute.

So sensing lets a contingency plan avoid unnecessary actions, but uncertainty means it cannot be shorter than the plan for the same problem without uncertainty.
