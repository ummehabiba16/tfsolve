---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "MP: CPU only, external memory/I/O, bigger and costlier, more power, von Neumann, general purpose (PC). MCU: CPU + RAM + ROM + I/O + timers on one chip, small and cheap, low power with sleep modes, Harvard, dedicated embedded use."
sources: ["EHP ATMega32_Core slides 2-4 (microprocessor vs microcontroller table)", "MHE Intro slides (microprocessor vs microcontroller basic concept)"]
---
| | Microprocessor | Microcontroller |
|:--|:--|:--|
| 1. What is on the chip | Only the CPU (ALU, CU, registers). RAM, ROM, I/O ports, timers must be connected **externally** | CPU **plus** RAM, ROM/Flash, EEPROM, I/O ports, timers, ADC, serial interfaces on **one chip** |
| 2. Size and cost of system | Many external chips: large board, high total cost | Few external parts: small, compact and cheap |
| 3. Power | Higher power, usually no power-saving modes; not suited to batteries | Low power, with sleep modes (idle, power-down) |
| 4. Architecture | Usually von Neumann (program and data share one memory) | Usually Harvard (separate program and data memory) |
| 5. Speed of operations | Memory and I/O accesses go off-chip over the system bus, so they are slower | Most operations are internal, so they are fast |
| 6. Use | General-purpose computing (PCs, laptops), e.g. Intel 8086, Core i7 | Dedicated embedded control (washing machine, remote, robot), e.g. ATmega32, 8051, PIC |

Any five of these rows answer the question. A microprocessor also usually runs at a much higher clock (GHz) with a wide data bus (32/64-bit), while a microcontroller runs at a few MHz with an 8- or 16-bit data path.
