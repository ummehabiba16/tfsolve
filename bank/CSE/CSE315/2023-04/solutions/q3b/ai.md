---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "RISC: few simple, mostly single-cycle, register-to-register instructions with separate LOAD/STORE; CISC: many complex multi-cycle instructions that can work on memory directly. ATmega32 is RISC."
sources: ["EHP ATMega32_Core slides 5-7 (ATmega32 RISC, RISC vs CISC, MULT example)"]
---
| RISC | CISC |
|:--|:--|
| Small set of simple instructions, most execute in **one clock cycle** | Large set including **complex, multi-cycle** instructions |
| **Register-to-register**: memory is accessed only by separate LOAD and STORE instructions | **Memory-to-memory**: LOAD/STORE are built into instructions (operands can be in memory) |
| Emphasis on software; larger code size, fewer cycles per instruction | Emphasis on hardware; smaller code size, more cycles per instruction |

*Example (slides):* multiply two memory values and store the result. CISC: `MULT 2:3, 5:2` (one instruction). RISC: `LOAD A, 2:3`, `LOAD B, 5:2`, `PROD A, B`, `STORE 2:3, A`.

**ATmega32 uses RISC** (131 instructions, mostly single-cycle, about 1 MIPS per MHz). The 8086 is CISC.
