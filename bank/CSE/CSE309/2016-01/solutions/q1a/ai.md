---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "None of the three statements contains a lexical error, so panic mode never fires and both scanners produce the same tokens: (i) int float double int float float ; (all keywords; the error is a syntax/semantic one); (ii) ; ) ( } { ) ) ) ) ) id id id (every symbol is a legal token); (iii) int 12345 cse , dhaka ; (number then identifier)."
sources: ["MMA lexical analysis slides 29-36 (Lexical errors, panic mode)", "Dragon book 2e sec. 3.1.4"]
---
**Principle.** A lexical error exists only when **no prefix** of the remaining input matches the pattern of any token (Dragon book sec. 3.1.4). Panic-mode recovery (delete characters until a token can be formed) is triggered only then. If every substring matches some pattern, the scanner reports no error, with or without panic mode, and the two scanners give identical token lists. Errors that depend on how tokens combine (spelling of keywords, order of declarations, missing operators) are found later, by the parser or semantic analyzer. Token names below are my own.

**(i) `int float double int float float;`**

Every word is a keyword and `;` is a valid token. **Lexical errors: none.** Tokens (same with and without panic mode):

```text
INT  FLOAT  DOUBLE  INT  FLOAT  FLOAT  SEMICOLON
```

The statement is wrong (several type specifiers in one declaration, and no declared identifier), but this is detected by the parser or the semantic analyzer, not the scanner.

**(ii) `;) (}{)))))cse dhaka buet`**

Every character is a punctuation symbol that has its own token pattern, and `cse`, `dhaka`, `buet` match the identifier pattern. **Lexical errors: none.** Tokens (with or without panic mode):

```text
SEMICOLON  RPAREN  LPAREN  RBRACE  LBRACE  RPAREN RPAREN RPAREN RPAREN RPAREN
ID(cse)  ID(dhaka)  ID(buet)
```

The unbalanced and badly ordered brackets and the three identifiers in a row are syntax errors, reported by the parser (the scanner does not count brackets).

**(iii) `int 12345cse, dhaka;`**

With the usual patterns $\textit{number} = digit^+$ and $\textit{id} = letter\,(letter \mid digit)^*$, the scanner takes the longest match at each point: `12345` is a **number** (it cannot extend through `c`), then `cse` is an **id**. So there is again **no lexical error**, with or without panic mode:

```text
INT  NUM(12345)  ID(cse)  COMMA  ID(dhaka)  SEMICOLON
```

The parser then rejects `int 12345 cse` (a number where a declarator is required). If the language instead defines a numeric constant as a lexeme that must not be followed by a letter (as C does for `12345cse`, "invalid suffix on integer constant"), then the scanner itself reports the error. In that case:

- *with panic mode*, it deletes characters from the malformed lexeme until a valid token starts and continues with `, dhaka ;` (the tokens become `INT`, `COMMA`, `ID(dhaka)`, `SEMICOLON`);
- *without panic mode* it stops at the error.

**Summary table (standard patterns).**

| Statement | Lexical error? | Tokens without panic mode | Tokens with panic mode |
|:--|:-:|:--|:--|
| (i) | no | 7 tokens as above | same |
| (ii) | no | 13 tokens as above | same |
| (iii) | no | 6 tokens as above | same |
