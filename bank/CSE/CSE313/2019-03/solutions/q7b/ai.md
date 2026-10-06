---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Proposed problem: the operating-theatre problem (surgeons, nurses and surgical kits must be acquired together); IPC issues: mutual exclusion, rendezvous, multi-resource deadlock, starvation, priorities, termination."
sources: ["Tanenbaum MOS 4e, sec. 2.5 (classical IPC problems), ch. 6 (deadlocks)"]
---
**New problem: the operating-theatre problem.**

A hospital has $S$ surgeon threads, $N$ nurse threads and $K$ sterile surgical kits ($K<S$). An operation can start only when **one surgeon, two nurses and one kit** are all present in the theatre. Routine operations repeat forever; **emergency patients** may arrive at any time and must be operated on before routine ones. After the operation the kit is sent for **sterilisation** (done by a single sterilizer thread, which takes time) before it can be used again. At the end of each operation, the surgeon, the nurses and the kit leave together.

**IPC issues in this problem (the problem is not solved here):**

1. **Mutual exclusion:** shared state (the counts of waiting surgeons/nurses, kits, the theatre) must be updated atomically: race conditions.
2. **Rendezvous / synchronisation of several parties:** the operation starts only when all four (surgeon, 2 nurses, kit) have met; like a *barrier* for a group of unequal composition.
3. **Multiple-resource allocation and deadlock:** if every surgeon grabs a nurse and a kit one by one, we can reach a state in which each surgeon holds one resource and waits for another (hold-and-wait, circular wait). Resources must be acquired together or in a fixed order.
4. **Producer-consumer / bounded buffer:** used kits go to the sterilizer (producer) and clean kits come back (consumer).
5. **Priorities and starvation:** emergency cases have priority, so routine operations may starve; a fair queueing or ageing rule is needed (**liveness**).
6. **Priority inversion** if a low-priority thread holds a nurse that an emergency needs.
7. **Termination / shutdown:** all threads must stop correctly at the end of the day without leaving threads blocked forever.
