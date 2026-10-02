---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "The activation tree has root main, child binCoeff(5,3) and 19 binCoeff activations in all (result 10); the deepest path main - (5,3) - (4,2) - (3,1) - (2,1) - (1,0) gives at most 6 activation records on the stack at once (5 for binCoeff plus main). When the base case is first reached, in binCoeff(2,0), the control stack holds main, (n=5, r=3), (n=4, r=2), (n=3, r=1), (n=2, r=0), with (2,0) on top."
sources: ["KMS Chapter 7 slides 9-18 (Stack Allocation, Activation Tree, Control Stack, Activation Records)", "Dragon book 2e sec. 7.2.1-7.2.2"]
---
**Assumptions.** In `binCoeff(n-1, r-1) + binCoeff(n-1, r)`, the **left call is executed first** (C++ does not fix the order of evaluation of operands; left to right is assumed). `main` counts as an activation. `cout` belongs to a library and its activations are not shown.

**(i) Activation tree** (the children of a node are its calls, left to right in the order they are made):

```text
main
`-- binCoeff(5,3)
    |-- binCoeff(4,2)
    |   |-- binCoeff(3,1)
    |   |   |-- binCoeff(2,0)            base case -> 1
    |   |   `-- binCoeff(2,1)
    |   |       |-- binCoeff(1,0)        base case -> 1
    |   |       `-- binCoeff(1,1)        base case -> 1
    |   `-- binCoeff(3,2)
    |       |-- binCoeff(2,1)
    |       |   |-- binCoeff(1,0)        -> 1
    |       |   `-- binCoeff(1,1)        -> 1
    |       `-- binCoeff(2,2)            -> 1
    `-- binCoeff(4,3)
        |-- binCoeff(3,2)
        |   |-- binCoeff(2,1)
        |   |   |-- binCoeff(1,0)        -> 1
        |   |   `-- binCoeff(1,1)        -> 1
        |   `-- binCoeff(2,2)            -> 1
        `-- binCoeff(3,3)                -> 1
```

There are 19 calls of `binCoeff` (10 leaves, each returning 1, so the program prints **10**).

**(ii) Maximum number of activation records on the stack.** At any moment the stack holds exactly the activations on the path from the root to the node currently executing. So the maximum is the **height of the tree**. The longest root-to-leaf path is

$$\text{main} \to (5,3) \to (4,2) \to (3,1) \to (2,1) \to (1,0)$$

(or any other path ending in a `binCoeff(1, ·)` node). The maximum is therefore **6 activation records**: 5 for `binCoeff` plus 1 for `main`. Each recursive call reduces `n` by 1, and a base case is reached at the latest when `n` becomes $r$ or 0, so the depth is at most 5 calls.

**(iii) Control stack when a base case is satisfied for the first time.** Following the leftmost path, the first base case is `binCoeff(2,0)` ($r = 0$):

```text
   +------------------+
   | binCoeff  n=2 r=0 |  <- top: base case, about to return 1
   +------------------+
   | binCoeff  n=3 r=1 |
   +------------------+
   | binCoeff  n=4 r=2 |
   +------------------+
   | binCoeff  n=5 r=3 |
   +------------------+
   | main             |
   +------------------+   (bottom)
```

When it returns, its record is popped and `binCoeff(3,1)` calls `binCoeff(2,1)`, which is pushed in the same place.
