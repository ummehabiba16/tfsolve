---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "8(c)-1 is a microprocessor (Intel 8085: CPU registers, ALU, interrupt and serial control, address and address/data buffers to external memory, no on-chip memory or peripherals). 8(c)-2 is a microcontroller (AVR: on-chip Flash, SRAM, timers, ADC, SPI, TWI, watchdog, oscillators and I/O ports)."
sources: ["EHP ATMega32_Core slides 2-4, 8-9 (microprocessor vs microcontroller, ATmega32 vs 8086 block diagrams)", "EHP Intro to micro slide 2 (what is a microcontroller)"]
---
**Figure 8(c)-1 is a microprocessor** (it is the block diagram of the Intel **8085**):

- It contains only the **CPU**: accumulator, temporary register, flag flip-flops, ALU, instruction register and decoder, register array (B, C, D, E, H, L), stack pointer and program counter, timing and control.
- There is **no program memory, no RAM and no timers/ADC** on the chip. Instead it has an **address buffer** and an **address/data buffer** (multiplexed bus) to connect **external** memory and I/O, plus bus control signals (RD, WR, ALE, IO/M), DMA (HOLD/HLDA) and reset pins.
- Interrupt control (INTR, INTA, RST 5.5/6.5/7.5, TRAP) and simple serial I/O (SID, SOD) only handle external devices.

**Figure 8(c)-2 is a microcontroller** (an AVR, like the ATmega/ATtiny family):

- The CPU (program counter, stack pointer, general-purpose registers, ALU, interrupt unit) is on the **same chip** as **program Flash** (with programming logic) and **SRAM**.
- On-chip **peripherals**: Timer/Counter0 and 1, **ADC**, analog comparator, **SPI**, **TWI**, **watchdog timer**, internal/calibrated oscillators.
- **I/O ports** (Port A, Port B data and direction registers and drivers) connect directly to the outside world. No external bus to memory is shown.

**Reason:** a microprocessor is just a CPU that needs external memory and peripherals connected through a system bus; a microcontroller integrates CPU, memory and peripherals on one chip for a dedicated embedded task.
