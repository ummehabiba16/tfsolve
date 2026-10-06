---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Aging: every tick shift each counter right and insert R at the leftmost bit; the lowest counter is replaced."
sources: ["Tanenbaum MOS 4e, sec. 3.4.7 (aging)"]
---
```text
/* executed at every clock interrupt; counter[p] is an 8-bit (k-bit) value per page p */
for each page p in memory:
    counter[p] = counter[p] >> 1;            /* age: shift right by one bit            */
    if (R[p] == 1)
        counter[p] = counter[p] | 0x80;      /* put the R bit in the leftmost position */
    R[p] = 0;                                /* clear the reference bit                */

/* executed at a page fault */
victim = page p in memory with the smallest counter[p];   /* least recently/frequently used */
replace victim with the faulting page;
counter[new page] = 0;
```

The counter is a $k$-bit number whose most significant bit is the most recent tick, so a page referenced recently has a larger value than one referenced only long ago; the history older than $k$ ticks is forgotten.
