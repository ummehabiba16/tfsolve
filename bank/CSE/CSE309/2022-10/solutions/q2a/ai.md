---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An IR is a program representation between source and target code produced by the front end and consumed by the back end. Advantages: retargeting (m front ends + n back ends instead of m x n compilers), machine-independent optimisation, simpler code generation, modular design and portability. Examples: syntax trees/DAGs, three-address code (quadruples, triples), SSA form, Java bytecode, LLVM IR."
sources: ["KMS Chapter 6 slides 2-10 (Intermediate Representation, Why Need IR?, Designing Good IR, Choice of an IR)", "Dragon book 2e sec. 1.2.4, 6.1-6.2"]
---
**Intermediate representation (IR).** A representation of the program that the compiler's **front end** produces from the source program (after lexical, syntax and semantic analysis), and from which the **back end** generates target code. A compiler may use a sequence of IRs, from high-level (close to the source, e.g. syntax trees) to low-level (close to the machine). A good IR is easy to produce from the source and easy to translate into target code.

**Advantages of using an IR:**

1. **Retargeting and reuse.** The front end depends only on the source language, and the back end only on the target machine. A front end for a new language can reuse existing back ends, and vice versa: $m$ languages $\times$ $n$ machines need $m + n$ components instead of $m \times n$ compilers (GCC, LLVM).
2. **Machine-independent optimisation** (common-subexpression elimination, constant propagation, loop optimisations) is done once on the IR, for every target.
3. **Simpler code generation.** Complex source constructs are broken into simple operations with explicit temporaries and jumps, which map easily onto machine instructions.
4. **Modularity:** a clean interface between phases, so they can be developed and tested separately.
5. **Portability:** an IR such as Java bytecode can be interpreted on any machine with a virtual machine.

**Two examples of IR:**

- **Syntax tree / DAG:** e.g. `a + a * (b - c)` as a tree, or as a DAG sharing the node `a`.
- **Three-address code:** e.g.

```text
t1 = b - c
t2 = a * t1
t3 = a + t2
```

(Others: quadruples, triples, SSA form, Java bytecode, LLVM IR.)
