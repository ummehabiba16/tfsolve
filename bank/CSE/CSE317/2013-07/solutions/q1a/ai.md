---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "stack(x,y): pre holding(x), clear(y); effect on(x,y), clear(x), armempty, not holding(x), not clear(y). unstack(x,y): pre on(x,y), clear(x), armempty; effect holding(x), clear(y), not on(x,y), not clear(x), not armempty. pickup(x): pre ontable(x), clear(x), armempty; effect holding(x), not ontable(x), not clear(x), not armempty. putdown(x): pre holding(x); effect ontable(x), clear(x), armempty, not holding(x)."
sources: ["AIMA 3e sec. 10.1.3 (blocks world)", "Rich & Knight, Artificial Intelligence, sec. 13.2"]
---
(The paper prints "unstuck"; the handwritten correction says unstack.)

| Action | Preconditions | Effects (add, and delete as $\neg$) |
|:--|:--|:--|
| **stack(x, y)**: put the held block x on block y | $holding(x)\land clear(y)$ | $on(x,y)\land clear(x)\land armempty\land\neg holding(x)\land\neg clear(y)$ |
| **unstack(x, y)**: lift block x off block y | $on(x,y)\land clear(x)\land armempty$ | $holding(x)\land clear(y)\land\neg on(x,y)\land\neg clear(x)\land\neg armempty$ |
| **pickup(x)**: lift block x from the table | $ontable(x)\land clear(x)\land armempty$ | $holding(x)\land\neg ontable(x)\land\neg clear(x)\land\neg armempty$ |
| **putdown(x)**: put the held block x on the table | $holding(x)$ | $ontable(x)\land clear(x)\land armempty\land\neg holding(x)$ |

(For $stack$ and $unstack$, $x\neq y$, and $y$ is a block, not the table.)
