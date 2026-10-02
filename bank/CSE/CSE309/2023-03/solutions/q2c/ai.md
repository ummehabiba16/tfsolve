---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Five classes: (1) one token per keyword; (2) tokens for operators, individually or in classes (e.g. comparison); (3) one token for all identifiers; (4) one or more tokens for constants (numbers, literal strings); (5) one token for each punctuation symbol (parentheses, comma, semicolon)."
sources: ["MMA lexical analysis slides 17-22 (Tokens, Patterns, and Lexemes)", "Dragon book 2e sec. 3.1.2"]
---
In many programming languages, the following classes cover most or all of the tokens:

1. **One token for each keyword.** The pattern is the keyword itself, e.g. `if`, `else`, `while`: tokens **if**, **else**, **while**.
2. **Tokens for the operators**, either individually or in classes. Example: one token **comparison** for `<`, `<=`, `>`, `>=`, `==`, `!=`, with an attribute telling which one.
3. **One token representing all identifiers.** Pattern: letter followed by letters and digits. Token **id**, with attribute = pointer to the symbol-table entry for the lexeme (e.g. `pi`, `score`, `D2`).
4. **One or more tokens representing constants**, such as numbers and literal strings. Tokens **number** (lexemes `3.14159`, `0`, `6.02e23`) and **literal** (anything between `"` and `"`, e.g. `"core dumped"`), with the value or text as attribute.
5. **Tokens for each punctuation symbol**, such as left and right parentheses, comma and semicolon: `(`, `)`, `,`, `;`.

Example: for `printf("Total = %d\n", score);`, `printf` and `score` are **id**, `"Total = %d\n"` is a **literal**, and `(`, `,`, `)`, `;` are punctuation tokens.
