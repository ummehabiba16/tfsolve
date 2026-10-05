---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "On INTR: finish the current instruction; if IF = 1, run two INTA' bus cycles and read the type number n from D7-D0; push FLAGS; clear IF and TF; push CS; push IP; load IP from 4n and CS from 4n + 2; execute the ISR; IRET pops IP, CS, FLAGS and the program resumes."
sources: ["MHE INTR slides 11-14 (function of 8086 during interrupts, vector table)", "Brey, The Intel Microprocessors, Sec. 12-1 and 12-2 (interrupt processing, INTA cycles)"]
---
Steps of the 8086 for an external (INTR) interrupt:

1. **Request:** a device raises **INTR** (and holds it).
2. **Finish the current instruction:** INTR is sampled during the last clock of each instruction (string instructions can be interrupted between repetitions).
3. **Check IF:** if IF = 0 the request is ignored (masked); if IF = 1 it is accepted.
4. **Acknowledge:** the processor runs **two $\overline{INTA}$ bus cycles**. In the first the device is told the interrupt is accepted; in the second it puts the **interrupt type number $n$** (0-255) on D7-D0, which the 8086 reads.
5. **Push FLAGS** onto the stack.
6. **Clear IF and TF**, so further INTR interrupts and single stepping are disabled during the ISR.
7. **Push CS** and then **push IP** (the return address: the next instruction).
8. **Fetch the vector:** IP $\leftarrow$ word at $4n$, CS $\leftarrow$ word at $4n + 2$ in the interrupt vector table.
9. **Execute the ISR** (which should save and restore the registers it uses).
10. **IRET** at the end pops IP, CS and FLAGS (restoring IF and TF), and the interrupted program continues.

(For NMI and internal interrupts steps 3-4 are skipped: the type number is fixed.)
