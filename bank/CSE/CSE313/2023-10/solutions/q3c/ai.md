---
author: ai
via: chat
status: unverified
summary: 'Hold-and-wait: make each process request all its resources at once before starting (all-or-nothing). Circular wait: number resources and require requests in increasing order.'
sources: ['Deadlocks slides 34, 36', 'Tanenbaum, MOS 4e, sec. 6.6.2 and 6.6.4']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
- Hold and wait: require each process to request every resource it will need at once, before it starts, and grant only if all are free (all-or-nothing); then it never holds some while waiting for others. (Alternative: to request more, first release all it holds.) Cost: lower utilisation and possible starvation.
- Circular wait: number resource types globally and require requests in strictly increasing order. No cycle can form, because in any blocked set one process holds the highest-numbered resource and cannot be waiting for a lower-numbered one.
