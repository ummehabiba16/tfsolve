---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The input is read N characters at a time into two buffers that are reloaded alternately; pointer lexemeBegin marks the start of the current lexeme and forward scans ahead; when forward reaches the end of one buffer the other is reloaded and forward moves to its beginning; sentinels (eof) make the end-of-buffer test cost nothing extra; lexeme length plus lookahead must be at most N."
sources: ["MMA lexical analysis slides 39-45 (Buffer Pairs)", "Dragon book 2e sec. 3.2.1"]
---
**Why buffering.** Reading the source one character at a time with one system call each is very slow. The scanner instead reads a block of $N$ characters (usually $N$ = disk block, 4096) with one system call into a buffer.

**Two-buffer (buffer pair) scheme** (Dragon book sec. 3.2.1):

- Two buffers of $N$ characters each are used and are **reloaded alternately**: while the scanner is working in one, the other can be filled with the next $N$ characters of the input.
- If fewer than $N$ characters remain in the file, a special character `eof` marks the end of the source.
- Two pointers are kept: **`lexemeBegin`** marks the start of the current lexeme; **`forward`** scans ahead until a pattern matches.
- When the lexeme has been found, `forward` is at its right end (or one beyond it, in which case it is retracted); the lexeme is passed on as the token attribute, and `lexemeBegin` is set to the character right after it.
- Advancing `forward` requires a test for the end of a buffer: when the end of one buffer is reached, the **other buffer is reloaded** from the input and `forward` moves to the beginning of the newly loaded buffer.

```text
 buffer 1                       buffer 2
 [ . . . . . . . . . . . ] [ . . . . . . . . . . . ]
     ^lexemeBegin       ^forward  -->  (when forward leaves one buffer the other is reloaded)
```

**Limit.** As long as the sum of the lexeme length and the lookahead distance is at most $N$, the lexeme is never overwritten before it is recognised. With a sentinel `eof` at the end of each buffer, only one test is needed per character instead of two (end of buffer, and which character).
