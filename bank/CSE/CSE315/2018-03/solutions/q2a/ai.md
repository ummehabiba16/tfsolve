---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Build the page directory and page tables first (page-aligned), identity-map the code that enables paging (and the GDT/IDT/stack it uses), be in protected mode, load CR3 with the physical address of the page directory, then set PG (bit 31 of CR0) and immediately execute a JMP to flush the prefetch queue."
sources: ["MHE 80386-updated slides 21-23 (paging, CR3, PG bit in CR0)", "Intel 80386 Programmer's Reference Manual, Sec. 10.4 (software initialization for protected mode and paging)"]
---
Paging is switched on by setting **PG (bit 31 of CR0)**. From the very next instruction fetch, every linear address is translated through the page tables, so the following must be done first:

1. **Build the page directory and page tables in memory.** Each must start on a 4 KB boundary; entries need the Present bit and the proper R/W and U/S bits. Unused entries must be marked not present.
2. **Identity-map the code that enables paging.** The instruction after `MOV CR0, EAX` is fetched at the next linear address. If that page did not map to the same physical address (linear = physical), the processor would jump to the wrong place. The same applies to the GDT, IDT, TSS and the current stack, which are reached through linear addresses.
3. **Be in protected mode.** Paging works only with PE = 1 (set PE first, or PE and PG together).
4. **Load CR3 (PDBR)** with the **physical** address of the page directory. This also flushes the TLB.
5. **Set PG in CR0** (`MOV EAX, CR0 / OR EAX, 80000000h / MOV CR0, EAX`).
6. **Execute a JMP right after setting PG** to flush the prefetch queue, which still holds instructions fetched without paging.

```text
    MOV  EAX, PAGE_DIR_PHYS
    MOV  CR3, EAX          ; physical address of page directory
    MOV  EAX, CR0
    OR   EAX, 80000000H    ; PG = 1 (PE already 1)
    MOV  CR0, EAX
    JMP  NEXT              ; flush prefetch queue
NEXT:                      ; this code is identity-mapped
```
