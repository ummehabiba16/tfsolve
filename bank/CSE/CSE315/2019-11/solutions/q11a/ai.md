---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Device requests; CPU finishes the current instruction; acknowledges; saves state and PC on the stack (and clears the global interrupt bit); loads the ISR address from the vector table into PC; runs the ISR; restores state and PC (RETI); resumes the main program."
sources: ["EHP ATmega32 Interrupt slide 5 (interrupt execution sequence)", "EHP ATMega32_Core slides 16-17 (interrupt execution in four cycles, RETI)"]
---
1. **A device issues an interrupt** (sets its interrupt flag, e.g. INTF0).
2. **The CPU finishes the current instruction** (a multi-cycle instruction is completed first).
3. **The CPU acknowledges the interrupt**: if the interrupt and the global interrupt bit (I in SREG) are enabled, the highest-priority pending request is accepted, and its flag is cleared.
4. **The CPU saves its state and the PC on the stack.** In the ATmega32 the hardware pushes the PC (2 bytes) and clears the I-bit, so other interrupts are blocked; the ISR prologue saves SREG and the registers it uses.
5. **The CPU loads the ISR address into the PC.** It jumps to the fixed vector address of that interrupt (e.g. \$002 for INT0), where a `JMP` to the ISR is stored. Steps 4-5 take at least 4 clock cycles.
6. **The CPU executes the ISR.**
7. **The CPU restores its state and the PC from the stack.** The ISR epilogue restores the registers and SREG, and `RETI` pops the PC and sets the I-bit again (4 cycles).
8. **Normal execution resumes** at the instruction after the one that was interrupted.
