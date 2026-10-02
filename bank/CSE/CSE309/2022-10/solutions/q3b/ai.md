---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Register allocation/assignment is critical because registers are the fastest storage but few, instructions on registers are shorter and faster, and choosing optimal allocation is NP-complete. getReg(I) for x = y + z: for y (and z): (1) if y is already in a register, use it; (2) else use an empty register; (3) else pick a register R all of whose variables are safe (also in memory, or the result x, or dead with no next use), otherwise store them first (ST v, R), choosing the R that needs fewest stores. For x: (1) a register holding only x can be used; (2) if y (or z) has no next use and its register holds only y, use that register; (3) otherwise as for y; for a copy x = y, Rx = Ry."
sources: ["KMS Chapter 8 slides 12, 51-61 (Register Allocation, A Simple Code-Generator, Design of Function getReg)", "Dragon book 2e sec. 8.1.4, 8.6.3"]
---
**Why register allocation and assignment is critical (5 marks).**

- Instructions with register operands are **shorter and faster** than those with memory operands. Keeping frequently used values in registers is one of the most important sources of speed.
- There are **few registers**, so the compiler must decide which values live in registers at each point (**allocation**) and which particular register each one uses (**assignment**).
- Finding an optimal assignment is **NP-complete**, and it is complicated by machine conventions (register pairs for multiplication and division, registers reserved for the stack pointer and return values).
- Poor decisions cause many extra loads and stores (spill code).

**Rules used by getReg(I) for $I$: $x = y + z$ (15 marks).** getReg uses the **register descriptors** (which variables each register holds) and the **address descriptors** (where the current value of each variable can be found), plus next-use information.

*Choosing a register for operand $y$* (and likewise for $z$):

1. If $y$ is **currently in a register**, pick that register ($R_y$). No load is needed.
2. Otherwise, if there is an **empty** register, pick it and load $y$ into it (`LD Ry, y`).
3. Otherwise, consider each candidate register $R$. For every variable $v$ held in $R$, it is safe to overwrite $R$ if:
- (a) the address descriptor of $v$ says $v$ is also somewhere else (e.g. in memory); or
- (b) $v$ is $x$, the result being computed, and $x$ is not also the other operand $z$; or
- (c) $v$ is not used later (no next use and not live after $I$).

If none of these holds for some $v$, generate `ST v, R` to save it (a spill). The **score** of $R$ is the number of stores needed. Choose a register with the lowest score.

*Choosing a register for the result $x$:*

- Since $x$ is about to be computed, a register holding **only $x$** is always acceptable.
- If $y$ is **not used after $I$** (no next use, and its value is also in memory or it is dead) and $R_y$ holds only $y$, then $R_y$ can be used for $x$. The same applies to $z$ and $R_z$.
- Otherwise, choose as for an operand (empty register, or the lowest-score register).

*Copy instructions* $x = y$: choose $R_y$ as above, then simply set $R_x = R_y$. That is, record $x$ in $R_y$'s register descriptor and set $x$'s address descriptor to $R_y$ only.

After generating `ADD Rx, Ry, Rz`, update the descriptors: $R_x$ holds only $x$; $x$'s address descriptor contains only $R_x$ (memory is now out of date); and $x$ is removed from all other registers.
