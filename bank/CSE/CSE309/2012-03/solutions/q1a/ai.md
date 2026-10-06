---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Compiler: translates the source program into assembly or machine code; assembler: translates assembly into relocatable machine code; linker: combines object files and libraries into one executable, resolving external references. Header files are expanded by the preprocessor and only supply declarations (leaving external references for the linker); libraries (static or shared) supply the definitions that the linker or the loader binds."
sources: ["MMA introduction slides 14-39 (preprocessor, assembler, linker, loader)", "Dragon book 2e sec. 1.1, Fig. 1.5"]
---
**Compiler.** A program that reads a program in a source language and translates it into an equivalent program in a target language, typically assembly or machine code, reporting errors on the way (Dragon book sec. 1.1). For C/C++ the input is the preprocessed source and the output is assembly or an object file.

**Assembler.** Translates the **assembly language** produced by the compiler into **relocatable machine code** (an object file): it replaces mnemonics by binary instruction codes, resolves labels into offsets, and records relocation information and the symbols that are defined and used.

**Linker.** A large program is compiled in pieces; the object files contain unresolved references to functions and variables defined in other files and in libraries. The **linker** combines all relocatable object files and the needed library modules into one executable, **resolving the external references** and relocating the addresses. (A **loader** then places the executable in memory to run it.)

```text
source --preprocessor--> source --compiler--> assembly --assembler--> object --linker (+ libraries)--> executable
```

**Relationship with C/C++ programs.**

(i) **Header files.** `#include <stdio.h>` is handled by the **preprocessor**, which pastes the header into the source text before the compiler sees it. A header contains declarations (function prototypes, types, `extern` variables, macros), not code, so the compiler can check calls and types. For every function or variable that is declared but defined elsewhere, the object file records an **undefined symbol**; the **linker** later resolves it. So the header serves the *compiler*; the definition is found by the *linker*.

(ii) **Libraries.** A library is a collection of precompiled object modules (for example `libc`). A **static library** (`.a`) is searched by the linker, which copies the modules that satisfy the undefined symbols into the executable. A **shared library** (`.so`/`.dll`) is not copied: the linker records a reference and the loader (dynamic linker) maps the library at load time. The header declares a library function, the library defines it.
