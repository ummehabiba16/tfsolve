---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Four strategies: ignore (ostrich), detect and recover, dynamic avoidance (safe states/Banker's), prevention (negate a Coffman condition); recovery by preemption, rollback or killing processes."
sources: ["Tanenbaum MOS 4e, sec. 6.1-6.7 (dealing with deadlocks, recovery)"]
---
**Four strategies for dealing with deadlocks** (Tanenbaum):

1. **Ignore the problem** (the *ostrich algorithm*): assume deadlocks are rare; used by UNIX and Windows because the cost of prevention is higher than the occasional reboot.
2. **Detection and recovery:** let deadlocks occur, detect them (e.g. a cycle in the resource graph, or the matrix algorithm) and take action.
3. **Dynamic avoidance:** allocate resources only if the resulting state is **safe** (Banker's algorithm).
4. **Prevention:** structurally negate one of the four conditions (spooling to avoid mutual exclusion, request all resources at once to avoid hold-and-wait, allow preemption, or number the resources to avoid circular wait).

**Ways of recovering from a deadlock**

- **Recovery through preemption:** temporarily take a resource away from its owner and give it to another process (possible only for some resources, often needs manual intervention).
- **Recovery through rollback:** processes write **checkpoints** periodically; when deadlock is detected, a process is rolled back to a checkpoint before it acquired the needed resource, which is then released and given to a deadlocked process.
- **Recovery by killing processes:** the crudest way: kill one process in the cycle (or one not in the cycle that holds a needed resource), and repeat until the deadlock is broken; the victim should be restartable without bad side effects.
