---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Using getReg with R1, R2 (p, q dead on exit; a, b, c, d live): LD R1, a; LD R2, b; ADD R1, R1, R2 (R1 = p); LD R2, c; SUB R1, R2, R1 (R1 = q); LD R2, d (R2 = d and c, for c = d); SUB R1, R1, R2 (R1 = d); at exit ST c, R2; ST d, R1. 9 instructions; a and b are never stored, p and q never reach memory."
sources: ["KMS Chapter 8 slides 51-61 (A Simple Code-Generator, Register and Address Descriptors, getReg)", "Dragon book 2e sec. 8.6 (Example 8.16)"]
---
**Assumptions.**

- Target machine of the text: `LD R, x`, `ST x, R`, `ADD`/`SUB Rdst, Rsrc1, Rsrc2`. Two registers, R1 and R2.
- `p`, `q` are dead on exit; `a`, `b`, `c`, `d` are live on exit.
- Register selection follows the text's `getReg`:
- An operand already in a register is used there.
- Otherwise a free register is taken. If none is free, a register is taken whose variables are all "safe": also in memory, not live, or the result itself.
- The result goes into the register of an operand that has no next use, if there is one.

**Next-use information** (backwards from the exit):

| Statement | Information |
|:--|:--|
| 1: `p = a + b` | p: next use 2; a, b: live on exit |
| 2: `q = c - p` | q: next use 4; c: dead (redefined in 3); p: dead after 2 |
| 3: `c = d` | c: next use 4; d: dead (redefined in 4) |
| 4: `d = q - c` | d: live on exit; q: dead after 4; c: live on exit |

**Code generation with descriptors:**

| Statement | Code | R1 | R2 | Address descriptors that changed |
|:--|:--|:-:|:-:|:--|
| (start) | | | | a: a, b: b, c: c, d: d |
| 1: `p = a + b` | `LD R1, a` | a | | a: a, R1 |
| | `LD R2, b` | a | b | b: b, R2 |
| | `ADD R1, R1, R2` | p | b | a: a; p: R1 |
| 2: `q = c - p` | `LD R2, c` | p | c | b: b; c: c, R2 |
| | `SUB R1, R2, R1` | q | c | p: (none, dead); q: R1 |
| 3: `c = d` | `LD R2, d` | q | d, c | c: R2; d: d, R2 |
| 4: `d = q - c` | `SUB R1, R1, R2` | d | c | q: (none, dead); d: R1; c: R2 |
| exit | `ST c, R2` | d | c | c: c, R2 |
| | `ST d, R1` | d | c | d: d, R1 |

Explanation of the register choices:

- **Statement 1.** Neither operand is in a register, so load them into R1 and R2. The result `p` can replace `a` in R1, because `a`'s value is still in its memory location (`a` is "safe").
- **Statement 2.** `c` is loaded into R2, replacing `b`, which is safe because `b` is in memory. The result `q` replaces `p` in R1, since `p` has no next use.
- **Statement 3** (copy). `d` is loaded into a register, R2, replacing `c`: `c` is about to be redefined, so its old value is not needed. Then `c` is simply recorded as being in R2 too. No instruction is needed for the copy itself.
- **Statement 4.** Both operands are in registers (`q` in R1, `c` in R2). The result `d` goes into R1, since `q` has no next use. R2 now holds only `c`.
- **Exit.** The live variables whose current values are only in registers, `c` (R2) and `d` (R1), are stored. `a` and `b` are already in memory. `p` and `q` are dead and never stored.

**Final code** (9 instructions):

```text
LD  R1, a
LD  R2, b
ADD R1, R1, R2      // p = a + b
LD  R2, c
SUB R1, R2, R1      // q = c - p
LD  R2, d           // c = d   (R2 holds d and c)
SUB R1, R1, R2      // d = q - c
ST  c, R2
ST  d, R1
```
