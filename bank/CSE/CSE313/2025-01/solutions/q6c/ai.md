---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
- **Present/Valid bit**: tells the hardware (and OS) whether this PTE currently holds a valid virtual-to-physical translation, i.e., whether the page is actually resident in physical memory. If clear, any access causes a page fault, which traps into the OS to fetch the page (from disk/swap) or terminate the process on an illegal access.

- **Dirty (modified) bit**: set automatically by hardware the first time the page is *written*. The OS uses it when evicting a page: a clean (not dirty) page can simply be dropped/overwritten because an identical copy already exists on disk; a dirty page must first be written back to disk, which is more expensive -- so the bit lets the replacement algorithm prefer evicting clean pages.

- **Reference (accessed) bit**: set automatically by hardware whenever the page is accessed (read *or* written). The OS periodically clears it and uses its value to approximate how recently/frequently a page has been used, which is the basis of approximate-LRU replacement policies such as the Clock (second-chance) algorithm.
