---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Compiler-construction tools: scanner generators (Lex/Flex), parser generators (Yacc/Bison, ANTLR), syntax-directed translation engines, automatic code-generator generators (instruction selection by tree patterns), data-flow analysis engines and compiler-construction toolkits (LLVM, GCC); each takes a specification and produces a component of the compiler."
sources: ["MMA introduction slides 40-98 (compiler construction tools)", "Dragon book 2e sec. 1.2 and ch. 3, 4, 5, 8, 9"]
---
**Compiler-construction tools** are programs that help build a compiler: from a *specification* of a phase they generate its implementation, which saves effort and reduces errors. The main kinds:

1. **Scanner generators** produce lexical analyzers from regular-expression descriptions of the tokens. They build a DFA (or NFA) and a driver. Examples: **Lex, Flex, JFlex**.

2. **Parser generators** produce syntax analyzers (parsers) from a context-free grammar. Examples: **Yacc, Bison** (LALR parsers), **ANTLR, JavaCC** (LL parsers). Semantic actions in C or other code can be attached to the productions.

3. **Syntax-directed translation engines** produce routines that walk the parse tree and generate intermediate code (or evaluate attributes) from translation rules associated with each node; attribute-grammar tools belong here.

4. **Automatic code-generator generators** take a collection of rules for translating each operation of the intermediate language into the machine language of a target machine, and produce a code generator, usually by tree-pattern matching and dynamic programming. Examples: **BURG/IBURG**, the instruction selector description files (TableGen) of LLVM.

5. **Data-flow analysis engines** help gather information about how values are transmitted from one part of the program to another (the basis of optimization): reaching definitions, live variables, available expressions.

6. **Compiler-construction toolkits** are integrated sets of routines for building the various phases (intermediate representation, symbol-table management, optimizers, back ends). Examples: **LLVM** and the **GCC** middle and back ends, which reuse one optimizer for many languages and targets.

**Example of use.** A small compiler: write `scanner.l` for the tokens $\to$ `flex` creates the lexer; write `parser.y` with the grammar and actions $\to$ `bison` creates the parser; link both with a hand-written code generator. The first two phases are produced automatically.
