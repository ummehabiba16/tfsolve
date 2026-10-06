---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Peephole optimization examines a small sliding window of target instructions and replaces it by a shorter or faster sequence (repeating until no change). Examples: redundant loads/stores (LD R0, a; ST a, R0 -> LD R0, a), unreachable code (code after an unconditional jump), flow-of-control optimization (goto L1 ... L1: goto L2 -> goto L2), algebraic simplification and strength reduction (x = x + 0, x * 2 -> x + x)."
sources: ["KMS Chapter 8 slides 63-69 (Peephole Optimization)", "Dragon book 2e sec. 8.7"]
---
**Peephole optimization.** The **peephole** is a small sliding window (a few instructions) on the target code; the optimizer replaces the instructions in the window by a shorter or faster sequence whenever it finds a known pattern (Dragon book sec. 8.7). It is applied to target or intermediate code, and **repeated passes** are often needed because one improvement may expose another. Characteristic peephole optimizations: redundant-instruction elimination, flow-of-control optimizations, algebraic simplification, use of machine idioms.

**Technique 1: elimination of redundant loads and stores.** In

```text
LD  R0, a
ST  a, R0
```

the store writes back the value just loaded; it can be deleted (provided no label sits between the two instructions, so that both always execute in sequence): the sequence becomes `LD R0, a`.

**Technique 2: flow-of-control optimization (jumps to jumps) and unreachable code.** Jumps to unconditional jumps can be shortened:

```text
        goto L1                       goto L2
        ...                   ==>     ...
 L1:    goto L2                L1:    goto L2   (removed if no other jump uses L1)
```

and code that follows an unconditional jump and has no label can never be executed and is deleted:

```text
        goto L2                       goto L2
        x = x + 1             ==>
 L2:    ...                    L2:    ...
```

Similarly `if a < b goto L1; goto L2; L1: ...` becomes `if a >= b goto L2; L1: ...`.

**Others (not asked).** *Algebraic simplification and strength reduction*: `x = x + 0`, `x = x * 1` are removed; `x * 2` becomes `x + x` or a shift. *Machine idioms*: `ADD R0, R0, #1` becomes `INC R0`.
