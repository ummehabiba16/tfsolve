---
author: ai
via: chat
status: unverified
summary: Five philosophers alternate thinking and eating; each needs both adjacent forks, shared with neighbours. If all grab their left fork at once, all four deadlock conditions hold.
sources: [IPC slide 50, 'Tanenbaum, MOS 4e, sec. 2.5.1 and 6.2']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Definition: $N$ philosophers sit around a table with one fork between each pair. To eat, a philosopher must hold both its left and right fork, then puts them down to think. Forks are the shared single-use resources.

If every philosopher picks up its left fork first, all four resource-deadlock conditions hold:

- Mutual exclusion: a fork is held by only one philosopher at a time.
- Hold and wait: each holds its left fork while waiting for the right.
- No preemption: a fork is released only by its holder, never seized.
- Circular wait: $0$ waits on $1$'s fork, $1$ on $2$'s, ..., $N-1$ on $0$'s, a cycle.
