---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Reference counting cannot reclaim cyclic structures: objects that point to each other keep each other's count above zero even when no program variable can reach them, so cyclic garbage is never freed (it also costs an update on every pointer assignment)."
sources: ["KMS Chapter 7 slides 45-93 (garbage collection, reference counting)", "Dragon book 2e sec. 7.5.3"]
---
**Reference counting.** Every object has a count of the references to it; assignments and parameter passing increment and decrement the counts, and when a count falls to 0 the object is freed (and the counts of the objects it points to are decremented) (Dragon book sec. 7.5.3). Garbage is found incrementally, as soon as it appears, and without pausing the program.

**Major problem: it cannot collect cyclic garbage.** If objects reference each other in a cycle, each one's count stays at least 1 because of the others, even when the whole cycle is unreachable from the program.

**Example.**

```c
struct Node { struct Node *next; };
struct Node *a = new_node();   /* a's object: count 1 */
struct Node *b = new_node();   /* b's object: count 1 */
a->next = b;                   /* b's object: count 2 */
b->next = a;                   /* a's object: count 2 */
a = NULL;                      /* a's object: count 2 -> 1 (still referenced by b->next) */
b = NULL;                      /* b's object: count 2 -> 1 (still referenced by a->next) */
```

Now no program variable can reach either object (they are garbage), but both counts are 1, never 0, so neither is freed: a **memory leak**. Circular lists, doubly linked lists, trees with parent pointers and graphs all create cycles.

**Other drawbacks.** (1) Every pointer assignment needs extra work to update counts (high overhead, and extra care with threads); (2) a count field is needed in every object; (3) a long chain of frees can cause an unpredictable pause. Remedies: use a **tracing collector** (mark-and-sweep) for the cycles, or *weak references* to break cycles.
