---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Tokens: id cse123 (0-5), -- (6-7), ++ (8-9), number 12.45 (10-14), == (15-16), white space (17), number 1 (18), white space (19); forward runs one past an id/number/space and is retracted, while --, ++ and == are complete without lookahead in C."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering), 93-110 (transition-diagram lexer)", "Dragon book 2e sec. 3.2, 3.4"]
---
Positions in the buffer:

```text
position: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
char:     c s e 1 2 3 - - + + 1  2  .  4  5  =  =  _  1  _
```

Rules (C, longest match): `lexemeBegin` marks the start of a lexeme; `forward` scans until the lexeme is certain. For identifiers, numbers and white space, the lexer must read **one character beyond** the lexeme and then retract `forward`. For `--`, `++` and `==`, C has no longer token beginning with them, so the second character completes the token with no further lookahead. After each token, `lexemeBegin` is set to the character after the lexeme.

The table shows, for each step, `lexemeBegin`, the furthest position `forward` reached (and where it is retracted to), and the token found.

| Step | `lexemeBegin` | `forward` (furthest, final) | Token |
|:-:|:-:|:-:|:--|
| 1 | 0 | 6, retract to 5 | `<id, cse123>` |
| 2 | 6 | 7 | `<DEC>` (`--`) |
| 3 | 8 | 9 | `<INC>` (`++`) |
| 4 | 10 | 15, retract to 14 | `<num, 12.45>` |
| 5 | 15 | 16 | `<EQ>` (`==`) |
| 6 | 17 | 18, retract to 17 | white space, no token |
| 7 | 18 | 19, retract to 18 | `<num, 1>` |
| 8 | 19 | 20, retract to 19 | white space, no token |

*In the paper's table these steps are the columns: row 1 = lexemeBegin, row 2 = forward, row 3 = token.*

Explanation of the main steps:

1. From 0, letters and digits are read; `forward` reaches the `-` at 6, which cannot continue an identifier. Retract to 5 and return **id** `cse123` (installed in the symbol table).
2. At 6, `-` can start `-`, `--`, `-=` or `->`. The next character (7) is `-`, so the token is **`--`**.
3. At 8, `+` then `+` gives **`++`**.
4. At 10, digits, `.`, digits are read up to the `=` at 15, which cannot continue a number. Retract and return **number** `12.45`.
5. At 15, `=` then `=` gives **`==`**.
6. At 17, the blank is white space. `forward` sees `1` at 18 and retracts; nothing is returned to the parser.
7. At 18, `1` is followed by a blank at 19, so retract and return **number** `1`.
8. The blank at 19 is skipped as white space.

So the tokens are: id, `--`, `++`, number, `==`, number.
