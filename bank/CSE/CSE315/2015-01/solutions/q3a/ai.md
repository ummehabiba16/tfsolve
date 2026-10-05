---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Device raises the interrupt (flag set); CPU finishes the current instruction; if the interrupt and the global I-bit are enabled it acknowledges the highest-priority request (clears its flag, clears I); pushes the PC on the stack; jumps to the fixed vector address, which holds a JMP to the ISR (at least 4 cycles); executes the ISR; RETI pops the PC and sets I; the main program resumes."
sources: ["EHP ATmega32 Interrupt slides 5, 9-12, 25 (execution sequence, vector table and priority, I-bit cleared by hardware)", "EHP ATMega32_Core slides 16-17 (four-cycle response, RETI)"]
---
1. **Interrupt request:** the device sets its interrupt flag (e.g. INTF0 for INT0).
2. **Finish the current instruction** (a multi-cycle instruction is completed first).
3. **Acknowledge:** if that interrupt is enabled (e.g. GICR, TIMSK) and the **global I-bit** in SREG is 1, the CPU accepts the **highest-priority** pending interrupt (lowest vector number). Its flag is cleared by hardware.
4. **Clear the I-bit**, so no other interrupt can interrupt the ISR (unless the ISR sets it again).
5. **Save the return address:** the **PC is pushed** onto the stack (2 bytes).
6. **Jump to the interrupt vector:** the PC is loaded with the fixed vector address of that interrupt (e.g. \$002 for INT0), where a `JMP ISR` instruction is stored. Steps 4-6 take at least **4 clock cycles**.
7. **Execute the ISR** (its prologue saves SREG and the registers it uses).
8. **RETI:** pops the PC and **sets the I-bit** again (4 cycles); the main program continues at the interrupted point.
