---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Lookahead is needed whenever the end of a lexeme is recognised only by reading a character that does not belong to it: identifiers and numbers (until a non-alphanumeric), operators with a longer form (< vs <=, = vs ==, - vs -> or --), keyword vs identifier (if vs ifx), and Fortran DO 5 I = 1,25 vs DO 5 I = 1.25. The extra character is then pushed back (retraction of the forward pointer)."
sources: ["MMA lexical analysis slides 37-38 (Input Buffering)", "Dragon book 2e sec. 3.2 (introduction)"]
---
In a lexical analyzer we often have to **look one or more characters beyond the next lexeme** before we can be sure that the right lexeme has been found (Dragon book sec. 3.2). The scenarios where **at least one additional character** is needed:

1. **End of an identifier or a number.** We cannot be sure that we have seen the end of an identifier until we read a character that is not a letter or a digit, and therefore is not part of the lexeme for **id**. For `count+1`, only after reading `+` is `count` complete. In the same way, `123` is complete only after a non-digit is seen (and `12.` needs the character after the dot to see whether it continues as `12.5`).

2. **Operators that can be the start of a longer operator.** In C, a single-character operator such as `-`, `=`, `<`, `>` or `!` could be the beginning of a two-character operator: `-` of `->` or `--`, `=` of `==`, `<` of `<=` or `<<`. On reading `<` the scanner must read the next character; if it is `=` the lexeme is `<=`, otherwise it is `<` and the extra character is **pushed back** (the forward pointer is retracted by one, it will be the start of the next lexeme).

3. **Keyword versus identifier.** `if` is a keyword only if the next character cannot continue an identifier; for `ifx`, `if(x)` and `if x` the decision is made on the character after `if`.

4. **Languages with long lookahead.** In Fortran, `DO 5 I = 1,25` is a loop header but `DO 5 I = 1.25` is an assignment to the variable `DO5I`: the scanner must read ahead up to the `,` or the `.` to decide whether `DO` is a keyword. Pascal's `1..10` must not be read as the real number `1.`.

In all these cases the scanner uses `lexemeBegin` and `forward` pointers (buffer pairs): `forward` scans past the lexeme, and once the lexeme is decided, the extra characters are retracted. This is the reason why buffering with look-ahead of at least one character is needed.
