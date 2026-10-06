---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A token is <token-name, attribute-value>: the parser uses only the token name (an abstract terminal symbol) to decide what production to apply, while the attribute value (a symbol-table pointer for an id, the value for a number) carries the information about the particular lexeme that later phases need for translation (type checking, code generation)."
sources: ["MMA lexical analysis slides 17-28 (tokens, patterns, lexemes, attributes)", "Dragon book 2e sec. 3.1.3"]
---
The lexical analyzer returns a token $\langle token\text{-}name, attribute\text{-}value\rangle$ for every lexeme (Dragon book sec. 3.1.3).

**The token name influences parsing decisions.** The *token name* is an abstract symbol, a terminal of the grammar (`id`, `number`, `+`, `if`, ...). The parser uses **only token names** when it parses: it must decide which production to use depending on whether the next token is an **id**, a **number**, an **if**..., and it does not care *which* identifier it is. For the grammar $E \to E + T \mid T$, an identifier `rate` and an identifier `count` are the same terminal **id**.

**The attribute value influences the translation of tokens after the parse.** The *attribute value* carries the information about the specific lexeme that the later phases need: for an **id**, a pointer to its symbol-table entry (name, type, scope, address); for a **number**, its value; for a relational operator, which one (`<`, `<=`...). This information is used by semantic analysis (type checking), and by code generation, after (or while) the parse tree has been built.

**Example.** `position = initial + rate * 60` gives the tokens

```text
<id, 1> <=> <id, 2> <+> <id, 3> <*> <number, 60>
```

The parser sees the sequence `id = id + id * number` and checks that the structure is a valid assignment. The attributes 1, 2, 3 (symbol-table entries of `position`, `initial`, `rate`) and 60 are used afterwards to look up types, to insert the `int-to-float` conversion of 60 and to generate code for the right variable. The parse would be identical for any other identifiers; the translation is not.
