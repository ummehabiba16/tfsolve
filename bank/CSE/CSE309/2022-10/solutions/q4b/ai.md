---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "gcc turned the recursion in fact into a loop (tail-recursion elimination with an accumulator: eax = 1; while (n != 0) { eax \\*= n; n--; }), and in main it inlined fact(5) and evaluated it at compile time (constant folding to 120), so printf is called directly with 120; main returns 0 (xor eax, eax). Equivalent C: int fact(int n) { int r = 1; while (n != 0) { r = r \\* n; n = n - 1; } return r; } int main() { printf('%d', 120); return 0; }"
sources: ["KMS Chapter 8 slides 63-69 (An Example From GCC)", "KMS Chapter 9 slides 5-9 (Principle Sources of Optimization)"]
---
**Optimisations performed:**

1. **Recursion turned into iteration (tail-recursion elimination with an accumulator).** `n * fact(n-1)` is not literally a tail call, but multiplication is associative. GCC introduces an accumulator (`eax`, starting at 1) and replaces the recursive calls by the loop `.L2`: `eax = eax * n; n = n - 1; repeat while n != 0`. There are no calls, no stack frames and no return addresses, so it is faster, and the recursion depth no longer limits it.
2. **Test merged into the loop.** `test edi, edi / je .L1` handles `n == 0`: return 1 immediately. `sub edi, 1` sets the zero flag, so `jne .L2` needs no separate compare (a peephole improvement).
3. **Inlining and constant folding in `main`.** The call `fact(5)` was inlined, and since the argument is a constant, the whole computation was done at **compile time**: $5! = 120$. `main` passes `120` directly to `printf` (`mov esi, 120`), and `fact` is not called at all.
4. **Variable `i` eliminated** (constant/copy propagation): it is never stored in memory.
5. **`main` returns 0** (`xor eax, eax`), the implicit `return 0` of C99. The `xor eax, eax` before the call sets `al = 0` for the variadic `printf`. The out-of-line `fact` is kept because it has external linkage.

**Equivalent C program for the optimised code:**

```c
#include <stdio.h>

int fact(int n)
{
    int r = 1;
    while (n != 0) {      /* je .L1 when n == 0 at entry */
        r = r * n;        /* imul eax, edi */
        n = n - 1;        /* sub edi, 1 ; jne .L2 */
    }
    return r;
}

int main() {
    printf("%d", 120);    /* fact(5) computed at compile time */
    return 0;
}
```
