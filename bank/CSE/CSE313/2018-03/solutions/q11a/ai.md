---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Deadlock: each process in a set waits for an event only another process of the set can cause. Prevention: negate mutual exclusion (spool), hold and wait (request all at once), no preemption (allow taking resources) or circular wait (global order)."
sources: ["Tanenbaum MOS 4e, sec. 6.2 and 6.6 (deadlock prevention)"]
---
**Deadlock.** A set of processes is **deadlocked** if each process in the set is waiting for an event (typically the release of a resource) that **only another process in the set** can cause. Since all are waiting, none can ever run, release resources or wake another: they wait forever.

**Preventing deadlock** means making sure that at least one of the four necessary conditions can never hold:

| Condition attacked | Method | Drawback |
|:--|:--|:--|
| **Mutual exclusion** | avoid assigning a resource exclusively: e.g. **spool** the output (only the spooler uses the printer) | not possible for all resources (e.g. a table in a database) |
| **Hold and wait** | require each process to **request all its resources at the start** (or release all before asking again) | resources are held unused for long; need to know the needs in advance |
| **No preemption** | allow the system to **take away** a resource (virtualise it) | not possible for some resources (printer mid-job); costs |
| **Circular wait** | give the resources **global numbers** and let a process request only in increasing order (or hold only one at a time) | no order suits everyone; the numbering must be maintained |

Of these, resource ordering is the most practical.
