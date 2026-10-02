---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Use a common intermediate representation: build 10 language-specific front ends (lexer, parser, semantic analyser, IR generator) that all produce the same IR, one shared machine-independent optimiser on the IR, and one back end per target machine (instruction selection, register allocation, scheduling). Then 10 languages on k machines need 10 + k components instead of 10 x k complete compilers; front ends can be generated with Lex/Yacc."
sources: ["MMA introduction slides 40-50, 90-98 (Structure of a Compiler, Grouping of Phases into Passes, Compiler-Construction Tools)", "KMS Chapter 6 slides 2-7 (Why Need IR?, LLVM)", "Dragon book 2e sec. 1.2, 1.2.8"]
---
**Assumptions.** The company must support 10 source languages on $k$ target machines (the question does not give $k$). "Efficient" means minimal development effort and maximal reuse.

**Approach: separate front ends and back ends around one common intermediate representation (IR).**

```text
 C ------> [front end 1] --+
 Java ---> [front end 2] --+                               +--> [back end x86]   --> x86 code
 Python -> [front end 3] --+--> common IR --> [optimizer] -+--> [back end ARM]   --> ARM code
   ...          ...        |                               +--> [back end RISC-V]--> RISC-V code
 Lang10 -> [front end 10] -+                                       ...
```

**Design:**

1. **Front end (one per language, 10 in all):** lexical analyser, syntax analyser, semantic analyser (type checking, symbol table) and intermediate-code generator. It depends only on the source language and is **machine-independent**. Each front end translates its language into the **same IR**. Lexers and parsers can be produced with generators (Lex/Flex, Yacc/Bison) from token and grammar specifications, which saves effort.
2. **Common IR:** a well-defined, language- and machine-independent representation, e.g. three-address code in SSA form (as in LLVM). It must be rich enough for all 10 languages: types, calls, exceptions, memory operations.
3. **Machine-independent optimiser (written once):** CSE, constant and copy propagation, dead-code elimination, loop optimisations, all working on the IR. Every language benefits from every optimisation.
4. **Back end (one per target machine):** instruction selection, register allocation, instruction scheduling and peephole optimisation, emitting machine code. It depends only on the target machine.

**Why it is efficient:**

- Without a common IR, every language-machine pair needs its own compiler: $10 \times k$ compilers.
- With it, only $10 + k$ components are needed (10 front ends + $k$ back ends + one shared optimiser). For example, with 3 machines that is 13 instead of 30.
- Adding an 11th language means writing just one front end, which immediately works on all machines. Adding a new machine means one back end, which immediately supports all 10 languages.
- Optimisations and bug fixes in the optimiser or a back end benefit all languages.

This is how GCC and LLVM are organised.
