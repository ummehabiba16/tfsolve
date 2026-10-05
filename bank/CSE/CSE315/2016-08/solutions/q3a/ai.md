---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "An 80286 descriptor is 8 bytes: bytes 0-1 limit (16 bits, up to 64 KB), bytes 2-4 base (24 bits, anywhere in 16 MB), byte 5 access rights (P, DPL, S, E, ED/C, W/R, A), bytes 6-7 reserved (0, used by the 80386). It is selected by a selector (index, TI, RPL) from the GDT or LDT and cached in the segment register's hidden part."
sources: ["MHE 80286 slides (descriptor: base, limit, access rights byte P, DPL, S, E, ED, C, W, R, A)", "Brey, The Intel Microprocessors, Sec. 2-3 (80286 descriptor format)"]
---
In protected mode a segment register holds a **selector**, which points to an 8-byte **segment descriptor** in the GDT or LDT. The descriptor describes the segment's **location, length and access rights**.

**Format**

```text
 byte   7      6    |    5          |    4        |  3     2  |  1     0
      +-------------+---------------+-------------+-----------+-----------+
      | reserved    | access rights | base 23-16  | base 15-0 | limit 15-0|
      | (0000)      |               |             |           |           |
      +-------------+---------------+-------------+-----------+-----------+
```

- **Limit (bytes 0-1, 16 bits):** last valid offset; segments are 1 byte to 64 KB.
- **Base (bytes 2-4, 24 bits):** starting physical address anywhere in the 16 MB space; the paragraph restriction of real mode is gone.
- **Reserved (bytes 6-7):** must be 0 (the 80386 uses them for base 31-24, limit 19-16, G and D bits).

**Access rights byte (byte 5)**

| Bit | 7 | 6-5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Field | P | DPL | S | E | ED / C | W / R | A |

- **P (present):** 1 = segment is in memory; 0 = not present (exception 11, used for virtual memory).
- **DPL:** descriptor privilege level 0-3.
- **S:** 1 = code/data segment, 0 = system descriptor (LDT, TSS, gates).
- **E (executable):** 0 = data/stack segment, 1 = code segment.
- **ED** (data): 0 = expands up, 1 = expands down (stack). **C** (code): conforming or not.
- **W** (data): writable or read-only. **R** (code): readable or execute-only.
- **A (accessed):** set by the processor when the segment is used.

*Example:* descriptor 0000 92 10 0000 FFFF describes a present, DPL 0, writable data segment at base 100000H with limit FFFFH (64 KB). (AR 92H = 1 00 1 0 0 1 0.)
