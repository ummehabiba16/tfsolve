---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "LD R2, 100(R1): R2 = contents(100 + contents(R1)), cost 2. ST *100(R1), R2: contents(contents(100 + contents(R1))) = R2, cost 2. ADD R1, R1, #100: R1 = R1 + 100, cost 2."
sources: ["KMS Chapter 8 slides 3-26 (target machine, instruction cost)", "Dragon book 2e sec. 8.2.1-8.2.2"]
---
Cost of an instruction = 1 + the added cost of the addressing modes of its operands: register 0, memory location 1, literal `#c` 1, indexed `c(R)` 1, indirect register `*R` 0, indirect indexed `*c(R)` 1 (Dragon book sec. 8.2.2).

| Instruction | Effect | Cost |
|:--|:--|:-:|
| `LD R2, 100(R1)` | $R2 = contents(100 + contents(R1))$: load the word at memory address $100 + R1$ into `R2` | $1 + 0 + 1 = $ **2** |
| `ST *100(R1), R2` | $contents(contents(100 + contents(R1))) = R2$: store `R2` at the address held in the word at address $100 + R1$ (indirect indexed destination) | $1 + 1 + 0 = $ **2** |
| `ADD R1, R1, #100` | $R1 = R1 + 100$: add the constant 100 to `R1` | $1 + 0 + 0 + 1 = $ **2** |

**Total** for the three: 6.
