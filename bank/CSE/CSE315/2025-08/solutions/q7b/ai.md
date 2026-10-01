---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) Real mode: the 80286 runs 8086 machine code unchanged (a fast 8086). (ii) Protected mode: 8086 programs must be re-assembled/re-compiled, because segment registers hold selectors and descriptors must be set up."
sources: ["MHE 80286 slide 4 (operating modes)", "MHE 80286 slides 40-44 (real vs protected addressing)"]
---
**(i) Object code compatible with 8086 in Real Mode.** In real mode the 80286 is "just a fast 8086" (up to 6 times faster). All memory management and protection are disabled, a segment register is shifted left by 4 bits and added to the offset, and only the first 1MB is addressed. So the **same binary (object/machine code)** produced for an 8086 can be loaded and run on the 80286 **without any change**, not even re-assembly.

**(ii) Source code compatible with 8086 in Protected Mode.** In protected mode the segment registers hold **selectors**, not segment addresses: the base, limit and access rights come from descriptors in the GDT or LDT. An 8086 binary that loads segment values like `MOV AX, 2000H / MOV DS, AX` or computes physical addresses would not work. However, the instruction set is a superset of the 8086's, so the **source program** can be **re-assembled or re-compiled** (with the OS setting up proper descriptors and selectors) and then runs with all the memory management and protection features. Compatibility is at the source level, not the binary level.
