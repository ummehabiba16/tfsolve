---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "The CPU finishes the current instruction, pushes the PC (2 bytes), clears the I-bit and jumps to the fixed vector (at least 4 cycles); the ISR runs; RETI pops the PC and sets the I-bit (4 cycles). Lower vector number = higher priority."
sources: ["EHP ATMega32_Core slides 16-17 (interrupt execution, 4 clock cycles)", "EHP ATmega32 Interrupt slides 5, 9-10, 25 (execution sequence, vector priority, nested interrupts)"]
---
1. A device raises an interrupt and its flag is set. If the specific enable bit and the global I-bit (SREG) are set, the CPU **finishes the current instruction**, completing it first even if it is a multi-cycle instruction.
2. **Response takes at least 4 clock cycles:** the **Program Counter is pushed onto the stack** (2 bytes), the I-bit is cleared (so nested interrupts are disabled by default), and the CPU jumps to the interrupt's fixed **vector address** (e.g. \$002 for INT0). The JMP there takes 3 cycles and leads to the ISR.
3. The ISR executes. Registers and SREG are saved and restored by the compiler-generated code.
4. **RETI takes 4 clock cycles:** the PC (two bytes) is popped from the stack, the SP is incremented by 2, and the **I-bit is set** again. Normal execution resumes.

If several interrupts are pending, the one with the **lower vector number has higher priority** (INT0 > INT1 > INT2).
