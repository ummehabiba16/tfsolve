---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Yes in practice: the scanner must often look ahead one or more characters past the lexeme (e.g. to tell > from >=, or end an identifier), and reading one character at a time from the OS would be very slow; buffer pairs with sentinels give cheap lookahead and fast reading."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering)", "Dragon book 2e sec. 3.2"]
---
**Yes, it is practically essential**, for two reasons:

1. **Lookahead.** The lexer often cannot decide that a lexeme has ended until it has read one or more characters *beyond* it. Examples: an identifier ends only when a non-letter/digit is seen; `<` vs `<=`; `=` vs `==`; Fortran's `DO 5 I = 1.25` needs even more lookahead. The extra characters must be kept so they can be "pushed back" and re-read as part of the next lexeme. A buffer holds them, and the `forward` pointer can simply be retracted.
2. **Speed.** Lexical analysis is the only phase that reads every character, and reading one character at a time with a system call is very slow. Reading a whole block (e.g. 4096 characters) into a buffer at once, and using a **buffer pair** with **sentinels** (`eof` at the end of each half), lets the lexer test for the end of buffer and the end of input with a single comparison per character.

So, while a toy lexer could read characters one by one with `getc`/`ungetc`, a real compiler needs input buffering for correct lookahead and acceptable speed.
