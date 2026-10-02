---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "With A -> D deleted and roots X, Y: start Unscanned = {A, B}, Unreached = {C, D, E, F, G, H, I}. Scanning A moves E; B moves C; E moves H; C moves I; H and I add nothing. Scanned = {A, B, E, C, H, I}; the objects left in Unreached (D, F, G) are moved to Free, and Scanned becomes the new Unreached list. Time: proportional to the number of reachable objects (no sweep over the whole heap); space: the four lists are linked through the objects' headers, so O(1) extra per object and no extra stack."
sources: ["KMS Chapter 7 slides 71-73 (Optimizing Mark-and-Sweep, Baker's Mark-and-Sweep)", "Dragon book 2e sec. 7.6.2 (Algorithm 7.14)"]
---
**Assumptions.** The edges are read from the figure: X $\to$ A, Y $\to$ B, A $\to$ D (deleted), A $\to$ E, B $\to$ C, B $\to$ E, C $\to$ I, D $\to$ F, D $\to$ G, D $\to$ H, E $\to$ H, F $\to$ I, G $\to$ H, H $\to$ I, I $\to$ E. The heap holds the nine objects A-I. The *Unscanned* list is processed first-in first-out, adding objects in alphabetical order.

**Baker's algorithm** keeps every chunk on exactly one of four lists:

- *Free*: free chunks.
- *Unreached*: allocated chunks not yet found reachable (initially all allocated objects).
- *Unscanned*: reached, but their pointers are not yet examined.
- *Scanned*: reached, and their pointers examined.

Steps:

1. Move the objects referenced by the root set from *Unreached* to *Unscanned*.
2. While *Unscanned* is not empty: move an object $o$ to *Scanned*; for each object $o'$ referenced by $o$, if $o'$ is in *Unreached*, move it to *Unscanned*.
3. Finally *Free* = *Free* $\cup$ *Unreached*, and *Unreached* = *Scanned* (ready for the next collection).

**Trace (A $\to$ D deleted):**

| Step | Action | Unreached | Unscanned | Scanned |
|:-:|:--|:--|:--|:--|
| 0 | initially | A B C D E F G H I | | |
| 1 | roots: X $\to$ A, Y $\to$ B | C D E F G H I | A B | |
| 2 | scan A: E | C D F G H I | B E | A |
| 3 | scan B: C (E already reached) | D F G H I | E C | A B |
| 4 | scan E: H | D F G I | C H | A B E |
| 5 | scan C: I | D F G | H I | A B E C |
| 6 | scan H: I already reached | D F G | I | A B E C H |
| 7 | scan I: E already reached | D F G | (empty) | A B E C H I |

**Result:** D, F and G remain in *Unreached*, so they are garbage and are moved to *Free*. D lost its only incoming pointer; F and G were reachable only through D. A, B, C, E, H and I (*Scanned*) become the *Unreached* list for the next collection, with no reached-bits to reset.

**Complexity:**

- **Time:** proportional to the **number of reachable objects**. Each reached object is moved once and its pointers are examined once. Unlike basic mark-and-sweep, there is no sweep over the whole heap: the garbage is exactly the *Unreached* list, which is spliced onto *Free* in constant time (doubly linked lists).
- **Space:** the lists are threaded through the chunks themselves (e.g. two link pointers in each chunk header), so only $O(1)$ extra space per object is needed, and no recursion stack.
