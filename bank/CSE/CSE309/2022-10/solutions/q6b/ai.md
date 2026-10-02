---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "i. Yes (in principle the parser could work directly on characters, as scannerless parsers do; in practice it is kept separate). ii. With one buffer, reloading at the end overwrites the start of a lexeme that is still being scanned (and lookahead characters); with two halves, one half is reloaded while the other still holds the lexeme, so lexemes and lookahead up to N characters are safe, and sentinels make the end test cheap. iii. Panic mode: when no token pattern matches the remaining input, delete successive characters until a well-formed token is found, then continue."
sources: ["MMA lexical analysis slides 13-16, 29-49 (Lexical Analysis Versus Parsing, Lexical Errors, Input Buffering, Buffer Pairs)", "Dragon book 2e sec. 3.1.1, 3.1.4, 3.2"]
---
**i. Can the lexical analyzer step be eliminated? Yes (5 marks).**

The grammar could include the rules for characters, white space and comments, and the parser would then read characters directly (scannerless parsing). It is separated only for simplicity of design, efficiency and portability, not because it is necessary.

**ii. Why a buffer pair instead of a single buffer (8 marks).**

- The lexer reads the input in large blocks of $N$ characters (e.g. 4096) to avoid one system call per character. Two pointers are used: `lexemeBegin` (start of the current lexeme) and `forward` (scans ahead, possibly beyond the lexeme).
- **Single buffer:** when `forward` reaches the end of the buffer in the middle of a lexeme, the buffer must be refilled. That **overwrites the beginning of the current lexeme**, which `lexemeBegin` still points to, and any characters that `forward` may need to retract to. The lexeme is lost unless it is copied first.
- **Buffer pair:** two halves of $N$ characters each, reloaded **alternately**. When `forward` runs off the end of one half, only the other half is reloaded, while the half containing the start of the lexeme is untouched. So any lexeme (and lookahead) of up to $N$ characters is handled safely, with no copying.
- **Sentinels** (`eof` at the end of each half) make the end-of-buffer test part of the normal character test, giving one comparison per character in the common case.

**iii. Panic mode (7 marks).**

A **lexical error** occurs when the lexer cannot match any token pattern to a prefix of the remaining input (e.g. an illegal character like `@` in C). In **panic-mode recovery**, the lexer **deletes successive characters** from the remaining input until it can find a well-formed token at the beginning of what is left, then continues scanning normally.

- *Advantages:* very simple, never loops.
- *Drawbacks:* it may discard characters that belong to valid tokens, and it gives the parser a token stream the programmer did not write, which can cause confusing later errors.

Other simple recoveries: delete one character, insert a missing character, replace a character, or transpose two adjacent characters.
