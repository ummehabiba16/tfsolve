---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Peephole optimizations examine a small window of target instructions and replace them by a shorter or faster sequence: (1) redundant load/store elimination (LD R0, a ; ST a, R0 -> LD R0, a), (2) unreachable-code elimination (code after an unconditional jump), (3) flow-of-control optimization (goto L1 ... L1: goto L2 -> goto L2)."
sources: ["KMS Chapter 8 slides 63-69 (Peephole Optimization)", "Dragon book 2e sec. 8.7"]
---
**Peephole optimization** (Dragon book sec. 8.7) is a local improvement of the target code: a small sliding window, the *peephole* (a few instructions), is examined and each recognised pattern is replaced by a **shorter or faster** equivalent sequence. It can be repeated until nothing changes, since one replacement may create new opportunities. Common peephole optimizations include redundant-instruction elimination, flow-of-control optimization, algebraic simplification, reduction in strength and use of machine idioms. Three of them:

**1. Redundant loads and stores.**

```text
LD  R0, a                LD  R0, a
ST  a, R0        ==>
```

The store writes back what was just loaded; it is deleted (provided the store has no label, that is, it cannot be reached by a jump that skips the load).

**2. Unreachable code.** An instruction that follows an unconditional jump and carries no label can never be executed and is removed:

```text
    goto L2                     goto L2
    x = x + 1          ==>
L2: ...                     L2: ...
```

(An `if debug == 1 goto L1; goto L2; L1: print...; L2:` with a constant-false `debug` is a typical source of such code.)

**3. Flow-of-control optimization.** Jumps to jumps are replaced by a jump to the final target:

```text
    goto L1                     goto L2
    ...                ==>      ...
L1: goto L2                 L1: goto L2   (deleted if nothing else jumps to L1)
```

and `if a < b goto L1; goto L2; L1: ...` becomes `if a >= b goto L2; L1: ...`, which saves one jump.

**Others.** Algebraic simplification and reduction in strength: `x = x + 0`, `x = x * 1` are deleted, `x * 2` becomes `x + x`; machine idioms: `ADD R0, R0, #1` becomes `INC R0`.
