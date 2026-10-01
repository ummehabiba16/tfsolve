---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) 2^32 / 2^14 = 2^18 = 262144 pages; (ii) 32-bit linear address = L1 5 bits (31-27) | L2 6 bits (26-21) | L3 7 bits (20-14) | offset 14 bits (13-0); (iii) 32, 64 and 128 entries."
sources: ["MHE 80386-updated slides 21-23 (paging: directory / page table / offset split)"]
---
**(i) Total number of pages**

$$\frac{4\text{ GB}}{16\text{ KB}} = \frac{2^{32}}{2^{14}} = 2^{18} = \mathbf{262{,}144\text{ pages}}$$

**(ii) Parsing the 32-bit linear address**

- Page size 16KB $=2^{14}$, so the **offset takes 14 bits**.
- That leaves $32-14 = 18$ bits for the 3 levels. Each level has twice as many entries as the previous one, i.e. one more index bit:

$$a + (a+1) + (a+2) = 18 \Rightarrow 3a = 15 \Rightarrow a = 5$$

So Level 1 has 5 bits, Level 2 has 6 bits and Level 3 has 7 bits.

```text
 31         27 26          21 20          14 13                 0
+-------------+--------------+--------------+--------------------+
|   Level 1   |   Level 2    |   Level 3    |       Offset       |
|   5 bits    |   6 bits     |   7 bits     |      14 bits       |
+-------------+--------------+--------------+--------------------+
```

**(iii) Entries per table**

| Level | Index bits | Entries |
|:--|:-:|:-:|
| Level 1 | 5 | $2^{5}$ = **32** |
| Level 2 | 6 | $2^{6}$ = **64** |
| Level 3 | 7 | $2^{7}$ = **128** |

Check: $32\times64\times128 = 2^{18}$ pages, and $2^{18}\times2^{14} = 2^{32}$ B = 4GB.
