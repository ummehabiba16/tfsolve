---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "AVR uses a single-level (2-stage) pipeline: the next instruction is fetched from Flash while the current one executes, giving about 1 instruction per clock. Efficiency comes from the Harvard buses, mostly fixed 16-bit single-word instructions, a 32-register file feeding a single-cycle ALU (read two registers, operate, write back in one cycle), and load/store design; jumps/branches flush the prefetched instruction (extra cycle)."
sources: ["EHP ATMega32_Core slides 10-17 (Harvard, single-level pipelining, register file, single-cycle ALU operation)"]
---
**Pipelining in AVR.** The AVR CPU uses a **single-level pipeline** (two stages: fetch and execute). While instruction $n$ is being executed, instruction $n+1$ is already being **fetched** from program memory. The fetched instruction is not executed until the current one finishes; an instruction that takes 2 cycles delays the next one.

```text
clock:      T1      T2      T3      T4
fetch:      I1      I2      I3      I4
execute:            I1      I2      I3
```

So after the first cycle, one instruction completes **every clock**: about **1 MIPS per MHz**.

**What makes this pipeline efficient**

1. **Harvard architecture:** separate program and data buses, so the fetch of the next instruction never competes with the data access of the current one.
2. **Simple, uniform instructions (RISC):** most instructions are one 16-bit word, so one Flash access fetches a whole instruction, and decoding is simple.
3. **Register file + single-cycle ALU:** 32 general registers are all connected to the ALU. In **one clock** two register operands are read, the ALU operates, and the result is written back to the register file.
4. **Load/store design:** only a few instructions access SRAM (taking 2 cycles), so most instructions are single-cycle register operations.
5. **Branch handling:** a taken jump/branch/call makes the already-fetched instruction useless; it is discarded and the target is fetched, costing an extra cycle. Keeping the pipeline short (only one level) keeps this penalty to one cycle.
