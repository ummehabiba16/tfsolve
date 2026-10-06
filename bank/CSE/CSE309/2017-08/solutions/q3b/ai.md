---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Linker: combines relocatable object files and libraries into one executable, resolving external references. Loader: copies the executable into memory at run time and adjusts relocatable addresses (and binds shared libraries). Headers and macros are handled earlier by the preprocessor and leave only declarations/expanded text; libraries are the object code the linker (static) or loader (shared) supplies."
sources: ["MMA introduction slides 27-39 (Assembler, linker, loader)", "Dragon book 2e sec. 1.1 (Fig. 1.5)"]
---
**Linker.** A large program is compiled in pieces; each source file is translated to a **relocatable object file** that may refer to functions and variables defined in other files or in libraries. The linker combines all these object files and the needed library modules into one executable, **resolves the external references** (matches every use of a symbol with its definition) and relocates the addresses (Dragon book sec. 1.1).

**Loader.** The loader takes the executable (relocatable machine code) and **places it in memory** at the actual run-time addresses, adjusting the relocatable addresses; with shared libraries it also performs the dynamic linking at load/run time.

**Relationship with C/C++ programs.**

(i) **Header files.** `#include <stdio.h>` is processed by the *preprocessor*, which pastes the header text into the source before compilation. A header holds declarations (function prototypes, types, `extern` variables, macros), not code. The compiler uses them for syntax and type checking; for each declared-but-not-defined function that the program calls, the object file records an **undefined (external) symbol**, which the **linker** later resolves against a library or another object file. So a header makes the linker's job necessary, but a header itself is never linked or loaded.

(ii) **Macros.** `#define` macros are expanded by the preprocessor (macro processing) before the compiler proper runs. After expansion there is no trace of the macro in the object code, so macros have **no direct role in linking or loading**. A macro can only affect them indirectly, e.g. by expanding to a call of a library function, or by including/excluding code with `#ifdef`, which changes the external symbols the linker must resolve.

(iii) **Libraries.** A library is a collection of precompiled object modules. A **static library** (`.a`/`.lib`) is searched by the linker, which copies only the modules that resolve undefined symbols into the executable. A **shared (dynamic) library** (`.so`/`.dll`) is not copied: the linker records a reference and the **loader** (dynamic linker) maps the library into memory when the program starts, binding the call addresses. The header declares the library function and the library supplies its definition.

In order: preprocessor (headers, macros) $\to$ compiler $\to$ assembler $\to$ **linker** (libraries, external references) $\to$ **loader** (placement in memory, shared libraries).
