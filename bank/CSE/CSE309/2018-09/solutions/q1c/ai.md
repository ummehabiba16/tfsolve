---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Panic mode: when no token pattern matches a prefix of the remaining input, the lexer deletes successive characters until a well-formed token can be found (then continues); simple and good for interactive use, but side effects: it may delete valid characters and split/merge tokens, so the parser gets a wrong token stream and reports confusing cascades of syntax errors, and more errors may go unnoticed."
sources: ["MMA lexical analysis slides 29-36 (Lexical Errors)", "Dragon book 2e sec. 3.1.4"]
---
**Panic-mode recovery in lexical analysis.** A lexical error occurs when the lexer cannot match **any** token pattern to a prefix of the remaining input (e.g. an illegal character `@` or `$` in C, or `12ab` in some languages). The simplest recovery is **panic mode**: delete successive characters from the remaining input until the lexer can find a well-formed token at the beginning of what is left, then continue normally.

**Example:** in `x = 3 @# + y;`, the lexer deletes `@` and `#`, and the parser receives `x = 3 + y ;`.

**Advantages:** very easy to implement, cannot loop, and often adequate (especially in interactive environments).

**Side effects:**

1. **Valid characters may be lost.** Deleting up to the next recognisable token may throw away parts of correct tokens. For example, in `count@er = 5`, deleting `@` gives the two tokens `count` and `er`, i.e. `id id`, which is a different program.
2. **Misleading token stream.** The parser receives a token sequence the programmer never wrote. This causes **cascading (spurious) syntax errors** later, which confuse the user.
3. **Errors may be masked.** Text skipped during recovery is not checked, so further real errors in it are not reported.
4. **Wrong error position.** The reported location and message may not reflect what was really wrong (e.g. a missing quote of a string is "fixed" by deleting characters far away).

Other single-character repairs (insert, replace, or transpose a character) can sometimes give a more sensible correction than deleting.
