---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Rule: a token needs an attribute when its pattern matches more than one lexeme (e.g. id, number, relop), so later phases can tell which lexeme it was; tokens matching a single lexeme (if, ;) need none. Attributes need not be single values: e.g. an id carries lexeme, type and location, usually kept as a structure in the symbol table with the token holding a pointer to it."
sources: ["MMA lexical analysis slides 23-28 (Attributes for Tokens)", "Dragon book 2e sec. 3.1.3"]
---
**One-liner rule:** *when more than one lexeme can match a pattern, the lexer must provide an attribute that tells the later phases which lexeme was found.*

- `number` matches `0`, `1`, `3.14`, ...: the code generator needs the value, so the attribute is the value.
- `relop` matches `<`, `<=`, ...: the attribute says which operator (e.g. LE).
- `if` or `;` match exactly one lexeme, so they need no attribute: the token name says everything.

**Are all attributes single values? No.**

- Conceptually, a token has **one** attribute, but it can be a *structure* that combines several pieces of information.
- For an identifier, the information includes the lexeme, its type, and the location where it was first found (for error messages). This is kept in the **symbol-table entry**, and the token's single attribute is a **pointer** to that entry: `<id, pointer to symbol-table entry>`.
- Similarly, a string literal's attribute may be a pointer to the string in a string table.

**Example:** `E = M * C ** 2` gives

`<id, ptr to E>` `<assign_op>` `<id, ptr to M>` `<mult_op>` `<id, ptr to C>` `<exp_op>` `<number, integer value 2>`

Here only `id` and `number` carry attributes.
