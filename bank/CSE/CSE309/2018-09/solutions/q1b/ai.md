---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Flaws: '.' unescaped matches any character; the fraction is not optional (the ? only applies to the last [0-9]\\*); the exponent group has no ? so it is mandatory; 'E+' means one-or-more E's and the sign is not a class [+-]; the exponent digits [0-9]\\* allow an empty exponent (123E); (blanks would be literal in Lex). Correct: number -> [0-9]+(\\.[0-9]+)?(E[+-]?[0-9]+)?."
sources: ["MMA lexical analysis slides 50-62 (Recognition of Tokens, regular definitions for numbers), 111-148 (Lex)", "Dragon book 2e sec. 3.3.4-3.3.5 (Example 3.6, 3.7)"]
---
Given:

```text
number -> [0-9] [0-9]*.[0-9] [0-9]*?(E +-?[0-9]*)
```

Required form: digits, an optional decimal part (`.` followed by digits), and an optional exponent (`E`, an optional `+` or `-`, digits). Examples: `123`, `123.456`, `123.456E+789`, `123E-7`.

**Flaws:**

1. **Unescaped dot.** In regular expressions (Lex), `.` means *any character except newline*. As written, `123x456` would match. It must be `\.` (or `"."`).
2. **Decimal part is not optional.** `[0-9]*?` applies the `?` to the last `[0-9]*` only (which is already optional, so `?` has no effect). The `.` and the first fraction digit `[0-9]` are mandatory, so `123` or `123E5` are rejected. The whole fraction must be grouped and made optional: `(\.[0-9]+)?`.
3. **Exponent part is not optional.** The group `(E +-?[0-9]*)` has no `?` after it, so every number would need an exponent. It must be `( ... )?`.
4. **Wrong use of `+` for the sign.** `+` is an operator ("one or more"), so `E+` means one or more `E`s. `-?` makes only a minus optional, so a `+` sign is not even matched as a character. The sign should be a character class: `[+-]?` (or `(\+|-)?`).
5. **Exponent may be empty.** `[0-9]*` allows zero digits, so `123.4E` or `123.4E-` would be accepted. It should be `[0-9]+`.
6. **Blanks.** If written literally in Lex, the spaces in `E +-` are part of the pattern and would have to appear in the input. There should be no blanks.
7. (Style) `[0-9][0-9]*` is just `[0-9]+`. This is correct but clumsy; with a regular definition `digit -> [0-9]` it is clearer.

**Corrected regular definitions** (textbook style):

```text
digit            -> [0-9]
digits           -> digit+
optionalFraction -> (\. digits)?
optionalExponent -> (E [+-]? digits)?
number           -> digits optionalFraction optionalExponent
```

or in one Lex pattern: `[0-9]+(\.[0-9]+)?(E[+-]?[0-9]+)?`.
