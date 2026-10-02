---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The compiler/assembler produces relocatable machine code (addresses relative to 0, external references unresolved); the linker combines such object files and libraries, resolves external references (code in one file referring to a location in another), assigns each module its place and relocates (patches) the addresses, producing an executable that the loader then loads."
sources: ["MMA introduction slides 26-39 (Assembler, Relocatable Machine Code, Linker and Loader)", "Dragon book 2e sec. 1.1"]
---
**Relocatable machine code.** Large programs are compiled in pieces. The compiler (and assembler) produces, for each piece, **relocatable machine code**:

- Its addresses are numbered from 0 (or some arbitrary origin), because the final location in memory is not known yet.
- References to functions and variables in other files are left **unresolved**, with relocation/symbol information saying which addresses must be fixed later.

**Role of the linker.** The linker takes the relocatable object files and library files and produces one executable:

1. **Combining.** It merges the code and data sections of all object files (and the needed library modules) and decides where each module will be placed, i.e. how much memory each module's code occupies.
2. **Symbol resolution.** It resolves **external memory addresses**: where code in one file refers to a location in another file (a call to a function defined elsewhere, a global variable), it finds the definition and connects them. Undefined or doubly defined symbols are reported as errors.
3. **Relocation.** Once each module's start address is known, every address that depends on it is adjusted.

**Example from the slides.** Program SUBR is compiled starting at location 1. A jump at location 13 goes to statement ST at location 5. The linker places SUBR at location 120: the jump is now at 133 and must be relocated to point to ST's new location 125 ($= 120 + 5$). If the loader later puts the program at 300, the address is relocated again, to 305.

**Result.** The linker's output is an executable file. The **loader** then puts the executable (and any shared libraries) into memory and starts it, possibly relocating it again for its actual load address.

Without a linker, every program would have to be compiled as one unit at a fixed address, and libraries could not be reused.
