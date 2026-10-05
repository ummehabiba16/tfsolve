---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A task switch is triggered by JMP/CALL to a TSS descriptor or task gate, an interrupt/exception through a task gate, or IRET with NT = 1. The processor checks privilege and the new TSS (present, not busy, limit >= 67h), saves all registers of the current task into its TSS (via TR), loads TR with the new selector, marks the new TSS busy, loads all registers (CR3, LDTR, EFLAGS, EIP, general and segment registers) from the new TSS, sets the back link and NT for CALL/interrupt, sets TS in CR0, and continues at the new task's CS:EIP."
sources: ["Brey, The Intel Microprocessors, Sec. 17-6 (task switching)", "Intel 80386 Programmer's Reference Manual, Sec. 7.5-7.6 (task switching, task linking)"]
---
**What triggers a task switch**

1. A far `JMP` or `CALL` whose selector points to a **TSS descriptor** or a **task gate**.
2. An **interrupt or exception** whose IDT entry is a **task gate**.
3. `IRET` when the **NT** (nested task) flag is 1: return to the task in the back link.

**Steps performed by the processor**

```text
   current task                                  new task
  +-------------+                              +-------------+
  | TSS (old)   | <-- (2) save all registers   | TSS (new)   |
  +-------------+                              +-------------+
         ^                                            |
   TR (old selector)  -- (3) TR <- new selector --> (4) load all registers
                                                      |
                                       (5) continue at new CS:EIP
```

1. **Checks.** For JMP/CALL the CPL and selector RPL must be $\le$ the DPL of the TSS descriptor or task gate. The new TSS descriptor must be present, **not busy** (no recursion), and its limit at least 67h (104 bytes).
2. **Save the old state.** All general registers, segment selectors, EFLAGS and EIP (pointing to the next instruction) of the current task are stored in the **current TSS** (found through TR).
3. **Switch TR.** TR is loaded with the selector of the new TSS, and its hidden part with the new TSS descriptor. For a JMP the old TSS's busy bit is cleared; for CALL/interrupt it stays busy.
4. **Load the new state.** The new TSS's busy bit is set. The processor loads **CR3** (new page directory, flushing the TLB), **LDTR**, EFLAGS, EIP, the general registers and the segment registers (with full descriptor checks) from the new TSS. For CALL and interrupts it writes the old TSS selector into the new TSS's **back link** and sets **NT = 1**, so a later IRET returns to the old task.
5. **Set TS** (task switched) in CR0, so the next floating-point instruction lets the OS save the coprocessor state lazily.
6. Execution continues at the new task's **CS:EIP**. Its privilege level is the RPL of the CS loaded from its TSS.

When the new task executes `IRET` with NT = 1, the same steps run in reverse: its state is saved, its busy bit cleared, and the task in the back link resumes exactly where it stopped.
