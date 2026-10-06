---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "{cse}{buet}: concatenation of the two named definitions cse and buet (error if undefined); [csebuet]: one character from c, s, e, b, u, t; {csebuet}: expansion of the definition named csebuet; csebuet: the literal string; (csebuet)+: one or more copies of csebuet; csebuet+: csebue followed by one or more t."
sources: ["MMA lexical analysis slides 111-148 (Lex / Flex)", "Dragon book 2e sec. 3.5.2"]
---
Assumption: the printed spaces in `(csebuet) +` and `csebuet +` are typographical. In a real Lex program a blank would end the pattern, so the intended expressions are `(csebuet)+` and `csebuet+`.

| Expression | Meaning in Lex | Matches |
|:--|:--|:--|
| `{cse}{buet}` | **Name expansion twice, concatenated.** `{name}` is replaced by the regular expression defined for `name` in the definitions section. So it is the pattern `cse` followed by the pattern `buet` (undefined names are an error). | With `cse ab` and `buet cd`, only `abcd`. |
| `[csebuet]` | **Character class:** exactly **one** character, any of `c s e b u t`. | `c`, `s`, `e`, `b`, `u` or `t` |
| `{csebuet}` | **Name expansion:** the regular expression defined under the **name** `csebuet` (not the letters). Undefined $\to$ error. | whatever the definition `csebuet ...` describes |
| `csebuet` | The **literal string** of six characters. | `csebuet` only |
| `(csebuet)+` | Parentheses group the whole string; `+` means **one or more copies** of it. | `csebuet`, `csebuetcsebuet`, ... |
| `csebuet+` | `+` applies only to the **last character `t`**. | `csebue` followed by one or more `t`: `csebuet`, `csebuett`, `csebuettt`, ... |

The differences in short: `{...}` refers to a *name* defined earlier, `[...]` is a *set of single characters*, `(...)+` repeats the *whole word*, and a trailing `+` repeats only the *last letter*. On the input `csebuet` the expressions `csebuet`, `(csebuet)+` and `csebuet+` all match 7 characters; Lex then takes the rule listed first.

*Check:* the expressions were compiled with `flex` using `cse ab`, `buet cd` and `csebuet xy` as definitions, and run on `abcd`, `s`, `xy`, `csebuet`, `csebuetcsebuet` and `csebuett`: the matches are as listed (`abcd` by the first, `s` by the class, `xy` by `{csebuet}`, `csebuett` by `csebuet+`).
