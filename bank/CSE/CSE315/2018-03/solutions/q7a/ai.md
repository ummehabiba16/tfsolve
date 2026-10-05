---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Loop over all 1024 EEPROM addresses: EEPROM_read; if 'A' <= c <= 'Z', EEPROM_write(addr, c + ('a' - 'A')) (i.e. c + 32); leave other bytes unchanged. Read/write functions wait for EEWE = 0 and follow the EEMWE/EEWE sequence."
sources: ["EHP ATMega32_Core slides 25-41 (EEPROM registers, read/write functions, lowercase-to-uppercase example)"]
---
The ATmega32 has **1024 bytes** of EEPROM (addresses 0-1023).

```c
#include <avr/io.h>
#include <avr/interrupt.h>

unsigned char EEPROM_read(unsigned int uiAddress)
{
    while (EECR & (1 << EEWE));      // wait for any write to finish
    EEAR = uiAddress;
    EECR |= (1 << EERE);             // start read
    return EEDR;
}

void EEPROM_write(unsigned int uiAddress, unsigned char ucData)
{
    while (EECR & (1 << EEWE));      // wait for the previous write
    EEAR = uiAddress;
    EEDR = ucData;
    cli();                           // EEWE must follow EEMWE within 4 cycles
    EECR |= (1 << EEMWE);
    EECR |= (1 << EEWE);
    sei();
}

int main(void)
{
    unsigned int addr;
    unsigned char c;

    for (addr = 0; addr < 1024; addr++) {
        c = EEPROM_read(addr);
        if (c >= 'A' && c <= 'Z')                 // capital letter
            EEPROM_write(addr, c + ('a' - 'A'));  // e.g. 'B' (0x42) -> 'b' (0x62)
        // other bytes (e.g. 'd') are left unchanged
    }
    while (1);
}
```

Only bytes that are capital letters are rewritten, which also saves EEPROM write cycles (each write takes about 8.5 ms and EEPROM cells have limited endurance).
