---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Safe: order P3, P2, P1; a request (1,1,1) from P1 cannot be granted because the resulting state is unsafe."
sources: ["Tanenbaum MOS 4e, sec. 6.5.3 (Banker's algorithm for multiple resources)"]
---
**Given:** total $=(3,2,5)$, available $=(1,1,1)$.

$$\text{Need} = \text{Max}-\text{Allocated}$$

| Process | Allocated | Max | Need |
|:-:|:-:|:-:|:-:|
| P1 | 0 0 2 | 3 1 3 | 3 1 1 |
| P2 | 1 0 2 | 1 2 3 | 0 2 1 |
| P3 | 1 1 0 | 2 2 1 | 1 1 1 |

(Check: allocated total $(2,1,4)$ + available $(1,1,1)$ = total $(3,2,5)$.)

**(i) Safety algorithm.** Work $=$ Available $=(1,1,1)$.

1. P3: Need $(1,1,1)\le(1,1,1)$ $\Rightarrow$ P3 can finish; Work $=(1,1,1)+(1,1,0)=(2,2,1)$.
2. P2: Need $(0,2,1)\le(2,2,1)$ $\Rightarrow$ finishes; Work $=(2,2,1)+(1,0,2)=(3,2,3)$.
3. P1: Need $(3,1,1)\le(3,2,3)$ $\Rightarrow$ finishes; Work $=(3,2,3)+(0,0,2)=(3,2,5)$.

All can finish, so the state is **safe**, with the safe sequence $\langle P3, P2, P1\rangle$.

**(ii) Request $(1,1,1)$ from P1.**

- $(1,1,1)\le\text{Need}_{P1}=(3,1,1)$: allowed.
- $(1,1,1)\le\text{Available}=(1,1,1)$: resources are available.

Pretend to grant it: Available $=(0,0,0)$; P1's Allocated $=(1,1,3)$, Need $=(2,0,0)$. Now every process needs something that is not available: P1 needs $(2,0,0)$, P2 needs $(0,2,1)$, P3 needs $(1,1,1)$, and Work $=(0,0,0)$ satisfies none of them, so no process can finish. The new state is **unsafe**, so **the request cannot be granted immediately**; P1 must wait.
