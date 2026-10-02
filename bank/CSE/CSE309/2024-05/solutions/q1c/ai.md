---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Linker: i, iv, vi. Loader: ii, iii, v, vii."
sources: ["MMA introduction slides 28-39 (Language Processors, Difference between Linker and Loader)"]
---
**Linker:** i, iv, vi.

**Loader:** ii, iii, v, vii.

Reasons (following the linker/loader comparison in the slides):

- (i) **Object files**: the linker's *input* (object code from the compiler/assembler), so linker.
- (ii) **Loading programs and libraries**: loader.
- (iii) **Load executable files to memory**: the loader's main function.
- (iv) **Produce executable files**: the linker's main function (combining object modules and libraries).
- (v) **Allocate address to executable files**: the loader allocates memory space (load addresses) to the program.
- (vi) **Managing objects in the program's space**: the linker arranges the objects/modules in the program's address space and decides how much space each module's code holds.
- (vii) **Setting up references used in the program**: the loader adjusts/settles the references (relocation and dynamic symbolic references) when the program is placed in memory.
