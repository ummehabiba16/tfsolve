---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Interrupt vector: the fixed program-memory address for each interrupt source in the vector table (ATmega16: reset at $000, INT0 at $002, INT1 at $004, ...), usually holding a JMP to the ISR; a lower vector number means higher priority. (ii) ISR: the routine run when the interrupt occurs: entered with the PC saved and I cleared, saves/restores the registers it uses, does short work (shared variables volatile), ends with RETI."
sources: ["EHP ATmega32 Interrupt slides 8-15, 24-29 (vector table, program address, priority, ISR macro, ISR usage, volatile)"]
---
**(i) Interrupt vector**

- Each interrupt source of the ATmega16 (reset, INT0, INT1, INT2, timer, USART, SPI, ADC, EEPROM, ...) has a **fixed location in program memory** called its **interrupt vector**; together they form the **interrupt vector table** at the start of Flash (\$000 reset, \$002 INT0, \$004 INT1, ...).
- When the interrupt is accepted, the CPU loads the **PC with that address**. The vector normally contains a **`JMP` to the ISR**.
- The vector number also gives the **priority**: a lower vector number has a higher priority (INT0 > INT1 > INT2 ...).
- In C the vectors are named (`INT0_vect`, `TIMER1_OVF_vect`, `ADC_vect`), and the `ISR()` macro fills in the table.

**(ii) Interrupt Service Routine (ISR)**

- The **function executed when an interrupt occurs**, written as `ISR(vector_name) { ... }`.
- On entry the hardware has saved the PC and cleared the global I-bit; the ISR prologue saves SREG and the registers it uses, and the epilogue restores them.
- It ends with **`RETI`**, which returns to the interrupted program and sets I again.
- It takes no arguments and returns nothing, so it shares data with `main()` through **`volatile` global variables**.
- It should be **short** (in time): do only what is necessary, so that other interrupts and the main program are not delayed.
