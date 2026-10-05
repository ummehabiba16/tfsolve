---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Finish the current instruction; (for INTR: IF must be 1, then two INTA' cycles to read the type n); push FLAGS; clear IF and TF; push CS; push IP; load IP from 4n and CS from 4n + 2; run the ISR; IRET pops IP, CS and FLAGS."
sources: ["MHE INTR slides 11-15 (function of the 8086 during interrupts)", "Brey, The Intel Microprocessors, Sec. 12-1"]
---
1. **Finish the current instruction.** (INTR and NMI are checked at the end of each instruction.)
2. **Get the type number $n$.** For INTR, only if **IF = 1**: the 8086 runs two **$\overline{INTA}$** cycles and reads $n$ from D7-D0. NMI is type 2; internal interrupts and `INT n` give $n$ directly.
3. **Push the FLAGS** register on the stack (SP decreases by 2).
4. **Clear IF and TF**: further INTR interrupts and single-stepping are disabled inside the ISR.
5. **Push CS**, then **push IP**: the return address.
6. **Load the new IP and CS from the vector table:** IP $\leftarrow$ [4n], CS $\leftarrow$ [4n + 2].
7. **Execute the ISR** at CS:IP.
8. **IRET** at the end pops **IP, CS and FLAGS** (restoring IF and TF), and the interrupted program continues.
