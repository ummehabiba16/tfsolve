---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Request (3,2,3,3) from P5 satisfies Request <= Need and Request <= Available, but granting it leaves Available (3,1,2,1) with no process able to finish: unsafe, so it is not granted."
sources: ["Tanenbaum MOS 4e, sec. 6.5.3 (Banker's algorithm for multiple resources)"]
---
Resources: A 15, B 6, C 9, D 10 instances. Allocation (current) and Max are given; computed (script):

| Process | Allocation | Max | Need $=$ Max $-$ Alloc |
|:-:|:-:|:-:|:-:|
| P0 | 2 0 2 1 | 9 5 5 5 | 7 5 3 4 |
| P1 | 0 1 1 1 | 2 2 3 3 | 2 1 2 2 |
| P2 | 4 1 0 2 | 7 5 4 4 | 3 4 4 2 |
| P3 | 1 0 0 1 | 3 3 3 2 | 2 3 3 1 |
| P4 | 1 1 0 0 | 5 2 2 1 | 4 1 2 1 |
| P5 | 1 0 1 1 | 4 4 4 4 | 3 4 3 3 |

Total allocated $=(9,3,4,6)$, so **Available $=(15,6,9,10)-(9,3,4,6)=(6,3,5,4)$**. (The present state is safe: e.g. order P1, P2, P3, P4, P5, P0.)

**Request $(3,2,3,3)$ from P5.**

1. $\text{Request}\le\text{Need}_{P5}=(3,4,3,3)$: yes.
2. $\text{Request}\le\text{Available}=(6,3,5,4)$: yes.
3. **Pretend to grant it:** Available $=(3,1,2,1)$; $\text{Alloc}_{P5}=(4,2,4,4)$; $\text{Need}_{P5}=(0,2,0,0)$.
4. **Safety test** with Work $=(3,1,2,1)$: P0 $(7,5,3,4)$ no; P1 $(2,1,2,2)$: $2>1$ in D, no; P2 $(3,4,4,2)$ no; P3 $(2,3,3,1)$: $3>1$ in B, no; P4 $(4,1,2,1)$: $4>3$ in A, no; P5 $(0,2,0,0)$: $2>1$ in B, no. **No process can finish** $\Rightarrow$ the new state is **unsafe**.

**Answer: the request should NOT be granted** (P5 must wait), even though the resources are available, because granting it could lead to deadlock.
