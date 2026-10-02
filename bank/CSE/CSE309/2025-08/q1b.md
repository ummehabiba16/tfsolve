---
marks: 12
topics: [tokens, lexer-role]
kind: analysis
mandatory: true
source: {page: 2}
note: "Printed as 'a complier'."
---
You are designing the lexical analyzer for a complier. The language includes the arithmetic operators +, $-$, \* and /. Consider the following options for defining tokens for these operators:

**1. Distinct tokens:** Define completely different tokens for each operator:

- `+` $\to$ `TOK_PLUS`
- `-` $\to$ `TOK_MINUS`
- `*` $\to$ `TOK_MUL`
- `/` $\to$ `TOK_DIV`

**2. Grouped tokens:** Define one token for additive operators and another for multiplicative operators:

- `+`, `-` $\to$ `TOK_ADD_OP`
- `*`, `/` $\to$ `TOK_MUL_OP`

**3. Single token:** Define a single token for all arithmetic operators:

- `+`, `-`, `*`, `/` $\to$ `TOK_ARITH_OP`

Which approach would you recommend and why? Justify your answer with specific trade-offs between implementation complexity and language design requirements.
