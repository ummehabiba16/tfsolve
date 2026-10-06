---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "{mytoken}: expansion of the definition named mytoken (error if undefined); [mytoken]: one character from m, y, t, o, k, e, n; mytoken: the literal string; (mytoken)+: one or more repetitions of the string; mytoken+: mytoke followed by one or more n."
sources: ["MMA lexical analysis slides 111-148 (Lex / Flex)", "Dragon book 2e sec. 3.5.2"]
---
Assumption: the printed space in `(mytoken) +` is typographical; in a Lex program a blank would end the pattern, so the intended expression is `(mytoken)+`.

| Expression | Meaning in Lex | Lexemes matched |
|:--|:--|:--|
| `{mytoken}` | **Name expansion**: the regular expression defined under the **name** `mytoken` in the definitions section is substituted (it is an error if no such definition exists). | whatever the definition `mytoken ...` describes; with `mytoken ab`, only `ab` |
| `[mytoken]` | **Character class**: exactly **one** character from the set $\{m, y, t, o, k, e, n\}$. | `m`, `y`, `t`, `o`, `k`, `e` or `n` (one character) |
| `mytoken` | The **literal string** of 7 characters. | only `mytoken` |
| `(mytoken)+` | The parentheses group the whole string; `+` means **one or more** repetitions of it. | `mytoken`, `mytokenmytoken`, ... |
| `mytoken+` | `+` applies only to the **last character** `n`. | `mytoke` followed by one or more `n`: `mytoken`, `mytokenn`, `mytokennn`, ... |

The expressions differ in what is repeated or chosen: a *name* (`{...}`), a *single character from a set* (`[...]`), the *whole word* (`mytoken`, `(mytoken)+`) or only its *last letter* (`mytoken+`). For `mytoken` itself the third, fourth and fifth expressions all match 7 characters, and Lex picks the first listed rule.

*Check:* the five expressions were compiled with `flex` (definition `mytoken ab`) and run on `ab`, each of the letters, `mytoken`, `mytokenmytoken`, `mytokenn` and `mytokennn`; the matches are as in the table.
