---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8 bytes: limit 15-0 (bytes 0-1), base 23-0 (bytes 2-4), access rights (byte 5: P, DPL, S, type E/ED-C/W-R/A), byte 6: G, D, 0, AV and limit 19-16, byte 7: base 31-24. 32-bit base (4 GB), 20-bit limit in bytes (G = 0, 1 MB) or 4 KB pages (G = 1, 4 GB), D = default 16/32-bit operands."
sources: ["MHE 80386-updated slides 17-20 (descriptor, G, AV, D bits and examples)", "MHE 80286 slides (access rights byte)", "Brey, The Intel Microprocessors, Sec. 2-3 (80386 descriptor)"]
---
An 80386 segment descriptor is **8 bytes** and describes a segment's base, size and access rights.

```text
 byte 7          byte 6                  byte 5           bytes 4-2       bytes 1-0
+-----------+---+---+---+----+---------+---------------+---------------+-------------+
| base 31-24| G | D | 0 | AV | lim19-16| access rights | base 23-0     | limit 15-0  |
+-----------+---+---+---+----+---------+---------------+---------------+-------------+
```

**Fields**

- **Base (32 bits: bytes 2, 3, 4 and 7):** starting address of the segment anywhere in the 4 GB space.
- **Limit (20 bits: bytes 0, 1 and the low nibble of byte 6):** size of the segment minus 1, in units set by G.
- **G (granularity):** 0 = limit in **bytes** (segments up to 1 MB); 1 = limit in **4 KB units** (up to 4 GB; limit = limit field $\times$ 4K + FFFh).
- **D (default size):** 0 = 16-bit segment (80286 code: 16-bit operands/addresses, SP); 1 = 32-bit segment (32-bit operands, ESP stack up to 4 GB).
- **0:** reserved (must be 0).
- **AV (available):** free for the operating system's use.
- **Access rights (byte 5):**

| Bit | 7 | 6-5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| | P (present) | DPL (privilege 0-3) | S (1 = code/data, 0 = system) | E (1 = code) | ED (data: expand down) / C (code: conforming) | W (data: writable) / R (code: readable) | A (accessed) |

*Example (slides):* descriptor 38D4 9A23 A216 320BH has base 3823A216H, access 9AH (present code segment, DPL 0, readable), G = 1, D = 1, limit 4320BH $\times$ 4K.
