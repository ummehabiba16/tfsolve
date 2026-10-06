---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Errors: lexical (illegal characters, misspelled tokens), syntactic (missing semicolon, unbalanced brackets), semantic (type mismatch, undeclared name), logical/run-time (infinite loop, wrong algorithm). Lexical error recovery: panic mode (delete characters until a valid token), delete a character, insert a missing character, replace a character, transpose adjacent characters."
sources: ["MMA lexical analysis slides 29-36 (lexical errors); parser role slides 2-24", "Dragon book 2e sec. 1.2, 3.1.4, 4.1.3"]
---
**Types of errors in a compiler** (Dragon book sec. 4.1.3):

| Type | Detected by | Examples |
|:--|:--|:--|
| **Lexical** | lexical analyzer | misspelled identifiers or keywords, illegal characters (`@`), unterminated string or comment, malformed number such as `12.3.4` |
| **Syntactic** | parser | missing semicolon, unbalanced parentheses or braces, misplaced `else`, an operator without operand |
| **Semantic** | semantic analyzer (type checker) | type mismatch between an operator and its operands, use of an undeclared variable, wrong number of arguments, `break` outside a loop |
| **Logical** | not detected by the compiler (found by testing/debugging) | infinite loop or recursion, an assignment `=` where `==` was intended, wrong algorithm |

(Run-time errors such as division by zero or an array index out of range are found only when the program executes.)

**Recovery from lexical errors** (sec. 3.1.4). A lexical error occurs when no prefix of the remaining input matches any token pattern. Possible recovery actions:

1. **Panic mode:** delete successive characters from the remaining input until the lexer finds a well-formed token at its beginning. Simple, but may discard much input.
2. **Delete** one character from the remaining input.
3. **Insert** a missing character into the remaining input.
4. **Replace** one character by another.
5. **Transpose** two adjacent characters (for example `fi` $\to$ `if`).

The single-character repairs (2-5) are tried so as to obtain a valid lexeme with the minimum number of transformations, and the error is reported with its line number so that the programmer can fix it.
