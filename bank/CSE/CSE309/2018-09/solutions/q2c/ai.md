---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Two measures: (1) install the reserved words in the symbol table initially, with a field saying they are keywords (and their token); the identifier recogniser returns that token when the lexeme is found as a keyword, else id. (2) give each keyword its own transition diagram, prioritised over the identifier diagram, with a lookahead test that the next character cannot continue an identifier (e.g. then vs thenextvalue)."
sources: ["MMA lexical analysis slides 77-83 (Recognition of Reserved Words and Identifiers)", "Dragon book 2e sec. 3.4.2"]
---
Keywords such as `if`, `then`, `else` match the pattern for identifiers (letter followed by letters/digits), so the transition diagram for `id` would also recognise them. The textbook gives two ways to handle this:

**1. Install the reserved words in the symbol table initially.**

- Before scanning starts, every keyword is entered in the symbol table, with a field that says it is a reserved word and which token it represents.
- The lexer recognises keywords and identifiers with the **same** transition diagram (letter (letter | digit)\*).
- When the diagram accepts, the action is `getToken(installID())`:
- `installID()` looks up the lexeme. If it is not present it is inserted as an identifier; if it is a keyword the existing entry is found.
- `getToken()` returns the token stored in the entry: the keyword's own token (e.g. **then**) for reserved words, otherwise **id**.

This keeps the lexer small, and adding a keyword just means adding an entry.

**2. Create separate transition diagrams for each keyword.**

- For example, the diagram for `then` has states for `t`, `h`, `e`, `n`, followed by a test that the next character is **not** a letter or digit, i.e. not something that can continue an identifier. Otherwise `thenextvalue` would be split into `then` + `extvalue`.
- The keyword diagrams must be tried **before** (prioritised over) the identifier diagram, so that `then` is returned as the keyword token and not as **id**.

In Lex, the same effect comes from the **conflict-resolution rules**: the longest match is preferred (`thenx` is an id), and for equal lengths the earlier pattern wins, so keyword patterns are listed before the `id` pattern.
