---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Single buffer: simpler, less memory, but when forward reaches the end the buffer must be reloaded, which can overwrite the beginning of the current lexeme (lexemeBegin) and loses lookahead; buffer pairs reload one half while the other still holds the lexeme start, so lexemes up to N characters are safe; with sentinels both need only one test per character."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering, Buffer Pairs, Sentinels)", "Dragon book 2e sec. 3.2.1-3.2.2"]
---
| | Single buffer | Buffer pair |
|:--|:--|:--|
| Memory | $N$ characters | $2N$ characters |
| Code | simpler: one buffer, one reload point | two halves, reload alternately |
| Lexeme crossing the end | when `forward` reaches the end, reloading overwrites the start of the current lexeme (`lexemeBegin`), so the lexeme is lost unless it is first copied | the other half still holds the beginning of the lexeme; only the half `forward` is entering is reloaded |
| Lookahead / retracting | a reload loses characters that may need to be re-read | `forward` can be retracted across the boundary |
| Max lexeme length | effectively the part left before the end of the buffer (unpredictable) | up to $N$ characters is always safe |

**Advantages of a single buffer:** less memory, simpler logic. It is acceptable when lexemes are short and can be copied out before reloading, or when the whole file fits in memory.

**Disadvantages:** a lexeme that straddles the end of the buffer is the main problem. Before reloading, the lexer must move the partial lexeme to the front of the buffer (extra copying), or it loses it.

Both schemes normally use a **sentinel** (`eof`) at the end of each buffer, so the end-of-buffer test is merged with the character test, giving one comparison per character in the common case.
