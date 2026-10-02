---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Lex resolves conflicts by (1) always preferring the longest prefix that matches some pattern, and (2) when the longest prefix matches two or more patterns, choosing the pattern listed first in the Lex program (e.g. keywords listed before id)."
sources: ["MMA lexical analysis slides 146-148 (Conflict Resolution in Lex)", "Dragon book 2e sec. 3.5.3"]
---
When several prefixes of the input match one or more patterns, Lex decides by two rules:

1. **Always prefer a longer prefix to a shorter prefix** (longest match). Example: `<=` is one lexeme (relop LE), not `<` followed by `=`. `thenx` is an identifier, not the keyword `then` followed by `x`.
2. **If the longest possible prefix matches two or more patterns, prefer the pattern listed first** in the Lex program. Example: `then` matches both the keyword pattern `then` and the identifier pattern `{letter}({letter}|{digit})*`. Because the keyword rule is listed before the `id` rule, `then` is returned as the keyword.
