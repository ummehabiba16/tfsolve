---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Register descriptor: which variables are in each register; address descriptor: where the current value of each variable is (register, memory); spilling: storing a register's value to memory to free it. With two registers the given code needs no spill: R0={t}, R1={u}; then R0={v}; finally R0={d} and d is stored. Spilled variable: none."
sources: ["KMS Chapter 8 slides 51-61 (A simple code generator)", "Dragon book 2e sec. 8.6.1-8.6.2"]
---
**Definitions** (Dragon book sec. 8.6.1).

- **Register descriptor:** for every register, the variables whose *current value* is in it (initially all registers are empty). Used by `getReg` to find a free register.
- **Address descriptor:** for every variable, the *locations* (register, memory address, stack) where its current value can be found. Used to decide how to access an operand.
- **Spilling:** when no register is free, the value in some register is **stored to memory** (a `ST` instruction), so that the register can be reused; the variable moved out is the *spilled variable*. A good choice is a register whose value is dead or also in memory, otherwise one that is needed farthest in the future.

**Assumptions.** Two registers `R0`, `R1`. `t`, `u`, `v` are temporaries that are dead after their last use; `a`, `b`, `c` are in memory; `d` is live on exit from the block (so it is stored). The generated code is the code given in the question.

| Statement | Code generated | Register descriptor | Address descriptor | Spilled variable |
|:--|:--|:--|:--|:--|
| `t := a - b` | `MOV a, R0` | $R_0$: `a` | `a`: memory, $R_0$ | |
| | `SUB b, R0` | $R_0$: `t` | `t`: $R_0$ (only) | none |
| `u := a - c` | `MOV a, R1` | $R_0$: `t`; $R_1$: `a` | `a`: memory, $R_1$; `t`: $R_0$ | |
| | `SUB c, R1` | $R_0$: `t`; $R_1$: `u` | `t`: $R_0$; `u`: $R_1$ | none |
| `v := t + u` | `ADD R1, R0` | $R_0$: `v`; $R_1$: `u` | `v`: $R_0$; `u`: $R_1$; `t`: nowhere (dead) | none |
| `d := v + u` | `ADD R1, R0` | $R_0$: `d`; $R_1$: free (`u` dead) | `d`: $R_0$ | |
| | `MOV R0, d` | $R_0$: `d` | `d`: memory and $R_0$ | none |

**Explanation.** (1) `getReg` picks `R0` for `t = a - b`; after the `MOV`/`SUB`, `t` exists only in `R0`. (2) `u = a - c` needs a second register: `R1` is free, so no spill. (3) `v = t + u` is computed as `ADD R1, R0`, i.e. $R_0 \leftarrow R_0 + R_1$; the register for the result is `R0` because `t` is dead after this use (its register can be reused without storing it). (4) `d = v + u` reuses `R0` (holding `v`, dead afterwards); at the end of the block the live variable `d` is stored with `MOV R0, d`.

**Spilled variable: none.** All four statements fit in the two registers because each overwritten register held a value that was dead afterwards. A spill would be needed only if a third value had to be kept in registers at the same time, or if `t` or `v` were live after the block (then they would be stored first).
