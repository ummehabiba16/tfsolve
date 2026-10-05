---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RISC: a small set of simple, fixed-format instructions, mostly executed in one clock, register-to-register operations with separate load/store, many registers, hard-wired control and pipelining. ATmega16 supports it with 131 mostly single-cycle 16-bit instructions, 32 general registers all connected to a single-cycle ALU, load/store access to SRAM, and a Harvard single-level pipeline (fetch next while executing), giving about 1 MIPS per MHz."
sources: ["EHP ATMega32_Core slides 5-7, 12-15 (RISC, 131 instructions, single-cycle, RISC vs CISC, pipelining, register file, single-cycle ALU)"]
---
**RISC (Reduced Instruction Set Computer) concept**

- A **small set of simple instructions** with a fixed, regular format, so decoding is simple and fast.
- **Most instructions execute in one clock cycle**; complex operations are built from several simple ones.
- **Load/store architecture:** only LOAD and STORE access memory; arithmetic and logic work **register to register**.
- **Many general-purpose registers**, to keep operands on chip.
- Hard-wired control and easy **pipelining**. Emphasis on software (compiler); larger code, but fast execution.

**How the ATmega16 supports a RISC instruction set**

1. **131 instructions**, most of them **single-cycle**; most are one 16-bit word, fetched in one Flash access.
2. **32 general-purpose 8-bit registers** (R0-R31), all directly connected to the ALU. In one clock two registers are read, the ALU operates, and the result is written back.
3. **Load/store:** SRAM is accessed only by LD/ST (and LDS/STS, PUSH/POP) instructions, using the X, Y, Z pointer registers.
4. **Harvard architecture with a single-level pipeline:** separate program and data buses let the next instruction be fetched while the current one executes.

Result: about **1 MIPS per MHz** (e.g. 16 MIPS at 16 MHz).
