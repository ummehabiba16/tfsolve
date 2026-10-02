---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "After deleting A -> C, the reachable objects are A, B, D, E, G, H, I (C and F are garbage). Before: A 0, B 50, C 100, D 150, E 200, F 250, G 300, H 350, I 400. Mark-and-compact slides the live objects down in address order: A 0, B 50, D 100, E 150, G 200, H 250, I 300; free space starts at 350."
sources: ["KMS Chapter 7 slides 79-84 (Relocating Garbage Collectors, Mark-and-Compact)", "Dragon book 2e sec. 7.6.3 (Fig. 7.25)"]
---
**Assumptions.** The edges are read from the figure: X $\to$ A, A $\to$ B, A $\to$ C, B $\to$ D, B $\to$ E, C $\to$ E, C $\to$ F, D $\to$ G, G $\to$ E, E $\to$ H, F $\to$ H, G $\to$ I, H $\to$ I. $X$ is the root set. The basic mark-and-compact collector of the text is used, which keeps the objects in their original order.

**1. Mark.** After deleting A $\to$ C, the objects reachable from X are A, B, D, E, G, H, I. **C** (pointed to only by A) and **F** (pointed to only by C) are unreachable.

**2. Compute new locations.** Scan the heap from address 0 and give each marked object the next free address (`free` starts at 0 and grows by 50):

| Object | Old address | Reachable? | New address |
|:-:|:-:|:-:|:-:|
| A | 0 | yes | **0** |
| B | 50 | yes | **50** |
| C | 100 | no | (freed) |
| D | 150 | yes | **100** |
| E | 200 | yes | **150** |
| F | 250 | no | (freed) |
| G | 300 | yes | **200** |
| H | 350 | yes | **250** |
| I | 400 | yes | **300** |

**3. Update references** in the root set and in the reachable objects: X $\to$ 0; A $\to$ B(50); B $\to$ D(100), E(150); D $\to$ G(200); G $\to$ E(150), I(300); E $\to$ H(250); H $\to$ I(300).

**4. Move** each object to its new address.

**Heap before:**

```text
0     50    100   150   200   250   300   350   400   450
| A   | B   | C   | D   | E   | F   | G   | H   | I   |
```

**Heap after:**

```text
0     50    100   150   200   250   300   350         450
| A   | B   | D   | E   | G   | H   | I   |   free    |
```

The seven live objects (350 bytes) are now contiguous at the low end, and the free space (from 350) is one block. The relative order of the objects is unchanged.
