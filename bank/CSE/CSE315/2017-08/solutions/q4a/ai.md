---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The 80386 TSS (at least 104 bytes, described by a TSS descriptor in the GDT and selected by TR) stores a task's state: back link, SS0:ESP0, SS1:ESP1, SS2:ESP2, CR3, EIP, EFLAGS, the 8 general registers, the 6 segment selectors, the LDT selector, the T bit and the I/O map base (plus the I/O permission bitmap). Three stack sets give each privilege level 0-2 its own protected stack for calls/interrupts from less privileged code."
sources: ["Brey, The Intel Microprocessors, Sec. 17-6 (task state segment, task switching)", "Intel 80386 Programmer's Reference Manual, Sec. 7.1 (TSS format), Sec. 6.3.4.1 (stack switching)"]
---
**Task State Segment (TSS).** A TSS is a special segment that holds **everything needed to suspend and resume a task**. Each task has one. It is described by a **TSS descriptor** in the GDT, and the **task register (TR)** selects the TSS of the current task. On a task switch the processor saves the current state into the old TSS and loads the new state from the new TSS.

**80386 TSS layout** (32-bit words, offsets in hex)

```text
 offset  31                    16 15                     0
  64    | I/O map base            | 0 ...               |T |
  60    | 0                       | LDT selector           |
  5C    | 0                       | GS                     |
  58    | 0                       | FS                     |
  54    | 0                       | DS                     |
  50    | 0                       | SS                     |
  4C    | 0                       | CS                     |
  48    | 0                       | ES                     |
  44-28 | EDI, ESI, EBP, ESP, EBX, EDX, ECX, EAX           |
  24    | EFLAGS                                           |
  20    | EIP                                              |
  1C    | CR3 (PDBR: the task's page directory)            |
  18    | 0                       | SS2                    |
  14    | ESP2                                             |
  10    | 0                       | SS1                    |
  0C    | ESP1                                             |
  08    | 0                       | SS0                    |
  04    | ESP0                                             |
  00    | 0                       | back link (previous TSS)|
         + I/O permission bitmap (optional, after offset 68h)
```

- **Back link:** selector of the TSS of the task that called this one (used by IRET when NT = 1).
- **SS0:ESP0 ... SS2:ESP2:** stacks for privilege levels 0, 1, 2.
- **CR3:** each task can have its own page directory (own address space).
- **EIP, EFLAGS, general and segment registers, LDT selector:** the task's complete register state.
- **T bit:** debug trap on switching to this task. **I/O map base:** offset of the I/O permission bitmap.

**Why three sets of stack registers.** When a task calls more privileged code (through a call gate) or an interrupt/exception transfers control to a more privileged handler, the processor **switches to a new stack** for the target level, taking SS:ESP from the TSS entry of that level (0, 1 or 2). Each level has its own stack so that more privileged code never relies on a stack that less privileged code controls (it could be too small, invalid, or contain planted data), which protects the system and guarantees a valid stack. No entry is needed for level 3, because level 3 is never entered by a call from a more privileged level, only by returning.
