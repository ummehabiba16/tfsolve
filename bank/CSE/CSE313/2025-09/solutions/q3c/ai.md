---
author: ai
via: chat
status: unverified
summary: A process switch changes the address space (registers + memory map + TLB/cache flush); a thread switch within a process keeps the address space and swaps only the registers/stack, so it is far cheaper.
sources: ['Process/Thread slides 17, 25, 41', 'Tanenbaum, MOS 4e, sec. 2.2.2']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Process context switch: save the running process's registers into its PCB, switch the memory map (page-table / base registers), which invalidates the TLB and often the cache, then load the new PCB. Expensive.

Thread context switch (same process): the two threads share one address space, so there is no memory-map change and no TLB flush, only the program counter, general registers and stack pointer are swapped. Cheaper and faster.
