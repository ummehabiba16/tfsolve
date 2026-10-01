---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Three sources: hardware (NMI/INTR pins), software (INT n instruction), and error conditions from executing an instruction (pre-defined, e.g. divide by zero)."
sources: ["MHE INTR slide 10 (classification of 8086 interrupts)"]
---
An 8086 interrupt can come from **three** sources:

1. **External hardware signal on the NMI or INTR pin** (*hardware interrupt*). INTR is maskable: it is accepted only when IF = 1, and is acknowledged by $\overline{INTA}$. NMI is non-maskable and edge-triggered, and is always type 2 (for example, a power-failure signal).

2. **Execution of the INT instruction** (*software interrupt*), `INT n` with type $n$ from 0 to 255, including INT 3 (breakpoint) and INTO (type 4 on overflow). This is a user-defined interrupt.

3. **An error condition produced by executing an instruction** (*pre-defined / internal interrupt*). Examples: divide error (type 0) when the quotient of DIV/IDIV does not fit, and single step (type 1) when TF = 1.

In every case the 8086 pushes FLAGS, clears IF and TF, pushes CS and IP, and loads the ISR address from the interrupt vector table ($4\times$ type).
