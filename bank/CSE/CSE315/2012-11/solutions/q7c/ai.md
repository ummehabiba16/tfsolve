---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Paging maps each 4 KB linear page independently through its page-table entry, so the OS can fill consecutive PTEs with the addresses of whatever physical frames are free (scattered anywhere). The program then sees a contiguous linear range, e.g. a 16 KB buffer at linear 00400000H-00403FFFH, even though its frames are at 07000000H, 00123000H, 03456000H, 00050000H."
sources: ["MHE 80386-updated slides 21-23 (paging, 4 KB pages, page tables)", "Intel 80386 Programmer's Reference Manual, Sec. 5.2"]
---
**Idea.** Paging translates each 4 KB **linear page** separately: the page-table entry for linear page $k$ can hold the address of **any** physical frame. The operating system can therefore take free frames wherever they are in physical memory and put their addresses into **consecutive page-table entries**. The program sees one **contiguous linear block**, while the physical memory behind it is scattered.

**Example:** a program needs a 16 KB contiguous buffer at linear address 00400000H, but physical memory only has free 4 KB frames at 07000000H, 00123000H, 03456000H and 00050000H.

- 00400000H: directory index 1, table indices 0-3. The OS sets PDE 1 to point to a page table, and in that table:

| Linear page | PTE | Physical frame |
|:--|:-:|:--|
| 00400000H-00400FFFH | PTE 0 | 07000000H |
| 00401000H-00401FFFH | PTE 1 | 00123000H |
| 00402000H-00402FFFH | PTE 2 | 03456000H |
| 00403000H-00403FFFH | PTE 3 | 00050000H |

```text
 linear (contiguous)            physical (scattered)
 00400000 +------+  PTE0 ---->  07000000 +------+
 00401000 +------+  PTE1 ---->  00123000 +------+
 00402000 +------+  PTE2 ---->  03456000 +------+
 00403000 +------+  PTE3 ---->  00050000 +------+
```

- Linear address 00402010H = page 2 + offset 010H gives physical 03456010H. The program can use the buffer as one array, unaware of the gaps.

**Benefits:** large contiguous segments or arrays can be built without moving data (no external fragmentation), memory can be allocated page by page as it grows, and pages can even be on disk (not present) until used.
