---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Simplicity: the lexer removes white space and comments and groups characters with simple regular expressions/DFAs, so the grammar for the parser deals only with tokens and stays small; each phase uses the right formalism and can be built, tested and generated (Lex/Yacc) separately. Efficiency and portability are secondary benefits."
sources: ["MMA lexical analysis slides 13-16 (Lexical Analysis Versus Parsing)", "Dragon book 2e sec. 3.1.1"]
---
The textbook gives three reasons for separating lexical analysis from parsing: **simplicity of design**, efficiency and portability. Simplicity is the most important.

**Why simplicity matters most**

**1. Each phase handles one level of structure.**

- Lexical structure (identifiers, numbers, operators) is regular and is specified by **regular expressions**, recognised by finite automata.
- Syntactic structure (nested expressions and statements) needs a **context-free grammar** and a stack-based parser.

Mixing them forces the parser to deal with individual characters, making its grammar much larger.

**2. White space and comments disappear.** If the parser had to handle them, every grammar rule would need optional white space and comments between all symbols, e.g. `stmt -> id ws? = ws? expr ws? ;`. The lexer removes them, so the grammar is written over tokens only: `stmt -> id = expr ;`.

**3. Smaller, clearer components.** A small lexer and a token-level grammar are each easy to understand, test and debug. Errors are reported at the right level (lexical vs syntax). Each can be generated automatically (Lex, Yacc).

**4. Easier change.** Changing the spelling of tokens (e.g. allowing `0x` hex numbers) only affects the lexer, and changing syntax only affects the grammar.

**Other reasons (secondary):**

- **Efficiency**: specialised buffering (buffer pairs, sentinels) and DFA scanning speed up the slowest phase.
- **Portability**: input-device and character-set peculiarities are confined to the lexer.

Since efficiency and portability could, in principle, be obtained in other ways, while a clean, simple design is what keeps both phases manageable, simplicity of design is the main justification.
