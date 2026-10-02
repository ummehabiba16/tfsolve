---
marks: 12
topics: [input-buffering, token-recognition]
kind: analysis
source: {page: 36}
---
In lexical analysis, the analyzer often has to look one or more characters beyond the next lexeme before it can be sure it has the right lexeme.

A programming language has got the following tokens:

| Token | Pattern |
|:--|:--|
| Identifiers | Starts with \_ or letter followed by \_ or letter or digit as many times as we want |
| IF | `if` |
| THEN | `then` |
| ELSE | `else` |
| ROR | `>>` |
| ROL | `<<` |
| PLUS | `+` |
| INC | `++` |
| TINC | `+++` |
| GT | `>` |
| GE | `>=` |

Explain which of the above tokens require reading extra characters and which do not.
