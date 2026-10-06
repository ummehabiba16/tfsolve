---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The register context holds the program counter, processor status, stack pointer and the general-purpose registers saved when the process is not running."
sources: ["Bach, ch. 6 (register context)"]
---
The **register context** is the part of a process's context that holds the **contents of the hardware registers**:

- the **program counter** (the address of the next instruction to execute, in user or kernel mode),
- the **processor status register** (mode, interrupt level, condition codes),
- the **stack pointer** (user or kernel stack), and
- the **general-purpose registers** (and the floating-point registers),

that the process was using. When the process is not running, e.g. at a context switch or interrupt, the kernel **saves** these registers in the process's context layer (in the u area/kernel stack) and **restores** them when the process runs again, so that it continues exactly where it stopped. (The memory-management registers (register triples) are also part of the context in some descriptions.)
