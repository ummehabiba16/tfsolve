---
author: ai
via: chat
status: unverified
summary: Impose a global total ordering on resource types and require every process to request resources only in increasing order.
sources: [Deadlocks slide 36, 'Tanenbaum, MOS 4e, sec. 6.6.4']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Number all resource types $1..n$. A process may request resource $j$ only if it currently holds no resource $k \ge j$, i.e. resources must be acquired in strictly increasing order of their number.

Then no circular wait can form: in any set of blocked processes, one holds the highest-numbered resource involved and cannot be waiting for a lower-numbered one, so the cycle is broken.
