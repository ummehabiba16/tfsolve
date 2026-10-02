---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "No lexical errors: every character sequence forms a valid C token (keywords int, do, if, else, while; identifiers arr, i, print, index; numbers 1, 2, 3, 5, 0, 4; string literals; operators and punctuation). The real errors (print and index are undeclared; print is not printf) are found later by the semantic analyser or linker, because a lexer only checks the form of tokens, not their meaning."
sources: ["MMA lexical analysis slides 2-16, 29-36 (Role of the Lexical Analyzer, Lexical Errors)", "Dragon book 2e sec. 3.1.4"]
---
**Answer: No, the lexical analyzer will not find any errors in this snippet.**

A lexical analyzer only checks that the input can be divided into **valid tokens**. It cannot detect errors that need the meaning (declarations, types) or the structure of the program. Here every lexeme matches a token pattern of C:

| Lexemes | Token class |
|:--|:--|
| `int`, `do`, `if`, `else`, `while` | keywords |
| `arr`, `i`, `print`, `index` | identifiers (letter followed by letters/digits) |
| `1`, `2`, `3`, `5`, `0`, `4` | integer constants |
| `"EVEN\n"`, `"ODD\n"` | string literals (with valid escape sequence `\n`) |
| `=`, `%`, `==`, `++`, `<` | operators |
| `[`, `]`, `{`, `}`, `(`, `)`, `,`, `;` | punctuation |

**The real problems are detected by later phases:**

1. `print` is not a standard C function (`printf` was probably intended). It is lexically a valid identifier. It is reported as an implicit declaration or undeclared function by the **semantic analyser**, or as an undefined reference by the **linker**.
2. `index` is not declared (the loop variable is `i`). Lexically it is a valid identifier; the error "undeclared identifier `index`" is a **semantic error**. Logically the loop should test `i < 4`.
3. `arr[i] %2` is lexically just `arr [ i ] % 2`; the spacing does not matter.

So the lexer produces a correct token stream, and these mistakes are caught by the semantic analyser or linker, not by the lexical analyzer. (A lexical error would be, for example, an illegal character such as `@` or an unterminated string `"EVEN`.)
