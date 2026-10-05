---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Real mode (after reset): the Pentium works like a fast 8086 with 32-bit registers available: 1 MB, segment x 16 + offset, interrupt vector table at 0, no protection or paging. Protected mode (PE = 1 in CR0): selectors and descriptors (GDT/LDT/IDT) give 32-bit base and up to 4 GB segments, four privilege levels, task switching, optional paging (4 KB/4 MB pages) and virtual-8086 tasks; 4 GB physical, 64 TB virtual."
sources: ["Brey, The Intel Microprocessors, Ch. 18 (Pentium real and protected modes)", "MHE 80386-updated slides 14-16 (modes of operation)"]
---
**Real mode**

- The mode after **reset** (PE = 0 in CR0); used by DOS and to boot the system.
- The Pentium behaves like a **very fast 8086**: physical address = segment $\times$ 10H + offset, so only the **first 1 MB** is addressable (plus the 64 KB high-memory area).
- The 32-bit registers (EAX ...) and new instructions can be used, but offsets are limited to 64 KB.
- Interrupts use the **interrupt vector table** at 00000H (4 bytes per vector).
- **No protection, no paging, no multitasking support.**

**Protected mode**

- Entered by setting **PE = 1** in CR0 (after building the GDT and IDT).
- Segment registers hold **selectors** that index **descriptors** in the GDT/LDT: 32-bit base, 20-bit limit with granularity (segments up to **4 GB**), access rights. Linear address = base + offset.
- **Protection:** limit and type checks, **four privilege levels**, call gates, I/O privilege (IOPL and the I/O permission bitmap).
- **Multitasking:** TSS and hardware task switching.
- **Paging** (PG = 1): linear to physical translation with 4 KB or 4 MB pages and TLBs, virtual memory.
- **Interrupts** through the **IDT** (interrupt, trap and task gates).
- **Virtual-8086 mode** to run real-mode programs as protected tasks.
- 4 GB physical address space (64 GB with PAE on later models), 64 TB virtual.
