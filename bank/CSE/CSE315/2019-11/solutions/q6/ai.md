---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) 4 GB / 16 KB = 2^18 = 262144 pages. (ii) 14-bit offset; the other 18 bits split as 5 + 6 + 7 (each level twice the entries of the previous): bits 31-27 level 1, 26-21 level 2, 20-14 level 3, 13-0 offset. (iii) Level 1: 32 entries, level 2: 64, level 3: 128."
sources: ["MHE 80386-updated slides 21-26 (paging: page directory, page tables, splitting the linear address 10+10+12)"]
---
**(i) Total number of pages**

$$\text{Pages} = \frac{4\ \text{GB}}{16\ \text{KB}} = \frac{2^{32}}{2^{14}} = 2^{18} = \mathbf{262144}$$

**(ii) Splitting the 32-bit linear address**

- Page size 16 KB = $2^{14}$ bytes, so the **offset** needs **14 bits**.
- The remaining $32 - 14 = 18$ bits select the page through 3 levels. If level 1 uses $x$ bits ($2^x$ entries), "twice the entries of the previous level" means level 2 uses $x+1$ bits and level 3 uses $x+2$ bits:

$$x + (x+1) + (x+2) = 18 \ \Rightarrow\ x = 5$$

```text
 31        27 26          21 20            14 13                      0
+------------+--------------+----------------+-------------------------+
|  Level 1   |   Level 2    |    Level 3     |         Offset          |
|  5 bits    |   6 bits     |    7 bits      |         14 bits         |
+------------+--------------+----------------+-------------------------+
  index into   index into     index into       byte within the
  level-1      level-2        level-3          16 KB page
  table        table          table (-> page frame)
```

**(iii) Entries per table**

| Level | Bits | Entries |
|:-:|:-:|:-:|
| 1 | 5 | $2^5$ = **32** |
| 2 | 6 | $2^6$ = **64** |
| 3 | 7 | $2^7$ = **128** |

Check: $32 \times 64 \times 128 = 262144 = 2^{18}$ pages, and $2^{18} \times 16\ \text{KB} = 4$ GB.
