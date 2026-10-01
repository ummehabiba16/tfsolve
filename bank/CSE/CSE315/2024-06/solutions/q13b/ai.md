---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "RISC keeps the hardware simple (few, single-cycle, register-to-register instructions) and moves complexity to software (more instructions, LOAD/STORE); CISC builds complex multi-cycle, memory-to-memory instructions into hardware so programs are short."
sources: ["EHP ATMega32_Core slides 5-7 (RISC vs CISC, MULT example)"]
---
- **RISC (emphasis on software).** The hardware provides only a small set of simple instructions, mostly **single-clock** and **register-to-register**. Memory is used only through separate LOAD and STORE instructions. A complex operation is built by the **program**, i.e. by the compiler in software, as a sequence of simple instructions. Code is larger, but each instruction is fast, and the transistors are spent on many general-purpose registers. Example: the ATmega32 (131 instructions, about 1 MIPS per MHz).
- **CISC (emphasis on hardware).** The **hardware** implements complex, **multi-clock** instructions that can work memory-to-memory, with LOAD and STORE built into the instruction. Programs are short, but the processor needs complex decoding and microcode, with transistors used to store and execute those complex instructions. Example: the 8086.

Example from the slides, multiplying 2:3 by 5:2:

```text
CISC:  MULT 2:3, 5:2          ; one complex instruction (hardware does it all)

RISC:  LOAD  A, 2:3           ; software spells out each step
       LOAD  B, 5:2
       PROD  A, B
       STORE 2:3, A
```
