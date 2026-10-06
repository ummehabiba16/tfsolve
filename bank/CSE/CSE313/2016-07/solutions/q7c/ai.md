---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Safety: nothing bad happens (never more than one person buys milk); liveness: something good eventually happens (if milk is needed, someone buys it)."
sources: ["Anderson and Dahlin, OSPP, ch. 5 (synchronisation: too much milk)"]
---
In the **"Too Much Milk"** problem two roommates must make sure that the fridge never ends up with too much milk (nobody buys it twice) nor without milk.

- **Safety property** ("nothing bad ever happens"): **at most one person buys milk** (never both buying at the same time, i.e. no "too much milk"). This is the **mutual exclusion** property of the solution.
- **Liveness property** ("something good eventually happens"): **if there is no milk, someone eventually buys it** (nobody waits forever, no deadlock or starvation). A solution that never lets anybody buy milk would be perfectly *safe* but would violate liveness, so a correct solution needs both.
