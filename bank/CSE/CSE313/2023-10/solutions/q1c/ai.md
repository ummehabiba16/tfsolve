---
author: ai
via: chat
status: unverified
summary: An unsafe state cannot be guaranteed to let all processes finish but no process is necessarily blocked yet; a deadlock state already has a set of permanently blocked processes. Unsafe is a warning, deadlock is the failure.
sources: [Deadlocks slides 25-27, 'Tanenbaum, MOS 4e, sec. 6.5.2']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
- Unsafe state: no ordering guarantees completion, yet no process is necessarily blocked; with luck (processes releasing before reaching their maxima) it may still complete. It is a state from which deadlock is possible.
- Deadlock state: a concrete set of processes each wait on resources held by another in the set, none can proceed. It has already happened and is, by definition, unsafe.
