---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Physical addresses are used directly (not translated) for: (1) the page directory base in CR3/PDBR, (2) the page table base addresses in page directory entries, (3) the page frame addresses in page table entries (when the processor reads PDEs/PTEs during translation)."
sources: ["MHE 80386-updated slides 22-26 (CR3, page directory and page table entries)", "Intel 80386 Programmer's Reference Manual, Ch. 5.2 (page translation)"]
---
With paging on, almost every address is linear and is translated. The exceptions are the addresses used by the **translation itself**, which must be physical (otherwise translating them would need another translation):

1. **CR3 (PDBR):** holds the **physical** base address of the page directory. The processor reads the page directory entry at CR3 + 4 $\times$ (directory index) directly in physical memory.
2. **Page directory entries:** the upper 20 bits are the **physical** base address of a page table. The processor reads the page table entry at that physical address + 4 $\times$ (table index).
3. **Page table entries:** the upper 20 bits are the **physical** base address of the page frame; the final operand address is this frame + offset.

(The processor also writes the Accessed and Dirty bits back into these entries at their physical addresses. Descriptor tables via GDTR/IDTR/LDTR and the TSS are *linear* addresses and are paged.)
