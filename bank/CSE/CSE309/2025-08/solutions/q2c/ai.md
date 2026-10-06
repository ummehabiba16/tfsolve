---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With buffer pairs the lookahead (forward pointer) can move at most one buffer length N beyond lexemeBegin, so the buffer size limits the maximum lexeme length (identifiers, string literals) and the amount of lookahead the language can require; a language with long lexemes or unbounded lookahead (e.g. Fortran DO statements) needs larger buffers or a different scheme."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering, Buffer Pairs, Sentinels)", "Dragon book 2e sec. 3.2"]
changes:
  - "2026-10-06: added TikZ figure (figures/buffers.png) for the buffer pair; the answer itself is unchanged."
---
In the buffer-pair scheme, two buffers of $N$ characters each (typically $N$ = one disk block, e.g. 4096) are reloaded alternately. `lexemeBegin` marks the start of the current lexeme, and `forward` scans ahead.

![Buffer pair with sentinels, lexemeBegin and forward](figures/buffers.png)

**Effect of the buffer size:**

1. **Maximum lexeme length.** When `forward` runs off the end of one half, the other half is reloaded. If a lexeme is longer than $N$, `forward` would have to reload the half that still holds the start of the lexeme, which would overwrite the lexeme. So the language (or the implementation) must limit the length of identifiers, numbers and string literals to about $N$ characters, or handle long lexemes specially.

2. **Amount of lookahead.** `forward` can be at most about $N$ characters past `lexemeBegin`. A language whose tokens need long lookahead before a decision can be made cannot be scanned with a small buffer.

Example: in Fortran, `DO 5 I = 1.25` (an assignment to `DO5I`) and `DO 5 I = 1,25` (a loop) differ only at `.` or `,`. In PL/I, keywords are not reserved: `DECLARE (ARG1, ARG2, ..., ARGn)` can be a declaration or an array reference, and the lexer cannot tell until it sees what follows the `)`. The amount of lookahead is unbounded and needs a large buffer.

3. **Efficiency.** A larger $N$ means fewer reload operations (system calls), and sentinels make the end-of-buffer test cheap.

**Conclusion:** language designers keep lexemes and lookahead short (reserved keywords, limited identifier length, simple token forms) so that a fixed-size buffer pair is enough. The buffer size is therefore a practical limit on these language attributes.
