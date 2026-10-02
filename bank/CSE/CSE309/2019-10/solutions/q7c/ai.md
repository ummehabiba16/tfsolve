---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "The two problems are memory leaks (failing to free storage that can no longer be referenced, so the program uses more and more memory until it runs out) and dangling-pointer dereferences (freeing storage while a pointer to it is still used; the storage may be reused for other data, so reads and writes through the old pointer give wrong results or corrupt memory)."
sources: ["KMS Chapter 7 slide 44 (Manual Memory Management)", "Dragon book 2e sec. 7.4.5"]
---
With manual deallocation (`free` in C, `delete` in C++), the programmer must free each object exactly once, at the right time. The two common mistakes are:

**1. Memory leaks: failing to delete data that can no longer be referenced.**

```c
p = malloc(100);
p = malloc(200);   /* the first block can never be freed now */
```

The unreachable block stays allocated. A long-running program (server, OS component) gradually uses more and more memory, slows down because of paging, and may eventually run out of memory. Leaks are hard to find, because nothing fails immediately.

**2. Dangling-pointer dereferencing: referencing deleted data.**

```c
p = malloc(sizeof(struct node));
q = p;
free(p);
q->value = 5;      /* q is a dangling pointer */
```

After `free(p)`, the storage may be reallocated to another object. Reading through `q` gives garbage, and writing through it silently **corrupts** the other object or the allocator's own data structures. The error often shows up much later and far from the cause, which makes it very hard to debug. (Freeing the same object twice is a related error.)

Both problems are avoided by automatic **garbage collection**, which frees an object only when it is unreachable.
