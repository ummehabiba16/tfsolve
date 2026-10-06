---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Total demand 260 bytes (and P3 alone 120 bytes) exceeds the 100 bytes of memory: use virtual memory with demand paging (or swapping/overlays), keeping only the needed pages of each process in memory."
sources: ["Tanenbaum MOS 4e, sec. 3.3 (virtual memory), 3.2 (swapping), overlays"]
---
The processes need $48+64+120+28=260$ bytes in total and P3 (120 bytes) is even **larger than the whole memory** (100 bytes), so they **cannot all be loaded at once**, and not even P3 can be loaded completely. The solution is **virtual memory with demand paging**:

1. Divide each process's address space into fixed-size **pages** (e.g. 4 bytes) and memory into **page frames** ($100/4=25$ frames).
2. Give each process a **page table** (with a present bit). At start no or only some pages are loaded.
3. When a process references a page that is not present, a **page fault** occurs; the OS loads the page from disk into a free frame (or, if none is free, evicts a page chosen by a replacement algorithm such as LRU/clock, writing it back first if modified).
4. Only the **working set** of each process (the pages it uses at the moment) needs to be in memory, so all four processes can be "in memory" together and run in (pseudo-)parallel, switching when one waits for a page.

Alternatives (older or cruder): **swapping** whole processes in and out (does not work for P3, which is larger than memory) or programmer-defined **overlays** (the program is split into parts which replace each other in memory).
