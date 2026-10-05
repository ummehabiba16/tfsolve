---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Logical (selector:offset) -> segmentation: selector index/TI picks a descriptor in the GDT/LDT (cached), privilege and limit checks, linear = base + offset. Linear -> paging: with 4 KB pages split 10 + 10 + 12: CR3 + 4 x dir gives the PDE (page table base), + 4 x table gives the PTE (frame), physical = frame + offset; if PSE = 1 and the PDE has PS = 1, a 4 MB page: physical = PDE frame + 22-bit offset. TLBs cache translations; faults give exceptions 13/14 (CR2)."
sources: ["MHE 80386-updated slides 16-26 (protected-mode address translation, worked example)", "Brey, The Intel Microprocessors, Ch. 18 (Pentium paging, 4 MB pages)"]
---
**Stage 1: segmentation (logical $\to$ linear)**

```text
 logical address = selector : offset(32)
 selector = | index (13) | TI | RPL |
               |
               v  TI = 0: GDT (GDTR base)   TI = 1: LDT (LDTR)
     descriptor at table base + 8 x index
     (cached in the hidden part of the segment register)
               |
     checks: present, type, privilege max(CPL, RPL) <= DPL, offset <= limit
               v
     LINEAR address = descriptor base (32) + offset (32)
```

1. The selector's index and TI choose a descriptor in the GDT or LDT; its base, limit and access rights are loaded into the segment register's descriptor cache when the selector is loaded.
2. The processor checks the access (present, type, privilege, offset $\le$ limit; violation: exception 13 or 12).
3. **Linear address = base + offset.**

**Stage 2: paging (linear $\to$ physical), PG = 1**

```text
 4 KB page:  | dir (10) | table (10) | offset (12) |
   CR3 + 4 x dir --> PDE --> page table base
   table base + 4 x table --> PTE --> 4 KB frame
   PHYSICAL = frame + offset(12)

 4 MB page (PSE = 1 in CR4, PS = 1 in PDE):  | dir (10) | offset (22) |
   CR3 + 4 x dir --> PDE --> 4 MB frame
   PHYSICAL = frame + offset(22)
```

1. The **TLB** is checked first (separate code and data TLBs for 4 KB and 4 MB pages). On a hit the frame address is taken directly.
2. On a miss, the PDE is read at CR3 + 4 $\times$ (bits 31-22). For a 4 KB page it gives a page table base, and the PTE at base + 4 $\times$ (bits 21-12) gives the page frame; for a 4 MB page the PDE gives the frame directly.
3. Present, R/W and U/S bits are checked; on a failure a **page fault (exception 14)** is raised with the linear address in **CR2**.
4. **Physical address = frame + offset**, driven onto the address bus.

*Example (80386 slides):* CS = 0018H, EIP = 10A2BC23H: GDT descriptor 3 gives base 3823A216H, so the linear address is 48C65E39H; directory 291, table 101, offset E39H; with the PTE giving frame 30000000H, the physical address is 30000E39H.
