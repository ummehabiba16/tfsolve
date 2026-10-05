---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Segmentation: the selector (index, TI, RPL) picks a descriptor in the GDT or LDT (cached in the hidden part of the segment register); after privilege and limit checks, linear = descriptor base + offset. Paging (if PG = 1): the linear address splits 10 + 10 + 12; CR3 + 4 x dir gives the PDE (page table base), + 4 x table gives the PTE (page frame), physical = frame + offset; the TLB caches recent translations."
sources: ["MHE 80386-updated slides 16-26 (protected mode access: segmentation then paging, worked example)", "Brey, The Intel Microprocessors, Sec. 2-3, 2-4 (descriptors, paging)"]
---
A **logical address** is selector:offset (e.g. CS:EIP). It is translated in two stages.

**1. Segmentation: logical $\to$ linear**

```text
 selector (16 bits)              offset (32 bits)
 +-------------+--+---+                 |
 |  index (13) |TI|RPL|                 |
 +------+------+--+---+                 |
        | TI = 0: GDT (base in GDTR)    |
        | TI = 1: LDT (base in LDTR)    |
        v                               |
  descriptor at table base + 8 x index  |
  +-------+-------+-------+             |
  | base  | limit | access|             |
  +---+---+---+---+---+---+             |
      |       |       +--> privilege checks (CPL, RPL, DPL), type, present
      |       +----------> offset <= limit ? (else #GP)
      v                                 v
     base  ------------------------->  (+)  -->  32-bit LINEAR address
```

1. The selector's **index** (13 bits) chooses one of 8192 descriptors; **TI** chooses GDT or LDT; **RPL** is the requested privilege.
2. When the segment register is loaded, the descriptor (base, limit, access rights) is copied into its **hidden descriptor cache**, so later accesses do not read the table again.
3. The processor checks privilege (max(CPL, RPL) $\le$ DPL for data), the segment type and present bit, and **offset $\le$ limit** (limit in bytes, or in 4 KB units if G = 1).
4. **Linear address = base + offset.** If paging is off (PG = 0), this is the physical address.

**2. Paging: linear $\to$ physical** (when PG = 1 in CR0)

```text
 linear address:  | dir (10) | table (10) | offset (12) |
                       |          |              |
 CR3 (PDBR) --> page directory    |              |
                [CR3 + 4 x dir] = PDE           |
                    | page-table base (20 bits)  |
                    v                            |
                page table                       |
                [base + 4 x table] = PTE         |
                    | page-frame base (20 bits)  |
                    v                            v
                page frame (4 KB) -----------> (+) --> PHYSICAL address
```

1. Bits 31-22 index one of 1024 **page directory entries**; the directory's physical base is in **CR3**.
2. The PDE gives the physical base of a **page table**; bits 21-12 index one of its 1024 entries.
3. The PTE gives the physical base of the 4 KB **page frame**; bits 11-0 are the offset inside it.
4. **Physical address = frame base + offset.** Present, R/W and U/S bits are checked at both levels; a failure causes a **page fault** (#14) with the linear address in CR2.
5. The **TLB** keeps the 32 most recent page translations, so usually the two table reads are skipped.

*Example (slides):* CS = 0018H, EIP = 10A2BC23H, descriptor base 3823A216H gives linear 48C65E39H; split 0100100011 | 0001100101 | E39H, giving PDE 291 and PTE 101 and physical 30000E39H.
