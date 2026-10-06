---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Preprocessor: expands macros, includes files and handles conditional compilation before compilation. Linker: combines relocatable object files and libraries and resolves external references into one executable. Loader: loads the executable into memory at run time, relocating its addresses, and starts it."
sources: ["MMA introduction slides 14-39 (preprocessor, linker, loader)", "Dragon book 2e sec. 1.1 (Fig. 1.5)"]
---
**(i) Preprocessor.** Runs before the compiler proper and produces the source text that the compiler reads (Dragon book sec. 1.1). It does **macro processing** (`#define` expansion), **file inclusion** (`#include` pastes header files), **conditional compilation** (`#if`, `#ifdef`, `#else`), and in some systems extensions of the language. Example: after `#define N 10`, `a[N]` becomes `a[10]`.

**(ii) Linker.** A program is compiled in parts (separate files, libraries) into **relocatable object files** that contain unresolved references to symbols defined elsewhere. The linker **joins** the object files and the needed library modules into a single executable (or load module), **resolves the external references** (finds the definition of every called function or used global), and adjusts the relocatable addresses accordingly.

**(iii) Loader.** The loader brings the executable into memory when the program is run: it decides the memory addresses, **modifies the relocatable addresses** of the code and data to the actual load address, places the program there, and starts execution. With shared libraries it also performs *dynamic linking* at load or run time.

Order in the language-processing system: source $\to$ **preprocessor** $\to$ compiler $\to$ assembler $\to$ **linker** $\to$ **loader** $\to$ running program.
