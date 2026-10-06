---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Memory-mapped I/O: no special instructions and easy protection through the page tables, but caching must be disabled for device pages and all memory accesses must be checked against device addresses."
sources: ["Tanenbaum MOS 4e, sec. 5.1.3 (memory-mapped I/O)"]
---
In **memory-mapped I/O** the control registers of a device are mapped into the ordinary address space; they are read and written with normal `LOAD`/`STORE` instructions.

**Advantages**

- **No special I/O instructions** (`IN`/`OUT`), so a device driver can be written entirely in C; no assembly code is needed to read or write the control registers.
- **Protection is free:** to keep user processes away from a device, the OS simply does not map its registers into their virtual address space; they can even be given a single device by mapping only that page.
- **Every memory instruction can access device registers**, e.g. a `TEST` can examine a status bit directly, without first loading the register into the CPU.

**Disadvantages**

- **Caching must be disabled** for the pages holding device registers: a cached copy of a status register would never change. This needs extra hardware or OS support (a per-page cache-disable bit).
- With a **single address space**, all memory modules *and* all I/O devices must examine every memory reference to decide who responds. With a dedicated high-speed memory bus (as on modern PCs) this is hard, so extra hardware (a filter/bridge) is needed.
- The device registers consume part of the address space.
