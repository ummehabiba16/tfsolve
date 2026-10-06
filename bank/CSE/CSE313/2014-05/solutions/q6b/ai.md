---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Recover by preemption, rollback to a checkpoint, or killing processes (in the cycle or others holding the needed resource)."
sources: ["Tanenbaum MOS 4e, sec. 6.4.3 (recovery from deadlock)"]
---
Once a deadlock has been detected, the system must break it:

1. **Recovery through preemption:** temporarily **take a resource away** from its owner and give it to another process, so that the other can finish and release resources; sometimes possible without harm (e.g. suspending the owner of a resource like a printer after the job is finished), but often needs manual intervention and depends on the resource.
2. **Recovery through rollback:** processes take **checkpoints** periodically (state saved to a file). When a deadlock is detected, a process that holds a needed resource is **rolled back** to a checkpoint taken before it acquired the resource; the resource is released and given to a deadlocked process (the rolled-back process must repeat its work, and the later acquisition may be delayed).
3. **Recovery through killing processes:** the crudest, simplest method: **kill one or more processes**: a process in the cycle, repeated until the cycle is broken, or (preferably) a process outside the cycle that holds a needed resource. The victim should be chosen so that it can be rerun with no harm (e.g. a compilation rather than a database update), and by lowest cost (CPU time used, priority).
