---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Without sentinels each character read costs two tests (end of buffer? which character?); with an eof sentinel at the end of each buffer the end-of-buffer test is merged with the character test, so only one test per character is made except when the sentinel is actually reached (once per N characters)."
sources: ["MMA lexical analysis slides 46-49 (Sentinels)", "Dragon book 2e sec. 3.2.2"]
---
**Without sentinels.** Every time `forward` is advanced we must (1) test whether we have moved off one of the buffers (and, if so, reload the other buffer), and (2) determine which character was read (often a multiway branch: letter, digit, operator, white space...). So **two tests per input character**.

**With sentinels.** We extend each buffer by one extra cell holding a **sentinel** character that cannot occur in a program, naturally `eof`. Now the end-of-buffer test is a special case of the character test: reading `eof` is just one more outcome of the multiway branch that is performed anyway. The algorithm for advancing `forward` is

```text
switch (*forward++) {
  case eof:
      if (forward is at the end of the first buffer)  { reload the second buffer; forward = beginning of second buffer; }
      else if (forward is at the end of the second buffer) { reload the first buffer; forward = beginning of first buffer; }
      else /* eof inside a buffer */ terminate lexical analysis;
      break;
  cases for the other characters;
}
```

**Why it is faster.** The first test, which is part of the multiway branch on the character, is the **only test made per character**. The extra comparison (is this the end of buffer 1 or 2, or the real end of input?) is executed **only when the sentinel is reached**, i.e. once per buffer of $N$ characters (for example once per 4096 characters) instead of for every character. The cost of buffer management therefore falls from 2 tests per character to about $1 + 1/N$.

An `eof` that appears anywhere other than at the end of a buffer means that the whole input has ended.
