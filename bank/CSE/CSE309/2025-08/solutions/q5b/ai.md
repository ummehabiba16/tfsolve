---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "arr is a local array that is never read after the sort and has no other effect, so gcc removed the whole nested loop (dead-code elimination; the i, j loops, comparisons and swaps disappear) and kept only scanf (it has a side effect) plus return 0 (xor eax, eax). If arr were global, its contents would be visible outside main, so the loops could not be deleted (only optimised)."
sources: ["KMS Chapter 8 slides 63-69 (An Example From GCC, Peephole Optimization)", "KMS Chapter 9 slides 24-26 (Dead Code Elimination)"]
---
**What the assembly does.** `sub rsp, 24` makes room for `n` on the stack. `edi` gets the address of the format string `"%d"` and `rsi` the address of `n` (`[rsp+12]`), then `__isoc99_scanf` is called. Then `xor eax, eax` makes the return value 0, the stack is restored, and the function returns. **No code for the loops is left.**

**Optimisations performed:**

1. **Dead-code elimination of the whole sorting loop.** `arr` is a *local* array. Its values are only used inside the loops to compute new values of `arr` itself, and nothing after the loops reads `arr` (main just returns 0). Nothing is printed, returned or passed out. So the loops have no observable effect, and their results are dead. GCC removes the comparisons, the swaps (`temp`, `arr[j] = arr[j+1]`, ...), and then the loop control on `i` and `j`, which is now useless. (Reading the uninitialised `arr` is undefined behaviour anyway, which gives the compiler even more freedom.)
2. **Keeping only side effects.** `scanf` cannot be removed, because it reads input (a side effect), and its argument `&n` must point to memory, so `n` keeps a stack slot. Its return value is ignored.
3. **Small peephole-style choices.** `return 0` becomes `xor eax, eax` (shorter and faster than `mov eax, 0`). The `xor eax, eax` before `call` sets `al = 0` (no vector registers used, required for variadic calls). There is no frame pointer, and the stack is adjusted only once.

**If `arr[10]` is global:** the loops would **not** be removed (GCC may still optimise them internally). A global array is visible outside `main`: other translation units, functions registered with `atexit`, or a debugger may read it after the loops. Its final contents are therefore part of the program's observable state, and the compiler cannot prove the stores are dead. Also, a global array starts as all zeros instead of indeterminate values. So GCC must keep code that performs the sort, i.e. the stores to `arr`.
