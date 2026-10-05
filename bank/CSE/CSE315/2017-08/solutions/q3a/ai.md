---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Program-invisible registers are internal registers that programs cannot read or write directly with normal instructions. In the 80286/80386: the descriptor caches (base, limit, access rights) behind CS, DS, ES, SS, FS, GS; the hidden base/limit/attribute parts of LDTR and TR; and GDTR and IDTR (base + limit, loaded only by LGDT/LIDT)."
sources: ["Brey, The Intel Microprocessors, Sec. 2-3 (program-invisible registers)", "MHE 80386-updated slide 8 (6 program invisible segment descriptor registers, 73 bits)", "MHE 80286 slides (shadow registers)"]
---
**Program-invisible registers** are registers inside the processor that a program cannot access directly with ordinary instructions (`MOV`, `PUSH`, ...). They are loaded automatically by the processor, or only by special system instructions, and are used to speed up and control protected-mode memory management. They exist in the 80286 and later processors.

**1. Segment descriptor caches (shadow registers).** Each segment register (CS, DS, ES, SS, and FS, GS on the 80386) has a visible 16-bit **selector** part and an invisible **cache**:

```text
        visible            program-invisible (descriptor cache)
     +----------+   +-------------+-------------+------------+
 CS  | selector |   | base (32)   | limit (32)  | access (9) |
 DS  | selector |   |    ...      |    ...      |    ...     |
 ... |          |   |             |             |            |
     +----------+   +-------------+-------------+------------+
                    80386: 32 + 32 + 9 = 73 bits per register
```

When a selector is loaded, the processor reads the descriptor from the GDT/LDT once and stores its base, limit and access rights in the cache. Later memory accesses use the cache, so the descriptor table is not read on every access.

**2. GDTR and IDTR.** Hold the **base address and limit** of the Global Descriptor Table and the Interrupt Descriptor Table (80386: 32-bit base + 16-bit limit). They are loaded with `LGDT`/`LIDT` (system instructions), not by normal moves.

**3. LDTR.** Has a visible selector (pointing to an LDT descriptor in the GDT) and an invisible cache with the LDT's base, limit and attributes.

**4. TR (task register).** Visible selector of the current TSS descriptor, plus an invisible cache with the TSS base, limit and attributes, used during task switches.

Because of these registers, protected-mode addressing (selector $\to$ descriptor $\to$ base + offset) runs almost as fast as real-mode segment arithmetic.
