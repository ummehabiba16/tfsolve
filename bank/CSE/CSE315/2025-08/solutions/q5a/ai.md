---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Shadow registers hold each selected descriptor so memory is not read twice on every access. CS, DS, SS, ES, LDTR and TR have them: 24-bit base + 16-bit limit + 8-bit access = 48 bits each."
sources: ["MHE 80286 slides 64-71 (did you note: 100% degradation; program-invisible registers)"]
---
**Why shadow registers are needed.** In protected mode a segment register holds only a selector. To form a physical address, the 80286 must read the 8-byte descriptor from the GDT or LDT to get the base, and then access the operand. Without help, **every memory access becomes two accesses**: a **100% degradation** in memory access time.

The solution is to keep, alongside each segment register, a program-invisible **shadow (descriptor cache) register**. When a new selector is loaded, the descriptor is read once and copied into the shadow register. It is then used for all later accesses until the selector changes.

**Registers that must have shadow registers, and their sizes:**

| Register | Visible part | Shadow / cache part | Shadow size |
|:--|:-:|:--|:-:|
| CS | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |
| DS | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |
| SS | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |
| ES | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |
| LDTR | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |
| TR | 16-bit selector | base 24 + limit 16 + access 8 | 48 bits |

GDTR and IDTR do not hold a selector. They hold the table address directly: 24-bit base + 16-bit limit = 40 bits.
