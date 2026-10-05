---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The 80286 descriptor has a 24-bit base, 16-bit limit (max 64 KB) and bytes 6-7 reserved (zero). The 80386 uses those bytes: base extended to 32 bits (byte 7), limit to 20 bits, and new G (granularity: byte or 4 KB units, segments up to 4 GB), D (16/32-bit default size) and AV bits. The access rights byte is the same, so 286 descriptors still work on the 386."
sources: ["MHE 80386-updated slides 17-20", "MHE 80286 slides (80286 descriptor)"]
---
| Feature | 80286 descriptor | 80386 descriptor |
|:--|:--|:--|
| Base address | 24 bits (16 MB) | **32 bits** (4 GB): byte 7 adds base 31-24 |
| Limit | 16 bits: segment up to **64 KB** | **20 bits** + **G** bit: up to 1 MB in bytes, or up to **4 GB** in 4 KB units |
| Bytes 6-7 | reserved, must be 0 | byte 6: G, D, 0, AV, limit 19-16; byte 7: base 31-24 |
| Default operand size | always 16-bit | **D bit**: 16-bit or 32-bit segment |
| OS-available bit | none | **AV** |
| Access rights byte | P, DPL, S, E, ED/C, W/R, A | same |

Because the 80286 requires bytes 6-7 to be zero, an 80286 descriptor read by an 80386 means G = 0, D = 0 and base 31-24 = 0, i.e. exactly the same 16-bit segment, so **80286 software runs unchanged** on the 80386.
