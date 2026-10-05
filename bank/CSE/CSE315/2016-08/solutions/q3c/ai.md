---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "When PG = 1 the 80386 splits the 4 GB linear space into 1M pages of 4 KB. The linear address is split 10 + 10 + 12: CR3 holds the page directory (1024 entries), each PDE points to a page table (1024 entries), each PTE gives a 4 KB frame; physical = frame + offset. Entries hold the 20-bit frame address plus P, R/W, U/S, A, D, AVL bits; a 32-entry TLB caches translations; missing pages cause page faults (CR2)."
sources: ["MHE 80386-updated slides 21-26 (paging, page directory, page tables, CR3, TLB, worked example)", "Brey, The Intel Microprocessors, Sec. 2-4 (paging)"]
---
**Purpose.** Paging lets the operating system map the linear address space onto physical memory in fixed **4 KB pages**, so programs can be placed in scattered physical memory and pages can be swapped to disk (virtual memory) efficiently. It is enabled by **PG = 1 (bit 31 of CR0)** and works on the linear address produced by segmentation.

**Two-level translation**

```text
 linear: | directory (10) | table (10) | offset (12) |
                |               |              |
 CR3 --> page directory         |              |
         (1024 PDEs) --PDE--> page table       |
                              (1024 PTEs) --PTE--> 4 KB page frame
                                                        + offset = physical
```

- **CR3 (PDBR)** holds the physical address of the single **page directory** (4 KB, 1024 entries).
- The top 10 bits select a **page directory entry**, which gives the physical address of a **page table** (4 KB, 1024 entries).
- The next 10 bits select a **page table entry**, which gives the physical address of the **page frame**.
- The low 12 bits are the **offset** inside the 4 KB page.
- $1024 \times 1024$ pages $\times$ 4 KB = **4 GB**.

**Page directory / page table entry**

| Bits | 31-12 | 11-9 | 6 | 5 | 2 | 1 | 0 |
|:--|:--|:--|:-:|:-:|:-:|:-:|:-:|
| Field | frame / table address (20 bits) | AVL (for OS) | D (dirty) | A (accessed) | U/S | R/W | P |

- **P = 0**: page not in memory, so a **page fault (exception 14)**; the faulting linear address is put in **CR2**, and the OS loads the page and restarts the instruction.
- **R/W, U/S**: write and user/supervisor protection per page. **A, D**: used by the OS for replacement and write-back.

**TLB.** Reading two tables for every access would be slow, so the **translation look-aside buffer** keeps the 32 most recent page translations; most accesses hit in the TLB.

*Example (slides):* linear 48C65E39H gives directory 291, table 101, offset E39H; with CR3 = 1000H, PDE = 20000001H and PTE = 30000001H, the physical address is 30000E39H.
