---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Memory-mapped I/O: ports share the memory address space and use memory instructions. Port-mapped (isolated) I/O: separate I/O address space, IN/OUT instructions, M/IO' signal. The 8086 uses isolated I/O (64K ports): it keeps the full 1 MB for memory and needs simpler decoding, but only IN/OUT through AL/AX can access ports."
sources: ["Brey, The Intel Microprocessors, Sec. 11-1 (isolated vs memory-mapped I/O)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 3 (8086 I/O, M/IO')", "Hall, Microprocessors and Interfacing, Ch. 7"]
---
**Memory-mapped I/O.** I/O ports are given addresses **inside the memory address space**. The CPU uses the same signals ($\overline{MRDC}$, $\overline{MWTC}$) and the same instructions (`MOV`, `ADD`, `AND`, ...) for ports as for memory. A port is just a "memory location" that is wired to a device.

**Port-mapped (isolated) I/O.** I/O ports have a **separate address space** from memory. Special instructions (`IN`, `OUT`) and separate control signals ($\overline{IORC}$, $\overline{IOWC}$, or M/$\overline{IO}$ = 0 on the 8086) tell external logic that the address is a port, not memory.

**Which one the 8086 uses.** The 8086 provides **isolated (port-mapped) I/O**: it has a separate 64K-byte I/O space (port addresses 0000H-FFFFH, using A15-A0), accessed by `IN`/`OUT`, and the M/$\overline{IO}$ pin distinguishes memory from I/O cycles. (Memory-mapped I/O is still possible by decoding ports into memory addresses.)

**Advantages of isolated I/O over memory-mapped I/O**

- The **whole 1 MB** memory space stays available for memory; no memory addresses are lost to ports.
- **Simpler, cheaper decoding**: only 8 or 16 address lines are decoded for a port instead of 20.
- I/O instructions are easy to spot in a program, and memory instructions cannot write a port by mistake.
- Short instructions for fixed ports (`IN AL, 40H` is 2 bytes).

**Disadvantages**

- Only `IN` and `OUT` can access ports, and data moves only through **AL/AX**. Data must be copied into a register before it can be tested or changed; with memory-mapped I/O any instruction (e.g. `AND [port], 0FH`, `TEST`) works directly on the port.
- Fewer addressing modes for ports (only an 8-bit immediate port number or DX).
- Extra control signals ($\overline{IORC}$, $\overline{IOWC}$ / M/$\overline{IO}$) are needed in the hardware.
