---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Temporal locality: recently accessed data is likely to be accessed again soon; spatial locality: data near a recently accessed location is likely to be accessed soon. A GC improves locality by compacting/copying live objects into a contiguous region (removing fragmentation) and placing objects that refer to each other close together. Root set: data the program can access directly without dereferencing, i.e. static/global variables, variables on the run-time stack (locals, parameters) and registers. LookupNewLocation(o): if NewLocation(o) = NULL { NewLocation(o) = free; free = free + sizeof(o); copy o to NewLocation(o); } return NewLocation(o)."
sources: ["KMS Chapter 7 slides 35-36 (Locality in Programs), 46-53 (Preliminaries, Reachability), 85-92 (Copying Garbage Collectors, Cheney)", "Dragon book 2e sec. 7.4.3, 7.5.2, 7.6.4 (Fig. 7.26)"]
---
**Locality of reference.**

- **Temporal locality:** memory locations a program accesses are likely to be accessed **again within a short period** (e.g. loop variables, the code of a loop).
- **Spatial locality:** memory locations **close to** a location just accessed are likely to be accessed soon (array elements in sequence, the fields of one object, consecutive instructions).

Caches and pages exploit both, so the layout of heap data matters.

**How a GC improves locality.**

- A **relocating** collector (mark-and-compact or copying) moves all reachable objects into one **contiguous** region, removing fragmentation. The live data then occupies fewer cache lines and pages (**spatial locality**), and free space is one block, so new objects are allocated next to each other.
- A copying collector copies objects in the order it reaches them (breadth-first in Cheney's algorithm, or depth-first). Objects that refer to each other, and are therefore likely to be used together, end up close together. Recently and frequently used objects are packed into a small working set, which helps the cache keep them (**temporal locality**).
- Generational collectors keep young, frequently accessed objects in a small nursery.

**Root set.** The data that the program can access **directly, without dereferencing any pointer**:

- static (global) variables;
- variables on the run-time stack: local variables and parameters of active procedures, and temporaries;
- machine registers holding pointers.

Every object reachable from the root set by following pointers is live; all others are garbage.

**Completing Cheney's copying collector.** `NewLocation(o)` is NULL while `o` has not been copied. `free` is the next free address in To space. `LookupNewLocation` copies an object the first time it is reached and returns its new address:

```text
LookupNewLocation(o) {
    if (NewLocation(o) == NULL) {        /* o not yet copied            */
        NewLocation(o) = free;           /* reserve space in To space   */
        free = free + sizeof(o);
        copy object o to NewLocation(o); /* its pointers still refer to */
    }                                    /* From space until scanned    */
    return NewLocation(o);
}
```

Each object is copied once (later calls return the recorded address). The region between `unscanned` and `free` acts as the queue of copied-but-unscanned objects. The main loop scans each copied object and redirects its references with this function. When `unscanned` reaches `free`, all reachable objects are in To space, and From space can be reused as a whole.
