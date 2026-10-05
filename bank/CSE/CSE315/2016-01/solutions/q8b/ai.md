---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Flash: 32 KB in-system reprogrammable, organized as 16K x 16 (most instructions 16-bit), addressed by a 14-bit PC, split into a boot loader section and an application section (10,000 write/erase cycles). Data memory: 2144 locations: 0x0000-0x001F the 32 general registers, 0x0020-0x005F the 64 I/O registers, 0x0060-0x085F the 2 KB internal SRAM (stack at the top); 2-cycle SRAM access."
sources: ["EHP ATMega32_Core slides 18-23 (program memory, Flash 16K x 16, boot and application sections, data SRAM map, access cycles)"]
---
The ATmega32 has two main memory spaces (Harvard architecture), plus a separate 1 KB EEPROM.

**In-system reprogrammable Flash (program memory)**

- **32 KB** of Flash that can be reprogrammed in the system (through SPI/ISP, JTAG or by the program itself through a boot loader).
- AVR instructions are 16 or 32 bits wide, so the Flash is organized as **16K $\times$ 16** words; the **program counter is 14 bits** (addresses 0x0000-0x3FFF).
- Divided into a **boot loader section** (at the top, size set by fuses) and an **application program section** (from 0x0000, which also holds the reset and interrupt vectors). The boot section can rewrite the application section (self-programming).
- Endurance about 10,000 write/erase cycles.

**Data memory (SRAM space): 2144 locations**

```text
 0x0000 - 0x001F   32 general purpose registers R0-R31
 0x0020 - 0x005F   64 I/O registers (PORTx, DDRx, TCCR1A, ADMUX, ...)
 0x0060 - 0x085F   2048 bytes internal data SRAM (variables, stack at the top)
```

- The registers and I/O registers are also mapped into this space, so they can be reached with normal load/store instructions (I/O registers also with IN/OUT at addresses 0x00-0x3F).
- Five addressing modes: direct, indirect, indirect with displacement, indirect with pre-decrement and post-increment (using X, Y, Z pointers).
- An SRAM access takes **2 CPU cycles**.
