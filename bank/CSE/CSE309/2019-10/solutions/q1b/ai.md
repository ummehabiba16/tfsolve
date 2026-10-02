---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The lexer deals with characters using regular expressions (identifiers, numbers, white space, comments) while the parser works on a token stream with a CFG; e.g. for 'count = count + 1; /\\* c \\*/' the parser just sees id = id + num ;, so its grammar needs no rules for blanks/comments/character details and both parts are small, separately designed and generated (Lex/Yacc)."
sources: ["MMA lexical analysis slides 13-16 (Lexical Analysis Versus Parsing)", "Dragon book 2e sec. 3.1.1"]
---
Separating the two phases simplifies the design of **both**:

1. **The parser's grammar works on tokens, not characters.** The lexer removes white space and comments and groups characters into tokens. Example:

```c
position = initial + rate * 60;   /* compute */
```

The lexer produces

```text
<id,1> <=> <id,2> <+> <id,3> <*> <number,60> <;>
```

and the parser only needs `stmt -> id = expr ;` and `expr -> expr + term | ...`. If the parser had to handle characters, every rule would need optional blanks and comments between symbols (`stmt -> ws id ws = ws expr ws ;`) and rules for spelling identifiers letter by letter. The grammar would become huge and unreadable.

2. **Each phase uses the simplest adequate formalism.** Tokens are regular, so the lexer uses regular expressions and finite automata. Nesting (parentheses, blocks) needs a context-free grammar and a stack-based parser. Neither phase has to deal with the other's complexity.

3. **Independent design, testing and tools.** The lexer can be written or generated (Lex) and tested on its own; likewise the parser (Yacc). Errors are separated into lexical errors (illegal characters) and syntax errors.

4. **Localised changes.** Changing how numbers or keywords are spelled affects only the lexer; changing statement syntax affects only the grammar.

(Efficiency and portability are additional benefits of the separation.)
