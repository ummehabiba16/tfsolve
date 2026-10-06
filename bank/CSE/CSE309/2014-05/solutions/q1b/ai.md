---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Relocatable machine code is not tied to fixed memory addresses: its addresses are relative to the start of the module (and carry relocation information), so the loader/linker can place the module anywhere in memory by adding the actual load address to each relocatable address; hence it is called relocatable."
sources: ["MMA introduction slides 27-39 (relocatable machine code)", "Dragon book 2e sec. 1.1"]
---
The assembler turns assembly code into **relocatable machine code**. It is called *relocatable* because its addresses are **not absolute**: the compiler or assembler does not know where in memory the module will finally be loaded, so the addresses inside the code (of data, labels, procedures) are **relative to the start of the module** (offsets from 0), and the object file keeps **relocation information** that marks which words are addresses.

Because of this, the **linker/loader can place the module at any memory location**: it **relocates** the code by adding the actual starting address (the load address) to every relocatable address. Several modules compiled separately can thus be linked into one program, each at a different base, and the same module can be loaded at different places in different runs (Dragon book sec. 1.1).

**Example.** An instruction `LD R1, 100` in a module means "the variable at offset 100 from the start of this module". If the loader places the module at address 4000, the relocation step changes the instruction to `LD R1, 4100`; if it is placed at 9000, to `LD R1, 9100`. External references (a call to a function in another file) are likewise left symbolic by the assembler and resolved by the linker.

By contrast, *absolute* machine code has fixed addresses and works only if loaded at one particular place.
