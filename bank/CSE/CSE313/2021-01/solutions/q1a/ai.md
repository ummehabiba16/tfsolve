---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "No with 4096-byte pages (8+5+4 = 17 pages > 16); yes with 512-byte pages (64+33+31 = 128 pages = 128)."
sources: ["Tanenbaum MOS 4e, ch. 3, problem on page size and address-space fit"]
---
Each page holds only text, data or stack, so each segment is rounded **up** to a whole number of pages.

**Page size 4096 bytes.** The address space has $65{,}536/4096 = 16$ pages.

| Segment | Size (bytes) | Pages |
|:--|:-:|:-:|
| Text | 32,768 | $32768/4096 = 8$ |
| Data | 16,386 | $\lceil 16386/4096\rceil = 5$ (4 full pages + 2 bytes) |
| Stack | 15,870 | $\lceil 15870/4096\rceil = 4$ |
| **Total** | | **17** |

$17>16$, so the program **does not fit**.

**Page size 512 bytes.** The address space has $65{,}536/512 = 128$ pages.

| Segment | Size (bytes) | Pages |
|:--|:-:|:-:|
| Text | 32,768 | $64$ |
| Data | 16,386 | $\lceil 16386/512\rceil = 33$ |
| Stack | 15,870 | $\lceil 15870/512\rceil = 31$ |
| **Total** | | **128** |

$128\le128$, so the program **fits** (exactly).
