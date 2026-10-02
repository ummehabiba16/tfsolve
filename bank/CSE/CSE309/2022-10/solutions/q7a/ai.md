---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "i {mytoken}: the regular definition named mytoken (defined in the declarations section) is substituted; ii [mytoken]: a character class, any ONE of the characters m, y, t, o, k, e, n; iii mytoken: the literal string mytoken; iv (mytoken)+: one or more repetitions of the string mytoken; v mytoken +: in Lex a blank ends the pattern, so this is the pattern mytoken followed by an action '+' (an error); if written mytoken+ it means mytoke followed by one or more n; vi (mytoken)\\*: zero or more repetitions of the string (includes the empty string); vii mytoken\\*: mytoke followed by zero or more n."
sources: ["MMA lexical analysis slides 111-148 (The Lexical-Analyzer Generator Lex, Structure of Lex Programs)", "Dragon book 2e sec. 3.3.3, 3.5"]
---
In Lex, operators such as `+`, `*` and `?` apply to the **single preceding item** (a character, a bracketed class, a `{name}` or a parenthesised group). Parentheses group a whole string.

| | Regular expression | Meaning | Example matches |
|:-:|:--|:--|:--|
| i | `{mytoken}` | Use of a **regular definition** called `mytoken`, declared in the declarations section (e.g. `mytoken [a-z]+`). The braces are replaced by that definition | whatever the definition matches |
| ii | `[mytoken]` | A **character class**: exactly **one** character, any of `m y t o k e n` (order and repetition do not matter) | `m`, `t`, `n` (one character only) |
| iii | `mytoken` | The **literal string** `mytoken` | `mytoken` |
| iv | `(mytoken)+` | One or more repetitions of the whole string | `mytoken`, `mytokenmytoken`, ... |
| v | `mytoken +` | In the rules section a **blank ends the pattern**, so this is the pattern `mytoken` followed by the action text `+` (not a valid action). If written without the blank, `mytoken+` means `mytoke` followed by one or more `n` (`+` applies only to `n`) | `mytoken`, `mytokenn`, `mytokennn` (for `mytoken+`) |
| vi | `(mytoken)*` | Zero or more repetitions of the string, **including the empty string** | (empty), `mytoken`, `mytokenmytoken` |
| vii | `mytoken*` | `mytoke` followed by zero or more `n` (`*` applies only to `n`) | `mytoke`, `mytoken`, `mytokennn` |

**Key differences:** braces name a definition; square brackets give a set of single characters; parentheses group the whole string for `+`/`*`; without parentheses the operator binds only to the last character; `+` means at least one, `*` means zero or more.
