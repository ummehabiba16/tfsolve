---
author: ai
via: chat
status: unverified
summary: 'The four conditions: mutual exclusion, hold and wait, no preemption, circular wait, all must hold simultaneously.'
sources: [Deadlocks slides 8-9, 'Tanenbaum, MOS 4e, sec. 6.2.1']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
1. Mutual exclusion: each resource is either assigned to exactly one process or is free.
2. Hold and wait: a process holding resources may request more.
3. No preemption: resources cannot be forcibly taken, only released voluntarily.
4. Circular wait: a closed chain of processes exists, each waiting for a resource held by the next.

All four must hold at once for a resource deadlock.
