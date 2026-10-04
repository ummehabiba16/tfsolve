---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Von Neumann: one memory and one bus for both code and data (fetch and data access cannot overlap). Harvard: separate program and data memories and buses (fetch and data access in parallel). ATmega32 uses Harvard."
sources: ["EHP ATMega32_Core slides 10-13 (Harvard architecture, single-level pipelining)", "EHP ATMega32_Core slide 4 (MP vs MCU table)"]
---
| Von Neumann | Harvard |
|:--|:--|
| One memory holds **both program and data** | **Separate** program memory and data memory |
| One shared bus (address + data) for instructions and data | Separate buses for instructions and data |
| Instruction fetch and data access **cannot happen at the same time** (the "von Neumann bottleneck") | Next instruction can be fetched **while** the current one reads/writes data, so pipelining is easy |
| Instruction and data words have the same width | Widths can differ (ATmega32: 16-bit instructions, 8-bit data) |
| Simpler, cheaper hardware; e.g. 8086, PCs | More hardware; used in most microcontrollers and DSPs |

**ATmega32 uses the Harvard architecture:** program code is in the 32 KB Flash (16K $\times$ 16) and data is in the 2 KB SRAM (plus register file and I/O), each with its own bus. This is what allows its single-level pipeline: the next instruction is fetched while the current one executes.
