---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RISC pros: simple, fixed-size, mostly single-cycle instructions, easy pipelining and decoding, many registers, less hardware/power. Cons: more instructions per task (larger code), more burden on the compiler, memory only through load/store. ATmega32 is RISC (131 instructions, 32 registers): with Harvard pipelining it runs about 1 instruction per clock, giving high speed at low clock and low power."
sources: ["EHP ATMega32_Core slides 5-7, 12-15 (ATmega32 RISC, RISC vs CISC, pipelining, register file)"]
---
**Advantages of RISC over CISC**

1. **Simple instructions, mostly one clock each**, fixed size and format, so decoding is simple and fast.
2. **Easy pipelining:** uniform instructions flow through the pipeline with few stalls.
3. **Many general-purpose registers** and register-to-register operations, so fewer slow memory accesses.
4. **Less hardware** (no microcode for complex instructions): smaller, cheaper chips with lower power, which suits microcontrollers.

**Disadvantages**

1. **More instructions per task:** one CISC instruction (e.g. `MULT 2:3, 5:2`) becomes several RISC instructions (LOAD, LOAD, PROD, STORE), so **code size is larger**.
2. **More work for the compiler/programmer** to use registers well and schedule instructions.
3. Memory can be accessed only through LOAD/STORE; complex addressing must be built from several instructions.

**ATmega32 uses RISC** (131 instructions, most single-cycle, 32 general-purpose 8-bit registers).

**How it aids performance.** Simple 16-bit instructions are fetched in one Flash access and, with the Harvard buses and single-level pipeline, one instruction is fetched while the previous one executes. The register file feeds the ALU so that an operation reads two registers and writes the result in one cycle. Together this gives about **1 MIPS per MHz**, so the ATmega32 is fast even at low clock rates and uses little power.
