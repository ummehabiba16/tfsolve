---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Intermediate code decouples the front end (source-dependent) from the back end (machine-dependent): n languages and m machines need n front ends and m back ends instead of n*m compilers, machine-independent optimization is done once on the IR, and each end is simpler."
sources: ["MMA compiler phases slides 40-98", "KMS Chapter 6 slides 1-19", "Dragon book 2e sec. 1.2.4, 6.1"]
---
Between the front end (analysis: lexical, syntax, semantic) and the back end (synthesis: code generation for a target machine) the compiler produces an **intermediate representation** (IR), for example three-address code. The reasons (Dragon book sec. 1.2.4 and 6.1):

1. **Retargetability.** The front end knows only the source language and the back end only the target machine. With an IR, $n$ source languages and $m$ target machines need $n$ front ends + $m$ back ends instead of $n \times m$ separate compilers (the classical argument for a common intermediate language).

2. **Machine-independent optimization.** Optimizations such as common-subexpression elimination, constant folding and loop-invariant code motion are performed once on the IR, and every back end benefits from them.

3. **Simplicity.** The source language need not be translated directly into machine instructions with all their addressing modes and registers; each phase handles one problem. The IR is neither about the source language nor about the machine.

**Example.** For the C statement `a = b + c * d;` the front end produces

```text
t1 = c * d
t2 = b + t1
a  = t2
```

A back end for x86 turns this into `mov`, `imul`, `add` instructions, a back end for ARM or MIPS into their own instructions, while the front end (and the optimizer) is the same. In the same way, a C, C++ or Fortran front end can feed the same optimizer and the same back ends.
