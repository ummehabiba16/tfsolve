---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Only 1/3 of the combinations are deadlock free (those in which both processes ask for the same record first): 12 of 36."
sources: ["Tanenbaum MOS 4e, sec. 6.6 (deadlock prevention), exercise on records 1,2,3"]
---
Each process may ask for the records in any of $3!=6$ orders, so there are $6\times6=36$ combinations of request orders. Both processes keep every record until they finish.

**When can a deadlock occur?** If both processes ask for the **same record first**, whoever gets it first proceeds, and the other blocks while holding *nothing*, so the first one runs to completion and there is no deadlock (whatever the remaining order).

If the **first records differ** (say A takes $a_1$ and B takes $b_1\ne a_1$), each will later need the other's first record: A will need $b_1$ and B will need $a_1$ (every process eventually asks for all three), and the interleaving "A holds $a_1$, B holds $b_1$, each waiting for what the other holds" is possible: a deadlock can occur. (All such cases were checked by enumerating the states with a short program.)

**Counting.** Combinations with the same first record: $3$ (choice of the common first record) $\times 2\times 2$ (orders of the other two records for each process) $=12$.

$$\frac{12}{36}=\boxed{\frac13}$$

of the combinations are guaranteed to be deadlock free.
