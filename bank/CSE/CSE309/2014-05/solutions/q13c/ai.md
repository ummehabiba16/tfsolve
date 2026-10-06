---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Assuming three registers and that t, u, v are dead after use: t := a - b: LD R1,a; LD R2,b; SUB R1,R1,R2 (R1 = t). u := a - c: LD R3,a; LD R2,c; SUB R3,R3,R2 (R3 = u). v := t + u: ADD R1,R1,R3 (R1 = v). d := v + u: ADD R1,R1,R3 (R1 = d); ST d,R1."
sources: ["KMS Chapter 8 slides 51-61 (A simple code generator, getReg)", "Dragon book 2e sec. 8.6.1-8.6.3"]
---
**Register descriptor:** for each register, the names whose current value it holds. **Address descriptor:** for each name, the locations (register, memory) where its current value can be found (Dragon book sec. 8.6.1).

**Assumptions.** Three registers `R1`, `R2`, `R3` are available; `a`, `b`, `c`, `d` are in memory and live at the end of the block; `t`, `u`, `v` are temporaries, dead after their last use. For a statement $x := y\ op\ z$ the code generator calls `getReg`, loads $y$ and $z$ into registers if they are not there, and emits `OP Rx, Ry, Rz`; a register holding a dead value (or a copy that is also in memory) can be reused without a store.

| Statement | Code generated | Register descriptor | Address descriptor |
|:--|:--|:--|:--|
| `t := a - b` | `LD R1, a` | R1: `a` | `a`: memory, R1 |
| | `LD R2, b` | R1: `a`; R2: `b` | `b`: memory, R2 |
| | `SUB R1, R1, R2` | R1: `t`; R2: `b` | `t`: R1; `a`: memory; `b`: memory, R2 |
| `u := a - c` | `LD R3, a` | R1: `t`; R2: `b`; R3: `a` | `a`: memory, R3 |
| | `LD R2, c` | R1: `t`; R2: `c`; R3: `a` | `c`: memory, R2; `b`: memory only |
| | `SUB R3, R3, R2` | R1: `t`; R2: `c`; R3: `u` | `t`: R1; `u`: R3; `c`: memory, R2 |
| `v := t + u` | `ADD R1, R1, R3` | R1: `v`; R2: `c`; R3: `u` | `v`: R1; `u`: R3; `t`: gone (dead) |
| `d := v + u` | `ADD R1, R1, R3` | R1: `d`; R2: `c`; R3: free | `d`: R1; `v`, `u`: gone (dead) |
| (end of block) | `ST d, R1` | R1: `d` | `d`: memory, R1 |

**Notes.** (1) In `t := a - b`, $R_1$ first holds `a`; since `a` is also in memory, overwriting $R_1$ by `t` loses nothing. (2) Loading `c` into `R2` overwrites `b`, which is still in memory, so no store is needed. (3) For `v := t + u` the register of `t` (dead afterwards) receives the result; for `d := v + u` the register of `v` receives the result. (4) At the end of the block the live variable `d` is stored; `t`, `u`, `v` are dead and need no store. The code uses three registers and no spill.
