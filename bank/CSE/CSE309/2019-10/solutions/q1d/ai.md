---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "lexemeBegin = forward = 1st +; forward reads the 2nd + and ++ is complete (no +++ in C++), so token INC, lexemeBegin = forward = 3rd +; forward reads the newline, which cannot extend + (++ or +=), so retract and return PLUS; lexemeBegin = forward = newline; if forward reaches the sentinel eof at the end of a buffer half on the way, the other half is reloaded and scanning continues."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering, Buffer Pairs, Sentinels)", "Dragon book 2e sec. 3.2"]
---
Input: `+++\n`. Buffer pair, each half ending with a sentinel `eof`. Initially `lexemeBegin` (lB) and `forward` (f) both point to the first `+`.

```text
   ... | + | + | + | \n | ... | eof |
         ^
        lB, f
```

**Step 1: read the first `+`.** f moves past the first `+`. A `+` may start `+`, `++` or `+=`, so the lexer cannot decide yet and must look at the next character.

**Step 2: read the second `+`.** The next character is `+`, so the lexeme is `++`. In C++ no token begins with `++` and is longer (there is no `+++`), so `++` is complete. No retraction is needed (f was not advanced beyond the lexeme). Return token **INC** (`++`).

```text
   ... | + | + | + | \n | ...
         ^---^
         lexeme "++"
```

Set lB = f = the third `+`.

**Step 3: read the third `+`.** Again it may be `+`, `++` or `+=`. f advances to the next character, which is `\n`. That is neither `+` nor `=`, so the lexeme is just `+`. **Retract** f by one, back to the third `+`. Return token **PLUS** (`+`).

```text
   ... | + | + | + | \n | ...
                 ^   ^
                lB   f (read, then retracted)
```

This is the longest-match rule: `+++` is tokenised as `++` followed by `+`, never `+` `++`.

**Step 4: the newline is found.** lB = f = `\n`. The lexer recognises it as white space (it may count lines for error messages) and skips it without returning a token.

**Buffer boundary.** Each time f advances, the character is compared with `eof`. If one of the `+` or the `\n` is the first character of the next buffer half, f hits the sentinel at the end of the current half. The lexer then reloads the other half and moves f to its beginning, and continues exactly as above. lB still points into the old half, which is not overwritten, so the lexeme is not lost. With sentinels, only one comparison per character is needed except at the buffer ends.
