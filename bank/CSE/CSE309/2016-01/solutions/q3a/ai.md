---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "{cse}{token}: name expansion, the concatenation of the two named definitions cse and token (an error if they are not defined); [csetoken]: any one character from c, s, e, t, o, k, n; csetoken: the string csetoken; (csetoken)+: one or more copies of csetoken; csetoken+: csetoke followed by one or more n."
sources: ["MMA lexical analysis slides 111-148 (Lex / Flex)", "Dragon book 2e sec. 3.5.2"]
---
Each expression, as Lex (Flex) interprets it:

| Expression | Meaning | Lexemes matched |
|:--|:--|:--|
| `{cse}{token}` | **Name expansion.** `{name}` is replaced by the regular expression assigned to `name` in the definitions section. So this is the *concatenation* of the two defined patterns `cse` and `token`; if either name is not defined, Flex reports "undefined definition". | A lexeme of pattern `cse` followed by a lexeme of pattern `token`. With `cse ab` and `token cd` in the definitions section it matches only `abcd`. |
| `[csetoken]` | **Character class.** Any **one** character from the set $\{c, s, e, t, o, k, n\}$ (repeated letters count once). | One character: `c`, `s`, `e`, `t`, `o`, `k` or `n`. |
| `csetoken` | The **literal string** of 8 characters. | Only `csetoken`. |
| `(csetoken)+` | The parentheses group the whole string and `+` means **one or more repetitions** of it. | `csetoken`, `csetokencsetoken`, `csetokencsetokencsetoken`, ... |
| `csetoken+` | `+` applies only to the **last character** `n`. | `csetoke` followed by one or more `n`: `csetoken`, `csetokenn`, `csetokennn`, ... |

Notes: for the input `csetoken` the expressions `csetoken`, `(csetoken)+` and `csetoken+` all match the same 8 characters; Lex then picks the **first** rule in the program (the longest match, with ties broken by order). `[csetoken]` matches only one character, so on `csetoken` it would produce eight separate matches if it were the only rule.

*Check:* the expressions were compiled with `flex` (with `cse ab` and `token cd`) and run on `abcd`, each single letter, `csetoken`, `csetokencsetoken`, `csetokenn` and `csetokennn`; the matches are as in the table, and Flex rejects `{cse}{token}` when the names are undefined.
