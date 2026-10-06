---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The buffer length N limits the maximum length of a lexeme (identifier, string literal, comment) and the lookahead the language can need: length of lexeme + lookahead must stay within N, otherwise the buffer holding the start of the lexeme is overwritten on reload; languages needing unbounded lookahead (Fortran DO, PL/I) need a bigger buffer."
sources: ["MMA lexical analysis slides 39-45 (Buffer Pairs)", "Dragon book 2e sec. 3.2.1"]
---
In the buffer-pair scheme each buffer has $N$ characters (typically one disk block, 4096). `lexemeBegin` must stay in a buffer that has not been reloaded, and `forward` may only run ahead as long as the other buffer can be refilled without overwriting the lexeme. Hence

$$\text{length of the lexeme} + \text{lookahead distance} \le N$$

must hold; otherwise the part of the lexeme in the buffer would be overwritten before the lexeme is determined (Dragon book sec. 3.2.1).

**Characteristics of a programming language affected by the buffer length:**

1. **Maximum length of lexemes.** The length of identifiers, string constants, numeric constants and comments (if they are scanned as one lexeme) cannot exceed about $N$. A language must therefore limit the length of these lexemes (many languages and compilers have such a limit), or use bigger buffers, or copy a long lexeme to a separate area.

2. **The amount of lookahead the language can require.** Languages whose lexemes can be recognised only after reading far ahead need larger buffers. Example: in Fortran, `DO 5 I = 1.25` versus `DO 5 I = 1,25` can be told apart only by looking at the `.` or the `,` after a possibly long expression; in PL/I, keywords are not reserved and `DECLARE (ARG1, ARG2, ..., ARGn)` is a declaration or an array reference depending on what follows the `)`, which may be arbitrarily far away. With a fixed $N$ the amount of lookahead is limited, which restricts such language features.

In short, the buffer length limits the length of tokens (identifiers, literals) and the lookahead distance of the language's lexical syntax; language designers therefore prefer reserved keywords and short, simple tokens.
