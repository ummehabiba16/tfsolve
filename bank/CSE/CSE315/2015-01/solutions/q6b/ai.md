---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8 bytes: bytes 0-1 limit (16 bits, max 64 KB), bytes 2-4 base (24 bits, 16 MB), byte 5 access rights (P, DPL, S, E, ED/C, W/R, A), bytes 6-7 reserved (0). Example 0000 92 10 0000 FFFF = present DPL 0 writable data segment at 100000H, 64 KB."
sources: ["MHE 80286 slides (descriptor format, access right byte bits)", "Brey, The Intel Microprocessors, Sec. 2-3"]
---
A segment descriptor is an **8-byte** entry in the GDT or LDT that describes one segment.

```text
 byte   7    6      5              4             3    2         1    0
      +---------+---------------+-------------+-------------+-------------+
      | reserved| access rights | base 23-16  | base 15-0   | limit 15-0  |
      |  (0)    | P DPL S E ... |             |             |             |
      +---------+---------------+-------------+-------------+-------------+
```

- **Limit (bytes 0-1):** 16 bits, highest valid offset: segments of 1 byte to **64 KB**.
- **Base (bytes 2-4):** 24 bits, starting physical address anywhere in the **16 MB** space (no paragraph restriction).
- **Access rights (byte 5):**

| Bit | Name | Meaning |
|:-:|:--|:--|
| 7 | P | present: 1 = segment in memory, 0 = not present (exception 11) |
| 6-5 | DPL | descriptor privilege level 0-3 |
| 4 | S | 1 = code/data segment, 0 = system descriptor (LDT, TSS, gate) |
| 3 | E | 0 = data/stack, 1 = code (executable) |
| 2 | ED / C | data: 0 expand up, 1 expand down (stack); code: conforming |
| 1 | W / R | data: writable; code: readable |
| 0 | A | accessed (set by the CPU when the segment is used) |

- **Bytes 6-7:** reserved, must be 0 (used by the 80386 for the upper base and limit bits, G and D).

*Example:* 0000 92 10 0000 FFFF: limit FFFFH, base 100000H, access 92H = 1 00 1 0 0 1 0: present, DPL 0, data segment, expand up, writable: a 64 KB read/write data segment starting at 100000H.
