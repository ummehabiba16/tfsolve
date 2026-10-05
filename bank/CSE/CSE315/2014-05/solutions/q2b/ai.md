---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "In protected mode a segment register holds a selector (13-bit index, TI, RPL) instead of a segment address. The index selects an 8-byte descriptor in the GDT (TI = 0, base in GDTR) or LDT (TI = 1, via LDTR); the descriptor gives a 24-bit base, 16-bit limit and access rights, cached in the register's hidden part. Physical address = base + offset (offset <= limit), anywhere in 16 MB; 8192 x 2 descriptors x 64 KB = 1 GB virtual per task."
sources: ["MHE 80286 slides (protected mode addressing, selector, descriptor, GDT/LDT, shadow registers)", "Brey, The Intel Microprocessors, Sec. 2-3 (protected-mode memory addressing)"]
---
In real mode a segment register holds the segment address itself (address = segment $\times$ 16 + offset). In **protected mode** it holds a **selector** that points to a **descriptor**, which describes the segment.

**Selector (16 bits)**

| Bits 15-3 | Bit 2 | Bits 1-0 |
|:--|:-:|:-:|
| Index (0-8191) | TI: 0 = GDT, 1 = LDT | RPL (requested privilege level) |

**Descriptor tables**

- **GDT** (global descriptor table): segments shared by all tasks; its base and limit are in **GDTR**.
- **LDT** (local descriptor table): segments of one task; selected by **LDTR**.
- Each table holds up to 8192 descriptors of 8 bytes.

**Descriptor (8 bytes):** 16-bit **limit**, 24-bit **base**, **access rights** byte (present, DPL, type: code/data, readable/writable, expand direction), 2 reserved bytes.

**Address translation**

```text
 DS = selector --> index x 8 + (GDTR or LDTR base) --> descriptor
                                                       base (24 bits)
                                                       limit, access rights
 physical address = descriptor base + offset   (offset <= limit, rights checked)
```

1. When a selector is loaded into a segment register, the processor reads the descriptor and stores base, limit and rights in the register's hidden **descriptor cache** (shadow register).
2. On each access: check offset $\le$ limit and the access rights; then **physical address = base + offset** (24 bits, up to 16 MB).

*Example:* DS = 0008H (index 1, GDT, RPL 0); GDT entry 1 has base 100000H and limit FFFFH; then DS:[0020H] is physical address 100020H.

**Virtual memory:** a task can use $2 \times 8192$ descriptors of up to 64 KB each, about **1 GB of virtual memory**; segments not present in memory (P = 0) cause an exception so the OS can load them.
