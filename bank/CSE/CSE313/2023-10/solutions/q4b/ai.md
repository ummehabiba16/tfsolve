---
author: ai
via: chat
status: unverified
summary: 'Per-process (shared): Address Space, Global Variables, Child Processes, Directories. Per-thread (private): Program Counter, Registers, Stack, Local Variables.'
sources: ['Process/Thread slides 23, 41', 'Tanenbaum, MOS 4e, sec. 2.2.2 (Table 2-3)']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
(Definitions as usual: a process switch changes the address space and flushes TLB/cache; a thread switch keeps the address space and swaps only registers and stack.)

- **Per-process items (shared by all threads):** Address Space, Global Variables, Child Processes, Directories
- **Per-thread items (private to each thread):** Program Counter, Registers, Stack, Local Variables
