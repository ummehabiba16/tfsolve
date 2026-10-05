---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Program memory (ATmega32): 16K x 16 Flash, 0x0000-0x3FFF, application section from 0x0000 (reset and interrupt vectors at the bottom) and boot loader section at the top. Data memory: 0x0000-0x001F 32 registers, 0x0020-0x005F 64 I/O registers, 0x0060-0x085F 2 KB internal SRAM (2144 locations). EEPROM is a separate 1 KB space."
sources: ["EHP ATMega32_Core slides 18-25 (program memory map, data memory map, EEPROM)"]
---
**Program memory map (Flash)**

```text
 word address
 0x0000  +---------------------------------+
         | reset and interrupt vectors      |
         | application program section      |
         |                                 |
         +---------------------------------+  (boot size set by fuses)
         | boot loader section             |
 0x3FFF  +---------------------------------+
         16K x 16 = 32 KB (ATmega32)
```

- 32 KB of in-system reprogrammable Flash, organized as **16K $\times$ 16** (instructions are 16 or 32 bits), so the PC is 14 bits.
- Split into an **application section** (from 0x0000, starting with the reset and interrupt vectors) and a **boot loader section** at the top, which can reprogram the application section.

**Data memory map**

```text
 address
 0x0000  +-------------------------------+
         | 32 general purpose registers  |  R0 - R31
 0x001F  +-------------------------------+
 0x0020  | 64 I/O registers              |  (I/O addresses 0x00-0x3F for IN/OUT)
 0x005F  +-------------------------------+
 0x0060  | internal SRAM (2048 bytes)    |  variables, stack (grows down from 0x085F)
 0x085F  +-------------------------------+
```

- 2144 locations in one linear space: registers, I/O registers and 2 KB SRAM, accessible with the LD/ST family (five addressing modes) and the I/O registers also with IN/OUT.
- The **EEPROM** (1 KB) is a separate data space accessed through EEAR, EEDR and EECR.
