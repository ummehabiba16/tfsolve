---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The lexical analyzer reads the source characters, groups them into lexemes and returns tokens to the parser on demand; it strips white space and comments, correlates error messages with line numbers, expands macros if required and interacts with the symbol table."
sources: ["MMA lexical analysis slides 2-16 (Role of the lexical analyzer)", "Dragon book 2e sec. 3.1.1"]
---
The lexical analyzer (scanner) is the first phase of a compiler (Dragon book sec. 3.1.1). Its roles:

1. **Reads the input characters** of the source program and **groups them into lexemes**; for every lexeme it produces a **token** $\langle token\text{-}name, attribute\text{-}value\rangle$ which it passes to the parser. It works as a subroutine of the parser: when the parser calls `getNextToken`, the scanner reads input until it finds the next lexeme.
2. **Strips out comments and white space** (blank, tab, newline), which the parser does not need.
3. **Interacts with the symbol table:** when it finds a lexeme for an identifier it enters it into the symbol table (and reads the entry to find whether it is a keyword) and makes the table entry the token's attribute.
4. **Correlates error messages with the source program:** it keeps track of the line number, so that the compiler can report where an error occurred; it also reports lexical errors (illegal characters, malformed tokens) and may recover from them.
5. Sometimes performs **macro expansion** (and, in some compilers, copies the source with error messages inserted).

Separating this work from the parser gives a simpler design, a more efficient compiler (specialised buffering) and better portability.
