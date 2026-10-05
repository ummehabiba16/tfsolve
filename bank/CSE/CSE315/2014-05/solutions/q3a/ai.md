---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "80386 descriptor (8 bytes): 32-bit base (bytes 2-4, 7), 20-bit limit (bytes 0-1 and low nibble of byte 6), G (byte or 4 KB granularity), D (16/32-bit default), AV, and the access rights byte (P, DPL, S, E, ED/C, W/R, A). Versus 80286: 24-bit base and 16-bit limit (64 KB), bytes 6-7 reserved; the 386 uses those bytes for base 31-24, limit 19-16, G, D and AV, so segments can be 4 GB."
sources: ["MHE 80386-updated slides 17-20 (descriptor, G, AV, D bits)", "MHE 80286 slides (80286 descriptor)", "Brey, The Intel Microprocessors, Sec. 2-3"]
---
**80386 descriptors**

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

**Differences from 80286 descriptors**

| Feature | 80286 descriptor | 80386 descriptor |
|:--|:--|:--|
| Base address | 24 bits (16 MB) | **32 bits** (4 GB): byte 7 adds base 31-24 |
| Limit | 16 bits: segment up to **64 KB** | **20 bits** + **G** bit: up to 1 MB in bytes, or up to **4 GB** in 4 KB units |
| Bytes 6-7 | reserved, must be 0 | byte 6: G, D, 0, AV, limit 19-16; byte 7: base 31-24 |
| Default operand size | always 16-bit | **D bit**: 16-bit or 32-bit segment |
| OS-available bit | none | **AV** |
| Access rights byte | P, DPL, S, E, ED/C, W/R, A | same |

Because the 80286 requires bytes 6-7 to be zero, an 80286 descriptor read by an 80386 means G = 0, D = 0 and base 31-24 = 0, i.e. exactly the same 16-bit segment, so **80286 software runs unchanged** on the 80386.
