---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Finish the current instruction; for INTR check IF and get the type number n by INTA cycles (NMI/internal/INT n have fixed or given numbers); push FLAGS; clear IF and TF; push CS and IP (EIP; in protected mode also SS:ESP on a privilege change and maybe an error code); load the ISR address from the vector table (4n) or IDT (8n, through a gate); execute the ISR; IRET restores IP, CS, FLAGS."
sources: ["MHE INTR slides 11-15 (function of the 8086 during interrupts, vector table)", "Brey, The Intel Microprocessors, Sec. 12-1 (interrupt processing in 8086-Pentium)"]
---
When an Intel processor accepts an interrupt:

1. **Finish the current instruction** (string instructions may be interrupted between repetitions).
2. **Identify the interrupt type $n$:** for INTR, check that **IF = 1**, then run the **interrupt acknowledge ($\overline{INTA}$) cycles** and read $n$ from the data bus; NMI is type 2; internal interrupts and `INT n` have fixed or given numbers.
3. **Push the FLAGS** register on the stack.
4. **Clear IF and TF** (no more INTR interrupts or single steps during the ISR).
5. **Push CS and IP** (EIP on 386 and later): the return address.
   - In **protected mode** (286/386/Pentium), if the handler is more privileged, the processor first switches to the stack given in the TSS and pushes the old SS:SP (SS:ESP); some exceptions also push an **error code**.
6. **Get the ISR address:** in real mode from the **interrupt vector table** at $4n$ (IP at $4n$, CS at $4n+2$); in protected mode from the **IDT** entry $n$ at IDTR base + $8n$, an interrupt/trap/task gate that gives the selector and offset (with privilege checks).
7. **Execute the ISR.**
8. **IRET** pops IP (EIP), CS and FLAGS (and SS:ESP if the level changed), and the interrupted program continues.
