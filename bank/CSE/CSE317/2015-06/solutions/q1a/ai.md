---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Table-driven: looks up the whole percept sequence in a table (correct but needs an astronomically large table, so it is infeasible). Simple reflex: condition-action rules on the current percept only (small and fast, but fails when the environment is partially observable, and can loop). Agents with memory (model-based reflex): keep internal state updated by a model of how the world evolves and what actions do, so they handle partial observability."
sources: ["AIMA 3e sec. 2.4 (agent programs)"]
---
| | **Table-driven agent** | **Simple reflex agent** | **Agent with memory** (model-based reflex) |
|:--|:--|:--|:--|
| Decides from | the **entire percept sequence**, looked up in a table | the **current percept** only | current percept + **internal state** |
| Mechanism | `table[percepts]` gives the action | condition-action rules: "if car-in-front-is-braking then initiate-braking" | updates its state with a model of how the world evolves and how its actions affect it, then applies rules |
| Size | $\sum_{t=1}^{T}|P|^t$ entries: astronomically large (chess: more than $10^{150}$) | small | moderate |
| Works when | in principle always (it implements any agent function) | the environment is **fully observable** | partially observable environments |
| Weakness | infeasible to build, store or learn; no autonomy | wrong decisions when information is missing; infinite loops (randomization helps) | needs a correct world model |

**Comparison.** The table-driven agent shows that an agent function *can* be implemented, but not practically. The simple reflex agent is compact and fast, but blind to anything not in the current percept. An agent with memory combines the reflex agent's efficiency with internal state, so it can act correctly when the world is only partially observable (for example, it remembers that the other square was already cleaned, or where the car in the blind spot was).
