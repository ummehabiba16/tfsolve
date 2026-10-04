---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Approach i is RISC (load/store, register-to-register, simple one-cycle instructions); approach ii is CISC (one complex memory-to-memory instruction). Differences: instruction complexity/cycles, memory access only by LOAD/STORE vs in any instruction, code size and hardware emphasis. ATmega32 is RISC."
sources: ["EHP ATMega32_Core slides 5-7 (ATmega32 RISC, RISC vs CISC with the MULT example)"]
---
**Identification**

- **Approach i is RISC.** Memory is touched only by separate `LOAD` and `STORE` instructions; the arithmetic (`ADD R3, R1, R2`) works **only on registers**. Each instruction is simple and can execute in one clock cycle, so the job needs **4 instructions**.
- **Approach ii is CISC.** A single complex instruction `ADD @c, @a, @b` reads two operands **from memory**, adds them and writes the result **to memory**. The load and store are built into the instruction, which takes several clock cycles.

**Three key differences**

| | RISC | CISC |
|:--|:--|:--|
| Instructions | Few, simple, fixed format; mostly **single-cycle** | Many, complex, variable length; **multi-cycle** |
| Memory access | **Load/store architecture**: only LOAD/STORE access memory; operations are register-to-register | Operations can work **directly on memory** (memory-to-memory); LOAD/STORE built in |
| Code size and design emphasis | More instructions per task (**larger code**); emphasis on **software** (compiler), many registers, easy pipelining | Fewer instructions (**smaller code**); emphasis on **hardware** (microcode, complex decoder) |

**ATmega32 uses RISC** (131 mostly single-cycle instructions, 32 general-purpose registers, about 1 MIPS per MHz). The 8086 is a CISC processor.
