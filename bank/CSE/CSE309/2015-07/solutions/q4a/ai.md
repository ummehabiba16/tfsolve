---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Cost = 1 + cost of each operand's addressing mode (register 0; memory location, literal #c, indexed c(R), indirect indexed *c(R) cost 1; indirect register *R costs 0): LD R0,x = 2; ADD R1,#3,#2 = 3; LD R2,*200(R0) = 2; ADD R0,R1,R2 = 1; ST x,R0 = 2. Total cost = 10."
sources: ["KMS Chapter 8 slides 3-26 (instruction cost)", "Dragon book 2e sec. 8.2.1-8.2.2"]
---
**Instruction cost** (Dragon book sec. 8.2.2) = 1 (the instruction itself, one word) + the extra cost of the addressing modes of its operands:

| Addressing mode | Form | Extra cost |
|:--|:--|:-:|
| register | `R` | 0 |
| indirect register | `*R` | 0 |
| memory location | `x` | 1 |
| literal | `#c` | 1 |
| indexed | `c(R)` | 1 |
| indirect indexed | `*c(R)` | 1 |

| Instruction | Computation | Cost |
|:--|:--|:-:|
| `LD R0, x` | $1 + 0$ (register) $+ 1$ (memory `x`) | **2** |
| `ADD R1, #3, #2` | $1 + 0$ (`R1`) $+ 1$ (`#3`) $+ 1$ (`#2`) | **3** |
| `LD R2, *200(R0)` | $1 + 0$ (`R2`) $+ 1$ (indirect indexed) | **2** |
| `ADD R0, R1, R2` | $1 + 0 + 0 + 0$ | **1** |
| `ST x, R0` | $1 + 1$ (memory `x`) $+ 0$ (`R0`) | **2** |

**Total cost of the sequence = 2 + 3 + 2 + 1 + 2 = 10.**

(The cost counts the number of words occupied by the code; the time to execute is proportional to it in the model of the textbook.)
