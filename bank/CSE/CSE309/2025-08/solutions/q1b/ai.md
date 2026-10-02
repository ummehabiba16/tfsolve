---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Recommend option 2 (grouped tokens TOK\\_ADD\\_OP / TOK\\_MUL\\_OP with the operator as attribute): the grammar needs only one rule per precedence level, while the attribute keeps which operator it was; option 1 bloats the grammar, option 3 loses precedence information the parser needs."
sources: ["MMA lexical analysis slides 17-28 (Tokens, Patterns, Lexemes; Attributes for Tokens)", "Dragon book 2e sec. 3.1.2-3.1.3"]
---
The choice of tokens decides what the **parser** must distinguish (token name) and what can be left to the **attribute** (passed to later phases). The rule: put into the token name exactly what the grammar needs to make its parsing decisions.

| | 1. Distinct tokens | 2. Grouped tokens | 3. Single token |
|:--|:--|:--|:--|
| Lexer | 4 patterns, no attributes | 2 tokens, attribute = which op | 1 token, attribute = which op |
| Grammar | one rule per operator: `E -> E + T`, `E -> E - T`, ... | `E -> E ADD_OP T`, `T -> T MUL_OP F` | needs precedence elsewhere |
| Precedence / associativity | expressed in grammar, but rules double | expressed naturally by levels | **cannot** be expressed in the grammar |
| Semantic actions | one per rule, no switch | `switch` on attribute | `switch` on attribute |
| Unary minus, overloading | easy (`-` is distinct) | `ADD_OP` must check attribute | hard |

**Option 1 (distinct tokens)** gives the parser full information, so special cases such as unary minus or `*` meaning dereference are easy. But the grammar and the parse table grow with every operator, and the four rules per level do the same thing.

**Option 3 (single token)** is the simplest lexer, but the parser cannot tell `+` from `*` from the token alone. Precedence (`*` binds tighter than `+`) and associativity can no longer be written in the grammar. They must be resolved later or by ad-hoc means, which makes the parser and semantic analysis more complex and error-prone.

**Option 2 (grouped tokens)** matches exactly what the grammar needs: operators with the same precedence and associativity behave identically during parsing, so they share a token, and the attribute (`+` or `-`; `*` or `/`) is used only by the semantic actions and code generator. This is the textbook practice: the same token name with attributes for operators of the same class, as with `relop` for $<, \le, =, \ldots$.

**Recommendation:** **option 2**. It keeps the grammar small, encodes precedence through the two levels, and keeps the lexer simple. Choose option 1 only if the language gives individual operators different syntax (for example, unary `-` or `*` as a pointer operator); avoid option 3 for languages with precedence levels.
