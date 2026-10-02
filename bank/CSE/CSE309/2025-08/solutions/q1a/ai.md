---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Relocatable code = object code whose addresses are relative and fixed up later; the linker resolves foo/bar/baz across main.o, libfoo, libbar and records dynamic references; the loader maps the executable and shared libraries into memory, relocates them and binds the shared-library symbols before main runs."
sources: ["MMA introduction slides 27-39 (Assembler, Relocatable Machine Code, Linker and Loader)", "Dragon book 2e sec. 1.1"]
---
**Relocatable machine code.** The compiler (with the assembler) turns each `.c` file into machine code whose addresses start at 0 and are *relative*. Calls to functions defined elsewhere are left as **unresolved external references**, with relocation entries that say "patch this address later".

- `main.o` contains `main`, with unresolved calls to `foo` and `bar` (lines 1-2 only *declare* them as `extern`).
- `libfoo.o` contains `foo`, with an unresolved reference to `baz`.
- `libbar.o` contains `baz` and `bar`; `bar` calls `baz` internally.

None of these can run on its own: the addresses are not final and some symbols are missing.

**Linker.** The linker combines relocatable object files and libraries into one executable:

1. **Symbol resolution:** it matches each undefined symbol with a definition: `foo` in `main.o` with `libfoo`, `bar` with `libbar`, and `baz` (used by `libfoo`) with `libbar`. If a definition were missing it would report "undefined reference".
2. **Relocation:** it lays out the code and data sections of `main.o` and fixes the relative addresses in it.
3. Because `libfoo` and `libbar` are **shared libraries**, their code is not copied into the executable. The linker records that the program needs `libfoo` and `libbar` and creates stubs (PLT/GOT entries) for `foo` and `bar`. The `libfoo` $\to$ `baz` reference stays a *dynamic* reference to `libbar`.

**Loader.** When the program is run, the loader (and the dynamic linker it starts):

1. reads the executable, allocates memory and copies the code and data of `main` into it, adjusting relocatable addresses to the actual load address;
2. finds and maps `libfoo` and `libbar` into the process's address space (each library can be loaded at any address, which is why it is relocatable/position-independent);
3. binds the dynamic references: `foo` and `bar` in `main`, and `baz` in `libfoo`, now point to their real addresses (eagerly, or lazily at the first call);
4. sets up the stack and jumps to the entry point, which calls `main`.

Execution: `foo(5)` = `baz(6)` = 12; `bar(3)` = 3 + `baz(3)` = 3 + 6 = 9; `main` returns **21**.

**Summary:** relocatable code is the *compile-time* product with addresses still to be fixed; the linker fixes the cross-file references (*link time*); the loader places everything in memory and completes the shared-library bindings (*load/run time*).
