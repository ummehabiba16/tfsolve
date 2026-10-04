---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Print '*' if it is the first row (BL = BH), the first column (CL = BL) or the last column (CL = 1), else '.': CMP BL,BH / JE STAR / CMP CL,BL / JE STAR / CMP CL,1 / JNE SKIP (fall through to STAR)."
sources: ["MHE IF slides (8086 instructions, addressing)", "Brey, The Intel Microprocessors, Ch. 6 (CMP, conditional jumps, LOOP)"]
---
**Understanding the given code**

- BL = number of characters in the current row (it starts at the input $n$ and is decremented after each row). BH = $n$ (saved, never changed).
- For each row, CX = BL, and `LOOP PRINT_COL` prints BL characters. CX counts **down**: the first character of a row is printed with CX = BL and the last with CX = 1. Since CH = 0, CL = CX.

**The pattern** (input 6): row 1 is all stars; in every other row the **first** and **last** characters are `*` and the ones in between are `.`:

```text
******     <- first row (BL = BH): all '*'
*...*      <- first (CL = BL) and last (CL = 1) are '*'
*..*
*.*
**
*
```

**Code after PRINT_COL**

```text
PRINT_COL:
    CMP BL, BH      ; first row?
    JE  STAR        ;   yes -> '*'
    CMP CL, BL      ; first column of this row?
    JE  STAR        ;   yes -> '*'
    CMP CL, 1       ; last column of this row?
    JNE SKIP        ;   no  -> '.'
                    ; yes: fall through to STAR -> '*'
```

**Check (input 4):** row BL = 4 = BH: `****`; BL = 3: CL = 3 (first) `*`, CL = 2 `.`, CL = 1 (last) `*`, so `*.*`; BL = 2: `**`; BL = 1: `*`. This matches the expected output. The code was also checked by simulating it for inputs 2-6 with a short script; all outputs match.
