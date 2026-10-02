---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The preprocessor produces the modified source fed to the compiler: file inclusion (#include), macro definition and expansion (#define PI 3.14159, parameterised macros), conditional compilation (#if/#ifdef/#else/#endif, e.g. platform code), line control (#line), plus removing comments and joining lines; it may also be a language extension tool."
sources: ["MMA introduction slides 13-25 (Language Processors, C Preprocessor, Line Control Directive)", "Dragon book 2e sec. 1.1"]
---
A source program may be divided into modules stored in separate files, and may use macros. The **preprocessor** collects the source program and expands such shorthands, producing the modified source program that is fed to the compiler (`source program -> preprocessor -> modified source program -> compiler`). The C preprocessor (`cpp`) is often a separate program invoked as the first part of translation. Its tasks:

**1. File inclusion.** `#include` replaces the directive with the text of the named file.

```c
#include <stdio.h>     /* replaced by the contents of stdio.h */
int main(void) { printf("Hello, world!\n"); return 0; }
```

**2. Macro definition and expansion.** `#define` introduces a name (optionally with parameters) that is textually replaced wherever it is used.

```c
#define PI 3.14159
#define RADTODEG(x) ((x) * 57.29578)
area = PI * r * r;          /* becomes 3.14159 * r * r      */
d = RADTODEG(a + b);        /* becomes ((a + b) * 57.29578) */
```

**3. Conditional compilation.** `#if`, `#ifdef`, `#ifndef`, `#elif`, `#else`, `#endif` select which parts of the source are compiled, e.g. platform-specific code:

```c
#ifdef __unix__
# include <unistd.h>
#elif defined _WIN32
# include <windows.h>
#endif
```

**4. Line control.** `#line 15 "ourdemo.cpp"` resets the line number (and file name) used in `__LINE__`, `__FILE__` and error messages. It is used by generated code (Lex/Yacc output) so that errors refer to the original file.

**5. Other tasks:** removing comments, joining lines ending with `\`, and `#error`/`#pragma`. Some preprocessors also act as language extensions, adding constructs to a language by macro-like translation.
