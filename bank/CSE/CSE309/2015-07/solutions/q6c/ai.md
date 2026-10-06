---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The analysis (front end) part breaks the source program into pieces, imposes a grammatical structure on them and builds an intermediate representation: lexical analysis (tokens), syntax analysis (parse/syntax tree), semantic analysis (type checking, coercions), together with the symbol table and error reporting; it also collects the information the synthesis part needs."
sources: ["MMA introduction slides 40-98 (phases of a compiler)", "Dragon book 2e sec. 1.2"]
---
The compiler has two parts: **analysis** (the *front end*) and **synthesis** (the back end). The analysis part (Dragon book sec. 1.2):

1. **Breaks up the source program into constituent pieces** and **imposes a grammatical structure** on them;
2. uses this structure to **create an intermediate representation** of the source program;
3. **detects and reports** syntactic and semantic errors, so that the user can correct them;
4. **collects information about the source program** in the **symbol table** and passes it, with the intermediate representation, to the synthesis part.

It is built from three phases:

| Phase | Role |
|:--|:--|
| **Lexical analysis** (scanning) | Reads the character stream and groups characters into **lexemes**, producing a token $\langle token\text{-}name, attribute\text{-}value\rangle$ for each; removes white space and comments, enters identifiers into the symbol table. |
| **Syntax analysis** (parsing) | Uses the tokens to build a **parse / syntax tree** that shows the grammatical structure of the program; reports syntax errors. |
| **Semantic analysis** | Checks the tree for **semantic consistency** with the language definition (declarations, types, scope); performs type checking and coercions, and gathers type information for code generation. |

The result, usually followed by intermediate-code generation, is machine-independent and depends only on the source language.
