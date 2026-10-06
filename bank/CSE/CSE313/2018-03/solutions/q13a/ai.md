---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Memory-mapped I/O puts device registers in the memory address space (no special instructions, easy protection, but caching and bus-filtering problems); port-mapped I/O uses a separate I/O space with IN/OUT (no address-space use, but special instructions)."
sources: ["Tanenbaum MOS 4e, sec. 5.1.3 (memory-mapped I/O)"]
---
**Memory-mapped I/O:** the control registers (and data buffers) of devices are mapped into the **ordinary address space**, so they are accessed with normal `LOAD`/`STORE` instructions.

**Port-mapped I/O (isolated I/O):** devices have a **separate I/O address space** ("ports") accessed only with special instructions (`IN`, `OUT`).

| | Advantages | Disadvantages |
|:--|:--|:--|
| **Memory-mapped** | no special instructions: a driver can be written fully in C; protection by simply not mapping the device pages into user space; any memory-reference instruction can use the registers directly (e.g. `TEST` a status bit) | **caching** of device registers must be disabled; the memory bus must be shared/filtered so devices can see their addresses (hard with a separate memory bus); uses up address space |
| **Port-mapped** | does not use any of the memory address space; the I/O instructions make device accesses easy to recognise | needs special instructions (assembly in C drivers); protection needs extra mechanisms (I/O permission bitmaps); the registers cannot be used by normal instructions: must be copied to the CPU first |
