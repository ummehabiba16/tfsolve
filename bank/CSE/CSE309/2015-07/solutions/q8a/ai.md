---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "When several prefixes of the input match one or more patterns, Lex (1) selects the longest prefix that matches any pattern, and (2) if that longest prefix matches more than one pattern, selects the pattern listed first in the Lex program."
sources: ["MMA lexical analysis slides 111-148 (Lex conflict resolution)", "Dragon book 2e sec. 3.5.2-3.5.3"]
---
Lex (Flex) resolves conflicts with two rules (Dragon book sec. 3.5.3):

1. **Longest match.** Always prefer a longer prefix of the remaining input to a shorter one. For example, `<=` is read as one token, the relational operator, not as `<` followed by `=`, and `ifx` is one identifier, not the keyword `if` followed by `x`.
2. **First rule on ties.** If the longest prefix matches more than one pattern, the pattern listed **first in the Lex program** is chosen. So keywords must be listed before the identifier pattern: for the input `if` both the keyword rule and the identifier rule match 2 characters, and the keyword rule (listed first) wins.

```text
%%
if          { return IF; }       /* listed first: wins for the input "if"  */
[a-z]+      { return ID; }       /* wins for "ifx" because it matches longer */
```

If no rule matches, the default action copies the character to the output. (The lexeme chosen is available in `yytext`, with length `yyleng`; the unused part of the input is put back.)
