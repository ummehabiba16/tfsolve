---
author: ai
via: chat
status: unverified
summary: 8 processes exist in total (7 created); the count doubles each iteration ($2^3=8$).
sources: [Introduction slides 24-26, 'Tanenbaum, MOS 4e, sec. 2.1.2']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
The loop runs for $i=0,1,2$; at each iteration every existing process forks, so the number of processes doubles: $1 \to 2 \to 4 \to 8$. Hence $2^3 = 8$ processes and 7 forks.

Process tree (each node labelled with the value of $i$ it is created with; the root $P_0$ starts at $i=0$, and a process created at iteration $k$ then runs the loop for $i=k+1,\dots,2$):

```text
P0 (i=0)
|-- A (i=0)
|   |-- (i=1)
|   |   `-- (i=2)
|   `-- (i=2)
|-- (i=1)
|   `-- (i=2)
`-- (i=2)
```
