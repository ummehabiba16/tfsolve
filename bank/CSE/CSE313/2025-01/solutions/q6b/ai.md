---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Yes, in principle two different *processes* could produce entries with the same Virtual Page Number (VPN) in the TLB, since every process's virtual address space starts numbering pages from 0 -- so VPN 3 of process A and VPN 3 of process B are completely different pages, but they look identical to a plain VPN-indexed TLB. Without any extra information this is ambiguous and unsafe (process B could accidentally get process A's translation).

**Resolution (OSTEP, "Paging: Faster Translations (TLBs)"):** tag every TLB entry with an **Address Space Identifier (ASID)** (essentially a shortened process/PID field) in addition to the VPN. A TLB lookup then matches on *(VPN, ASID)* together, so entries belonging to different processes but sharing the same VPN can coexist safely in the TLB without being confused for one another, and the TLB need not be flushed on every context switch (only entries with a matching ASID are considered a \"hit\"). If the hardware provides no ASID field, the only alternative is to flush the entire TLB on every context switch, which is correct but far more expensive (every process starts back at 100% TLB misses).
