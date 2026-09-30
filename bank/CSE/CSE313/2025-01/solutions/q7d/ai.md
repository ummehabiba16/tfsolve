---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
No -- classic DMA controllers are generally **not aware of memory virtualization**. A DMA engine transfers data directly between a device and memory over the system bus without going through the CPU's MMU/TLB, so by default it only understands raw **physical** addresses; it has no notion of a process's virtual address space or page tables.

To use DMA correctly in a (paged / virtualized-memory) system, the OS must:

1.  **Translate** the user buffer's virtual address to its physical address before programming the DMA controller with the transfer's source/destination.

2.  **Pin (lock) the target pages** in physical memory for the duration of the transfer, so the page cannot be swapped out or moved mid-transfer -- since the DMA engine has no way to detect or cope with such a change happening "behind its back".

Modern systems often add an **IOMMU (I/O Memory Management Unit)**, which gives devices their own translation layer (device virtual $\to$ physical addresses), analogous to what the CPU's MMU does for regular memory accesses. This both simplifies buffer management (large virtually-contiguous DMA buffers need not be physically contiguous) and adds protection, preventing a misbehaving or compromised device from DMA-ing into arbitrary physical memory it shouldn't touch.
