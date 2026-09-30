---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**Page fault:** a hardware trap that occurs when a running process accesses a virtual page whose page-table entry has its present/valid bit cleared -- i.e., the page is not currently resident in physical memory (it may be on disk, in the swap area, or simply never allocated). The trap hands control to the OS's fault handler, which locates the page's data, picks/evicts a physical frame if none is free, brings the page in from disk, updates the page table (and TLB), and finally resumes the faulting instruction.

**Thrashing:** the condition where the combined working sets of the currently-running processes exceed the amount of available physical memory. As a result, pages are constantly evicted and then almost immediately re-referenced (faulted back in), so *every* process spends nearly all of its time waiting on page-fault-driven disk I/O rather than doing useful computation. The connection to page faults is direct: thrashing is precisely a state of an extremely high, sustained **page fault rate** -- the system is "busy" (disk light constantly on) but effective CPU utilization and throughput collapse, because almost every reference misses and triggers another expensive fault.
