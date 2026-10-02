---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) One token relop with attribute LT/LE/... is good: all comparisons occupy the same grammatical position and precedence, so the grammar stays small; the cost is a switch on the attribute in semantic actions. (ii) One token for + - x / is bad: they have different precedence (and - may be unary), which the parser must see, so it needs at least separate tokens per precedence level; the merit is a simpler lexer."
sources: ["MMA lexical analysis slides 17-28, 50-62 (Tokens, Attributes, relop example)", "Dragon book 2e sec. 3.1.2-3.1.3, 3.4"]
---
**(i) Same token for the comparison operators $<, \le, >, \ge, \ne, ==$ (7 marks)**

This is the textbook's choice: token **relop**, with attribute LT, LE, GT, GE, NE or EQ.

*Merits:*

- All comparison operators play the **same syntactic role**: same position in the grammar (`B -> E relop E`), same precedence and associativity. So one grammar rule covers all six, and the grammar and parse table stay small.
- The parser does not need to distinguish them; only the semantic analyser and code generator do, and they get this from the attribute.
- The lexer can recognise all of them with one transition diagram (`getRelop()`).

*Demerits:*

- Semantic actions and code generation need a `switch` on the attribute.
- If the language ever gave some comparison operators different precedence (as C does: `==`/`!=` bind looser than `<`/`>`), one token would not be enough. For C, two tokens (relational and equality) are needed.

**(ii) Same token for the arithmetic operators $+, -, \times, \div$ (8 marks)**

*Merits:*

- The lexer is very simple (one token, attribute = which operator).
- Semantic actions for all binary operators can share code.

*Demerits (serious):*

- $\times$ and $\div$ have **higher precedence** than $+$ and $-$. Precedence is encoded in the grammar by levels (`E -> E addop T`, `T -> T mulop F`), so the **parser must be able to tell the levels apart**. With one token, `a + b * c` and `a * b + c` look identical to the parser, so precedence must be fixed by other means (e.g. Yacc precedence declarations on the attribute, which a plain grammar cannot express), or the grammar becomes ambiguous.
- Unary minus ($-x$) has a different syntax from binary minus; it must be distinguished from $\times$ and $\div$.

**Conclusion:** for comparison operators a single token with attributes is a good design. For arithmetic operators, use at least one token per precedence level (`addop` for $+, -$ and `mulop` for $\times, \div$), or separate tokens.
