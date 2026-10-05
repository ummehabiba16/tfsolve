---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Device requests; CPU finishes the current instruction; acknowledges; saves state and PC on the stack; loads the ISR address from the vector table; executes the ISR; restores state and PC (RETI); resumes the main program."
sources: ["EHP ATmega32 Interrupt slide 5 (interrupt execution sequence)", "EHP ATMega32_Core slides 16-17 (interrupt response and RETI)"]
---
1. A device **issues an interrupt** (its flag is set).
2. The CPU **finishes the current instruction**.
3. The CPU **acknowledges** the interrupt (if it and the global I-bit are enabled; the highest-priority one is chosen and its flag cleared).
4. The CPU **saves its state and the PC on the stack** (the AVR pushes the PC and clears the I-bit; the ISR saves SREG and registers).
5. The CPU **loads the ISR address into the PC** from the interrupt vector table (a JMP to the ISR at the fixed vector address).
6. The CPU **executes the ISR**.
7. The CPU **restores its state and the PC** from the stack (`RETI` also sets the I-bit).
8. **Normal execution resumes** where it was interrupted.
