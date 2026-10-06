---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Protection stops a process accessing others' memory; relocation lets a program run at any physical address; base and limit registers can ensure both (if only the OS can set them), at the cost of contiguous allocation."
sources: ["Tanenbaum MOS 4e, sec. 3.1.2-3.1.3 (address spaces, base and limit registers)"]
---
- **Protection:** a process must be prevented from reading or writing memory that belongs to the OS or to other processes.
- **Relocation:** a program must be able to be loaded at *any* physical address (not the one chosen at compile time); its addresses must be adjusted to where it is actually loaded.

**Can base and limit registers ensure both? Yes.**

- On each memory reference the hardware **adds the base register** to the program's address (**relocation**: the same program can run unchanged at any location, even be moved while running by changing the base) and **compares the offset with the limit register** (**protection**: an address beyond the limit, or below the base, causes a trap to the OS).
- The registers can be loaded only by **privileged instructions** in kernel mode, so a user process cannot enlarge its own window (this needs the dual-mode hardware).

**Limitations:** the process must occupy **one contiguous block** of physical memory (external fragmentation, no sharing between processes, and the process cannot exceed memory); the add and compare on every reference needs extra hardware. Paging/segmentation overcome these limits.
