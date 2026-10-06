---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Safe: need = C - A; safe sequence P2, P1, P3, P4 with work growing from (0,1,1) to (9,3,6)."
sources: ["Tanenbaum MOS 4e, sec. 6.5.3 (Banker's algorithm); Stallings OS, deadlock avoidance example"]
---
Totals $R=(9,3,6)$; available $V=(0,1,1)$. Need $=C-A$:

| Process | Allocation $A$ | Claim $C$ | Need $C-A$ |
|:-:|:-:|:-:|:-:|
| P1 | 1 0 0 | 3 2 2 | 2 2 2 |
| P2 | 6 1 2 | 6 1 3 | 0 0 1 |
| P3 | 2 1 1 | 3 1 4 | 1 0 3 |
| P4 | 0 0 2 | 4 2 2 | 4 2 0 |

(Check: allocated column sums $(9,2,5)$ + available $(0,1,1)$ $=(9,3,6)=R$.)

**(i) Yes**, I agree: the system is in a **safe state**.

**(ii) Proof: a safe sequence.** Work $=V=(0,1,1)$.

1. P2: need $(0,0,1)\le(0,1,1)$ $\Rightarrow$ finishes; Work $=(0,1,1)+(6,1,2)=(6,2,3)$.
2. P1: need $(2,2,2)\le(6,2,3)$ $\Rightarrow$ finishes; Work $=(6,2,3)+(1,0,0)=(7,2,3)$.
3. P3: need $(1,0,3)\le(7,2,3)$ $\Rightarrow$ finishes; Work $=(7,2,3)+(2,1,1)=(9,3,4)$.
4. P4: need $(4,2,0)\le(9,3,4)$ $\Rightarrow$ finishes; Work $=(9,3,4)+(0,0,2)=(9,3,6)=R$.

All processes can finish in the order **P2, P1, P3, P4**, so the state is safe (no deadlock can result if the OS lets the processes run in a suitable order).
