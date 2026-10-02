---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Scheme 1 (one MATHOP token) is acceptable lexically but bad for parsing: the parser cannot see the precedence of \\* and / over + and -. Scheme 2 (PM and MD tokens with attributes) is the best: one token per precedence level, small grammar, operator kept as attribute. Scheme 3 (one token per operator) is acceptable and gives full information but makes the grammar and table larger with duplicate rules."
sources: ["MMA lexical analysis slides 17-28 (Tokens, Patterns, Lexemes, Attributes)", "Dragon book 2e sec. 3.1.2-3.1.3"]
---
| Scheme | Acceptability | Merits | Demerits |
|:-:|:--|:--|:--|
| 1: one token MATHOP with attribute | Acceptable lexically, **poor for parsing** | Simplest lexer; one grammar rule for all binary operators | The parser cannot distinguish $+,-$ from $*,/$, so **precedence cannot be expressed in the grammar**; it must be handled by extra means (e.g. Yacc precedence on attributes) or the grammar becomes ambiguous; the semantic actions need a `switch` |
| 2: PM (+, -) and MD (\*, /) with attributes | **Best choice** | One token per **precedence level**: the grammar `E -> E PM T`, `E -> T`, `T -> T MD F`, `T -> F` encodes precedence and associativity with few rules; the attribute tells the code generator which operator | Semantic actions must check the attribute; unary minus must be handled separately |
| 3: separate tokens PLUS, MINUS, MULT, DIV | **Acceptable** | Parser has full information; no attributes needed; easy to treat unary minus or overloaded operators specially | More tokens and grammar rules (`E -> E + T`, `E -> E - T`, `E -> T`, ...), larger parse table, and repeated semantic actions |

**Conclusion:** tokens should distinguish exactly what the **parser** needs. The parser needs precedence levels, but not the individual operator within a level. So Scheme 2 is the best compromise, Scheme 3 is correct but verbose, and Scheme 1 loses information the parser needs.
