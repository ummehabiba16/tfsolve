---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(a) A lexical error when no pattern matches the input (e.g. the character @): report it and recover by panic mode (delete characters until a valid token) or by deleting/inserting/replacing/transposing one character. (b) A comment start /* inside a comment (comments do not nest in C): either treat it as ordinary comment text, optionally with a warning, or support nesting with a depth counter in a Lex start condition; report an unterminated comment at end of file."
sources: ["MMA lexical analysis slides 29-36 (lexical errors)", "Dragon book 2e sec. 3.1.4"]
---
**(a) No regular expression matches the current input.** The scanner tries to match the longest prefix of the remaining input to a token pattern; if **no** pattern matches any prefix, a lexical error is detected. Example: in the C statement

```c
x = 3 @ 4;
```

`@` begins no token (it is not a letter, digit, operator or punctuation of the language), so no pattern matches. The same happens for a malformed number such as `12.3.4`'s second dot in languages that disallow it, or an unterminated string.

*How to deal with it* (Dragon book sec. 3.1.4):

1. **Report** the error with the line number and the offending character (the scanner must not stop at the first error).
2. **Recover**, so scanning can continue and later errors can be found: (i) **panic mode**, deleting successive characters from the remaining input until a well-formed token starts; (ii) a single-character repair: delete one character, insert a missing one, replace one character, or transpose two adjacent characters.
3. In a Lex program a last catch-all rule does the job: `. { error("illegal character"); }` consumes the bad character, prints a message and continues with the next one.

**(b) A start-comment character (`/*`) inside a comment.** In C, comments **do not nest**: `/* a /* b */` ends at the first `*/`, so the second `/*` is just text inside the comment. If the programmer expected nesting (`/* a /* b */ c */`), the first `*/` closes the comment and ` c */` is then scanned as code: the stray `*/` (and `c`) cause a lexical or syntax error. The same trouble occurs when a comment is not closed (the end of file is reached inside the comment).

*How to deal with it:*

1. **Standard behaviour (no nesting):** inside a comment ignore everything up to the first `*/`; a `/*` inside is ignored too, but a good compiler issues a **warning** ("`/*` within comment") because it usually reveals a missing `*/`.
2. **Allow nested comments** by counting depth with a Lex *start condition*:

```text
%x COMMENT
%%
"/*"              { depth = 1; BEGIN(COMMENT); }
<COMMENT>"/*"     { depth++; }
<COMMENT>"*/"     { if (--depth == 0) BEGIN(INITIAL); }
<COMMENT>.|\n     ;
<COMMENT><<EOF>>  { error("unterminated comment"); return 0; }
```

3. **Unterminated comment:** at end of file inside a comment, report "unterminated comment" with the line where it started, and stop scanning that construct.

*Check:* the nested-comment rules above were compiled with `flex` and run on `a /* x /* y */ z */ b @ c`: the output is the identifiers a, b, c, a nesting warning, and an "illegal character" message for `@`; an unclosed comment is reported as an error.
