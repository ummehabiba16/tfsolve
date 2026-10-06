---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A resource deadlock: every process in a set waits for a resource held by another in the set; conditions: mutual exclusion, hold and wait, no preemption, circular wait."
sources: ["Tanenbaum MOS 4e, sec. 6.1-6.2"]
---
**Resource deadlock.** A set of processes is **deadlocked** if each process in the set is **waiting for a resource that is held by another process of the set**. Since all are blocked, none can release a resource, so they wait forever. (Example: P1 holds the scanner and waits for the printer; P2 holds the printer and waits for the scanner.)

**Conditions that must hold** for a resource deadlock to occur (Coffman):

1. **Mutual exclusion:** each resource is either assigned to exactly one process or available.
2. **Hold and wait:** a process holding resources can request additional ones.
3. **No preemption:** resources already granted cannot be forcibly taken away; they are released only by the owner.
4. **Circular wait:** there is a circular list of two or more processes, each waiting for a resource held by the next one.
