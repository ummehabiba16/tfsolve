---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "N-bit processor: its ALU (and registers) handle n bits of data at a time, e.g. 8085 = 8-bit, 8086 = 16-bit, 80386 = 32-bit. Superscalar processor: has several execution pipelines and issues more than one instruction per clock cycle, e.g. Pentium (U and V integer pipes)."
sources: ["MHE Intro slides ('What is an n-bit processor?', evolution of microprocessors)", "Brey, The Intel Microprocessors, Ch. 18 (Pentium: superscalar, U and V pipelines)"]
---
**i. N-bit processor**

A processor is called **n-bit** if it can operate on **n bits of data at the same time**. The ALU does the operations on data, so the ALU (and general-purpose register) width decides the size. The internal data path is usually n bits as well.

*Examples:* Intel 8085: 8-bit ALU, so an 8-bit processor. Intel 8086: 16-bit registers and ALU (`ADD AX, BX` adds 16 bits at once), a 16-bit processor. 80386: 32-bit; Core i7: 64-bit. (The 8088 is still a 16-bit processor although its external data bus is 8 bits, because its ALU is 16-bit.)

**ii. Superscalar processor**

A **superscalar** processor has **more than one execution pipeline/unit** and can **issue and execute more than one instruction in the same clock cycle**, when the instructions are independent. This is instruction-level parallelism inside a single CPU.

*Example:* the Intel **Pentium** has two integer pipelines, **U and V**. In one clock it can start two simple instructions, e.g. `MOV AX, BX` in U and `ADD CX, DX` in V, giving up to 2 instructions per clock. Pentium Pro and later issue 3 or more micro-operations per clock. (A *scalar* processor such as the 80486 issues at most one instruction per clock.)
