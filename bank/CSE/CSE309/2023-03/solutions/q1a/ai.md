---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Linker: subfunction is undefined in main.o and must be resolved from subcode.o (also exit from libc, and the implicit declaration int vs void mismatch, return n in a void function); the loader must allocate memory, relocate both modules and load libc. Resolved by declaring int subfunction(void) / extern, #include <stdlib.h>, linking both objects and libc, and relocation by linker and loader."
sources: ["MMA introduction slides 26-39 (Relocatable Machine Code, Linker and Loader)", "Dragon book 2e sec. 1.1"]
---
`main.c` and `subcode.c` are compiled separately into relocatable object files `main.o` and `subcode.o`. Each starts at address 0, and each contains references it cannot resolve itself.

**Issues for the linker**

1. **Unresolved external symbols.** `main.o` calls `subfunction()` (defined in `subcode.o`) and `exit()` (defined in the C library). The compiler leaves these as unresolved references with relocation entries. The linker must find a definition for each one; if `subcode.o` or libc were not given, it would report "undefined reference to `subfunction`".
2. **Combining modules and relocation.** The linker places the code and data of both modules (and the needed library code) one after another in one address space. It then fixes every address that depends on this placement, e.g. the `call subfunction` in `main` is patched with `subfunction`'s final (relative) address.
3. **Type mismatch across files.** `main` uses `i = subfunction();` without a prototype, so C assumes `int subfunction()`, while `subcode.c` defines `void subfunction()` and still does `return n;`. The linker matches **names only**, so it links them anyway, and the value `main` gets for `i` is undefined. (A compiler gives a warning/error for `return n;` in a `void` function and for the implicit declaration; `exit()` also needs `<stdlib.h>` and an argument.)
4. **Static vs dynamic library.** `printf`/`exit` may come from a shared libc. Then the linker records only the dependency and a stub, and leaves the final binding to the loader.

**Issues for the loader**

1. **Memory allocation.** The executable must be given memory for code, data, stack and heap.
2. **Relocation at load time.** If the program is not loaded at the address assumed by the linker, the loader adjusts the relocatable addresses (base address + offset), as in the slide example where code linked at 120 is loaded at 300.
3. **Dynamic linking.** Shared libraries (libc) must be found, mapped into memory, and the references to `exit` (and other library functions) bound to their actual addresses.
4. **Start-up.** It sets up the stack and arguments, then jumps to the start-up code, which calls `main`. The value passed to `exit` becomes the exit status.

**Resolution**

- Declare the function correctly: `int subfunction(void);` in a header included by both files (or `extern int subfunction(void);` in `main.c`), and define `int subfunction(void) { ...; return n; }`. Use `int main(void)` and `exit(0)` with `#include <stdlib.h>`.
- Link both object files and the library: `gcc main.o subcode.o -o prog` (libc is added automatically). The linker resolves `subfunction` and `exit` and relocates `main.o` and `subcode.o`.
- The loader places `prog` in memory, relocates it if necessary, loads and binds the shared libc, and starts execution. `i` becomes $1 + 2 + \ldots + 50 = 1275$.
