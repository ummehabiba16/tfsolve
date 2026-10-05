---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Physical: 24-bit address bus, 2^24 = 16 MB. Virtual: 1 GB per task: a selector's 13-bit index + TI bit picks one of 16K descriptors (8K GDT + 8K LDT), each segment up to 64 KB: 2^14 x 2^16 = 2^30 bytes. Addressing: selector -> descriptor (24-bit base, 16-bit limit) -> base + offset = physical; segments not present (P = 0) are swapped in from disk."
sources: ["MHE 80286 slides (protected mode, selectors, descriptors, virtual memory)", "Brey, The Intel Microprocessors, Sec. 2-3 and 17-1"]
---
**Physical memory: 16 MB.** The 80286 has a **24-bit address bus**: $2^{24}$ bytes = **16 MB**. (In real mode it uses only 20 bits: 1 MB.)

**Virtual memory: 1 GB per task.** In protected mode a selector has a 13-bit index plus the TI bit, so a task can use $2 \times 8192 = 2^{14}$ segment descriptors (8K global + 8K local), and each segment can be up to 64 KB ($2^{16}$ bytes):

$$2^{14} \times 2^{16} = 2^{30}\ \text{bytes} = \mathbf{1\ GB}$$

**How it addresses them**

1. A segment register holds a **selector**; the processor reads the selected **descriptor** from the GDT or LDT (cached in the hidden part of the register).
2. The descriptor gives a **24-bit base** and a **16-bit limit**: physical address = base + offset (offset $\le$ limit), anywhere in the 16 MB.
3. Since the virtual space (1 GB) is larger than physical memory (16 MB), only some segments are in memory. A descriptor with **P = 0** means the segment is on disk; using it causes a "segment not present" exception, and the operating system loads it into memory (swapping out another), updates the descriptor and restarts the instruction.
