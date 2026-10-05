---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Harvard: program and data are in separate memories with separate buses, so instruction fetch and data access happen at the same time. ATmega16's third memory is the EEPROM (512 bytes): non-volatile data memory that the program can write byte by byte at run time, needed to keep data (settings, calibration, counters, passwords) through power loss; SRAM loses data at power-off and Flash is for code and cannot easily be rewritten byte-wise."
sources: ["EHP ATMega32_Core slides 10, 18-25 (Harvard architecture, memory spaces, EEPROM data memory)"]
---
**Basic property of Harvard architecture:** **separate memories and buses for program and data**. The CPU can fetch the next instruction from program memory **at the same time** as it reads or writes data in data memory (and the two can have different widths).

**The third memory of the ATmega16: EEPROM (512 bytes; 1 KB in ATmega32)**

The ATmega16 has:

1. **Flash** (16 KB): program memory, non-volatile, but erased/written in pages and normally only during programming.
2. **SRAM** (1 KB) + registers + I/O: data memory, fast, but **volatile**: its contents are lost when power is removed.
3. **EEPROM**: a separate data space for **non-volatile data**.

**Why it is needed.** Many embedded applications must **remember data after power is switched off**, and must change that data while running: user settings (volume, set temperature), calibration constants, counters (e.g. number of washes), passwords, last state. SRAM cannot keep it, and Flash is meant for code (page-wise erase, limited and awkward self-programming). The EEPROM can be **read and written byte by byte by the program** at run time (EEAR, EEDR, EECR registers) and keeps the data without power (about 100,000 write cycles).
