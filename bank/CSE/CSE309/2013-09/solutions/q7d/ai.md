---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Issues in designing a code generator: input to the generator (IR and symbol table), the target program (absolute, relocatable or assembly code), instruction selection, register allocation and assignment, instruction evaluation order, and memory management; the generator must produce correct, efficient code and itself be easy to build and maintain."
sources: ["KMS Chapter 8 slides 3-26 (issues in code generation)", "Dragon book 2e sec. 8.1"]
---
Main issues (Dragon book sec. 8.1). The code generator must produce **correct** code (the first requirement) and **high-quality** code, and be easy to implement, test and maintain:

1. **Input to the code generator.** The intermediate representation (three-address code, trees, DAGs) produced by the front end and optimizer, plus the symbol table (types, addresses). It is assumed to be free of errors, with all type conversions done.
2. **The target program.** The form of the output: absolute machine code (fast, fixed addresses), **relocatable** machine code (separate compilation, needs linking), or assembly code (easy to produce and debug). The target machine's instruction set (RISC, CISC, stack machine) affects everything else.
3. **Instruction selection.** Mapping IR operations to machine instructions: the uniformity and completeness of the instruction set, instruction speeds and idioms (increment instruction, addressing modes); a naive statement-by-statement translation gives poor code, so the cost of alternatives must be compared.
4. **Register allocation and assignment.** Registers are fastest but few: *allocation* decides which values go into registers, *assignment* decides which register holds each. Finding the optimal assignment is NP-complete, and some instructions need register pairs or specific registers.
5. **Evaluation order.** The order of the computations affects the number of registers needed and the quality of the code; finding the best order is NP-complete.
6. **Memory management.** Names of the IR are mapped to run-time addresses (offsets in activation records, static areas), using the symbol-table information; labels and jumps must be turned into instruction addresses.

**Approaches to code generation:** a simple code generator based on register and address descriptors (basic block at a time), a code generator for expression trees, and generation from DAGs.
