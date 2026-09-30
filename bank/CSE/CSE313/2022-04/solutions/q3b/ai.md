---
author: ai
via: chat
status: unverified
summary: 'Starvation: a runnable process is perpetually denied the CPU/resource by the policy (it waits, idle). Livelock: processes keep running and reacting to each other but make no progress (CPU busy, no work done).'
sources: [Deadlocks slides 40-41, 'Tanenbaum, MOS 4e, sec. 6.7']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
- Starvation: a process is perpetually denied a resource or the CPU because the policy keeps favouring others (e.g. always serving the shortest job while a long job waits forever). The starved process is waiting and idle.
- Livelock: processes are not blocked, they keep running and changing state in response to each other but make no progress (e.g. two processes repeatedly yielding to each other). The CPU is used, but nothing completes.
