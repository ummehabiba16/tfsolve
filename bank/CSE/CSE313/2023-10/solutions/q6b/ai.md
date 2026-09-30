---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
The `malloc`/`free` pair is the classic user-level heap allocation API (OSTEP, "Memory API" chapter).

**How it works.** The heap is a single contiguous chunk of memory the OS gives the process (extendable via the `brk`/`sbrk` system call, or `mmap` for large allocations). The allocator library manages this space itself; the OS is not involved in each `malloc()`/`free()` call. A simple implementation keeps a *free list*: a linked list of currently-unused chunks of heap memory.

- `malloc(size)` searches the free list for a chunk big enough to satisfy the request (first-fit / best-fit / etc.), splits it if it is larger than needed, marks the remainder still free, and returns a pointer to the usable region *just past* a small **header**.

- `free(ptr)` is called with only a pointer -- it does not know the size. It steps backward from `ptr` to find the header, reads the size stored there, and adds that chunk back onto the free list (coalescing with adjacent free chunks if possible, to fight external fragmentation).

**Bookkeeping structures required.**

- **Header**: a small structure placed immediately before the returned pointer in every allocated chunk, typically containing `size` (size of the chunk, so `free()` knows how much to reclaim) and sometimes a `magic` number (to catch corruption / invalid frees).

- **Free list**: a linked list (pointers embedded inside the free chunks themselves, since that space is otherwise unused) threading together all currently free regions of the heap, used by `malloc()` to find space and by `free()` to give space back.

**Example.** If a program calls `malloc(20)`, the allocator might carve a $20+\text{header size}$ byte chunk out of a free region, write `size=20` into the header, and return `(header address)+headersize` to the caller. When the program later calls `free(ptr)`, the library computes `header = ptr - headersize`, reads `header->size`, and re-inserts that whole chunk (header + 20 bytes) onto the free list, merging it with a physically adjacent free chunk if one exists.
