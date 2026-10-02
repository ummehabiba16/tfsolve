---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "factorial always returns 0 (the loop ends by multiplying by i = 0; fact is uninitialised) so its body becomes xor eax, eax; in main: t eliminated in the swap (copy propagation into registers), x = y^y folded to 0 (algebraic identity), if (x) removed and n = 20 (constant propagation, dead branch), factorial inlined and k = 0, the inner loop keeps a[j] and b[j] in registers (load/store hoisting out of the loop), is unrolled by 2 (two imul, edx -= 2), j is replaced by the byte offset rsi += 4 up to 200 (strength reduction, induction-variable elimination), and the loop after return 0 is removed (unreachable code)."
sources: ["KMS Chapter 8 slides 63-69 (An Example From GCC, Peephole Optimization)", "KMS Chapter 9 slides 5-35", "Dragon book 2e sec. 8.7, 9.1"]
---
**Assumptions.** x86-64, 4-byte `int`, globals addressed RIP-relative.

| C code | Assembly | Optimisation |
|:--|:--|:--|
| `factorial`: `fact` uninitialised; loop `for (i = n; i >= 0; i--) fact = fact * i;` | `xor eax, eax` / `ret` | The last iteration always multiplies by `i = 0`, so the result is 0 (and for `n < 0` the uninitialised value is undefined, so 0 is allowed). **Algebraic simplification** ($x \times 0 = 0$) plus **dead-code elimination** of the loop: the function just returns 0 |
| `t = y; y = z; z = t;` | `mov eax, y` / `mov edx, z` / `mov y, edx` / `mov z, eax` | **Copy propagation** and **register allocation**: `t` never exists in memory; the swap is two loads and two stores |
| `x = y ^ y;` | `mov x, 0` | **Algebraic identity** $y \oplus y = 0$ and **constant folding**; `y` is not even read for it |
| `if (x) n = 10; else n = 20;` | `mov n, 20` | **Constant propagation** ($x = 0$) and **dead (unreachable) branch elimination** |
| `k = factorial(n);` | `mov k, 0` | **Inlining** of `factorial` and **constant propagation** of its result, so no call. The out-of-line copy of `factorial` remains because it has external linkage |
| nested loop `a[j] *= b[j]` | `.L4`/`.L5` loops | see below |
| loop after `return 0;` | (nothing) | **Unreachable-code elimination** |
| `return 0;` | `xor eax, eax` | Peephole idiom (shorter than `mov eax, 0`) |

**The nested loop** (`for j < 50: for i < 100: a[j] *= b[j]`):

- **Code motion of loads and stores (scalar replacement).** `a[j]` and `b[j]` do not change with `i`. So `a[j]` is loaded once into `eax` and `b[j]` into `ecx` before the inner loop (`.L4`). The inner loop works only on registers, and `a[j]` is stored once after it (`mov a[rsi], eax`). This replaces 100 loads and stores per `j` by one of each.
- **Loop unrolling.** The inner loop body contains two `imul eax, ecx` and the counter `edx` goes from 100 down by 2. That is 50 iterations, each doing two of the original iterations, which halves the loop overhead.
- **Reversed loop counter.** `i` is replaced by a down-counter (`sub edx, 2` / `jne`), so no compare instruction is needed. `i` itself is eliminated.
- **Strength reduction and induction-variable elimination for `j`.** The address `a + 4j` is computed with the byte offset `rsi`, which starts at 0 (`xor esi, esi`) and increases by 4 each time (`add rsi, 4`). The test `j < 50` becomes `rsi < 200` ($= 50 \times 4$), so `j` disappears.
- **Instruction scheduling.** The stores to `x`, `n`, `y`, `z`, `k` are reordered and interleaved with the initialisation of `esi`.
