---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "A double-indirect jump takes its target from a memory location that is itself addressed through a register, e.g. JMP TABLE[SI] or JMP [BX]: register -> memory word -> new IP. Two levels of indirection (register gives the address of the pointer, the pointer gives the target), hence 'double indirect'; used for jump tables."
sources: ["Brey, The Intel Microprocessors, Sec. 6-1 (indirect jumps using an index, double-indirect jump, jump tables)"]
---
**Double-indirect jump.** In an ordinary indirect jump such as `JMP AX`, the new IP is in a register. In a **double-indirect jump** the register does **not** contain the target; it contains the **address of a memory location**, and the **target address is stored in that memory location**:

$$\text{register (+ displacement)} \ \to\ \text{memory word} \ \to\ \text{new IP}$$

**Example (jump table):**

```text
TABLE   DW  ZERO, ONE, TWO      ; addresses of three routines
        ...
        MOV  SI, BX             ; BX = choice (0, 1 or 2)
        ADD  SI, SI             ; x2: each table entry is a word
        JMP  TABLE[SI]          ; IP <- word at DS:(TABLE + SI)
```

If BX = 1, SI = 2. The CPU reads the word at TABLE + 2 (the address of `ONE`) and loads it into IP, so control goes to `ONE`. (`JMP WORD PTR [BX]` and `JMP FAR PTR [DI]`, which also loads CS, work the same way.)

**Why it is called double indirect.** The target is reached through **two levels of indirection**: first the register gives the address of a pointer in memory, and then that pointer gives the jump address. A register-indirect jump (`JMP AX`) has only one level.
