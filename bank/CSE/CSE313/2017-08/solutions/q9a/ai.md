---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Preemptable resources can be taken away without harm (memory, CPU); non-preemptable ones cannot (printer, CD recorder); the four deadlock conditions are mutual exclusion, hold and wait, no preemption, circular wait."
sources: ["Tanenbaum MOS 4e, sec. 6.1 and 6.2"]
---
- A **preemptable resource** can be **taken away** from the process owning it **with no ill effects**, e.g. **memory** (can be swapped to disk) and the **CPU**.
- A **non-preemptable resource** cannot be taken away without making the computation fail, e.g. a **CD recorder** in the middle of burning a disc, a **printer** in the middle of a job, a locked database record. Deadlocks involve non-preemptable resources.

**The four conditions for deadlock**

1. **Mutual exclusion:** each resource is either assigned to exactly one process or is available.
2. **Hold and wait:** processes holding resources granted earlier can request new resources.
3. **No preemption:** previously granted resources cannot be forcibly taken away; the owner must release them explicitly.
4. **Circular wait:** there must be a circular chain of two or more processes, each waiting for a resource held by the next member of the chain.

All four must hold for a (resource) deadlock to occur.
