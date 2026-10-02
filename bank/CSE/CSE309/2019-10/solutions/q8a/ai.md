---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "With R1-R3 and getReg (t, u, v dead; a, b, c, d live on exit): LD R1, a; LD R2, b; SUB R3, R1, R2 (t; a and b are still needed); ADD R1, R1, R2 (u replaces a); ADD R3, R3, R1 (v replaces t); LD R1, d (R1 = d, a for a = d); LD R2, c; ADD R3, R3, R2 (d = v + c); exit: ST a, R1; ST d, R3. 10 instructions."
sources: ["KMS Chapter 8 slides 51-61 (A Simple Code-Generator, Register and Address Descriptors, getReg)", "Dragon book 2e sec. 8.6 (Example 8.16)"]
---
**Assumptions.**

- Target machine of the text: `LD`, `ST`, `ADD`/`SUB Rdst, Rsrc1, Rsrc2`. Three registers R1, R2, R3.
- `t`, `u`, `v` are dead on exit; `a`, `b`, `c`, `d` are live on exit.
- `getReg` follows the text:
- An operand already in a register is used there.
- An empty register is preferred.
- A register may be overwritten if every variable in it is also in memory, or is dead.
- A result goes into the register of an operand with no next use, if one exists.

**Next-use information:**

| Statement | Information |
|:--|:--|
| 1: `t = a - b` | t: next use 3; a: next use 2; b: next use 2 |
| 2: `u = a + b` | u: next use 3; a: dead after (redefined in 4); b: live on exit, no next use |
| 3: `v = t + u` | v: next use 5; t, u: dead after |
| 4: `a = d` | a: live on exit; d: dead after (redefined in 5) |
| 5: `d = v + c` | d: live on exit; v: dead after; c: live on exit |

**Code with register and address descriptors:**

| Statement | Code | R1 | R2 | R3 | Address descriptors that changed |
|:--|:--|:-:|:-:|:-:|:--|
| (start) | | | | | a: a, b: b, c: c, d: d |
| 1: `t = a - b` | `LD R1, a` | a | | | a: a, R1 |
| | `LD R2, b` | a | b | | b: b, R2 |
| | `SUB R3, R1, R2` | a | b | t | t: R3 |
| 2: `u = a + b` | `ADD R1, R1, R2` | u | b | t | a: a; u: R1 |
| 3: `v = t + u` | `ADD R3, R3, R1` | u | b | v | t: (none); v: R3 |
| 4: `a = d` | `LD R1, d` | d, a | b | v | u: (none); d: d, R1; a: R1 |
| 5: `d = v + c` | `LD R2, c` | d, a | c | v | b: b; c: c, R2 |
| | `ADD R3, R3, R2` | a | c | d | d: R3; v: (none) |
| exit | `ST a, R1` | a | c | d | a: a, R1 |
| | `ST d, R3` | a | c | d | d: d, R3 |

**Reasons for the choices:**

1. `a` and `b` are both needed again in statement 2, so `t` cannot overwrite them; it goes into the empty R3.
2. `u` is placed in R1: `a` has no next use, and its value is in memory anyway.
3. `v` replaces `t` in R3 (`t` has no next use).
4. For the copy `a = d`, `d` is loaded into R1 (`u` is dead), and `a` is then recorded as being in R1 as well. No instruction is needed for the copy itself.
5. `c` is loaded into R2, replacing `b`, which is safely in memory. The result `d` replaces `v` in R3 (`v` has no next use). R1 keeps only `a` now that `d` has a new value.
6. At the exit, the live variables whose current values are only in registers, `a` (R1) and `d` (R3), are stored. `b` and `c` are already in memory, and `t`, `u`, `v` are dead.

**Final code** (10 instructions):

```text
LD  R1, a
LD  R2, b
SUB R3, R1, R2     // t = a - b
ADD R1, R1, R2     // u = a + b
ADD R3, R3, R1     // v = t + u
LD  R1, d          // a = d   (R1 holds d and a)
LD  R2, c
ADD R3, R3, R2     // d = v + c
ST  a, R1
ST  d, R3
```
