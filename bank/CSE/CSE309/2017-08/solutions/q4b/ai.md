---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Buffer pair: two buffers of N characters, each ended by a sentinel eof, with pointers lexemeBegin and forward; the sentinel merges the end-of-buffer test with the character test (one test per character). Lexeme length plus lookahead must not exceed N for the lexeme to be safe from being overwritten by a reload; with the luckiest alignment the limit approaches 2N-1."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering, Buffer Pairs, Sentinels)", "Dragon book 2e sec. 3.2.1-3.2.2"]
---
**Buffer pairs.** The input is read in blocks of $N$ characters (usually $N$ = disk block size, e.g. 4096) into **two buffers** that are reloaded alternately, so one system call reads $N$ characters instead of one call per character. Two pointers are kept: `lexemeBegin` marks the beginning of the current lexeme and `forward` scans ahead until a pattern matches. When `forward` reaches the end of one buffer, the *other* buffer is reloaded and `forward` moves to its start.

**Sentinels.** Without sentinels each advance of `forward` needs two tests: (1) is it the end of a buffer? (2) which character is it (often a multiway branch)? With a **sentinel** `eof`, a character that cannot occur in the program, placed at the end of each buffer, the end-of-buffer test is combined with the character test:

```text
switch (*forward++) {
  case eof:
      if (forward is at end of first buffer)  { reload second buffer; forward = beginning of second buffer; }
      else if (forward is at end of second buffer) { reload first buffer; forward = beginning of first buffer; }
      else /* eof inside a buffer: end of input */ terminate lexical analysis;
      break;
  cases for the other characters;
}
```

The extra test is executed only when the sentinel is actually reached, i.e. once per $N$ characters, so each character costs a single test. An `eof` inside a buffer (not at its end) marks the real end of the input.

**Maximum lexeme length.** A lexeme is safe only while the buffer holding its beginning has not been reloaded. `forward` may travel through the rest of one buffer and one full buffer, but when it reaches the end of the second buffer, the first buffer (which may still contain `lexemeBegin`) is overwritten. So the sum

$$\text{length of lexeme} + \text{distance looked ahead} \le N$$

is what guarantees that a lexeme is never overwritten before it is determined, wherever it starts. **The maximum length of a lexeme the lexer can handle is therefore $N$ characters** (including the lookahead). With a lucky alignment (lexeme starting at the first character of a buffer) it could reach nearly $2N - 1$, but only $N$ is guaranteed for every starting position.

**Example.** Let $N = 4096$ and consider a string literal of length 5000 starting near the start of a buffer: `forward` crosses into the second buffer, and when it reaches the end of the second buffer it must reload the first, destroying the beginning of the literal; the lexer fails. The language design (or the lexer) must then limit literals to about $N$ characters, or use bigger buffers or a copy of the partial lexeme.
