---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "It does not wait for a previous EEPROM write (about 8.5 ms) to finish: if EEWE is still 1, changing EEAR/EEDR and setting EEWE again corrupts or ignores the write. Add 'while (EECR & (1<<EEWE));' at the start. Also keep interrupts off between setting EEMWE and EEWE (they must be within 4 cycles)."
sources: ["EHP ATMega32_Core slides 29-35 (EECR, EEMWE/EEWE, steps to write EEPROM, EEPROM_write function)"]
---
**Why it fails sometimes**

An EEPROM write takes a long time (about **8.5 ms**). While it is in progress the **EEWE** bit stays 1, and the EEPROM cannot be written again, and **EEAR/EEDR must not be changed**. Eliot's function starts writing immediately. If it is called again before the previous write has finished (e.g. writing several bytes in a loop), it changes EEAR and EEDR during the ongoing write and its own EEWE request is ignored, so data is lost or written to the wrong address. When calls are far apart it works, which is why it fails only **sometimes**.

A second, rarer cause: EEWE must be set **within 4 clock cycles** after EEMWE (hardware clears EEMWE after 4 cycles). If an interrupt occurs between the two statements, the ISR delays the EEWE write beyond 4 cycles and the write does not happen.

**Corrected function**

```c
void EEPROM_write(unsigned int uiAddress, unsigned char ucData)
{
    while (EECR & (1 << EEWE));   // added: wait for completion of previous write
    EEAR = uiAddress;
    EEDR = ucData;
    cli();                        // added: no interrupt between EEMWE and EEWE
    EECR |= (1 << EEMWE);
    EECR |= (1 << EEWE);          // start the write (within 4 cycles of EEMWE)
    sei();                        // added: re-enable interrupts
}
```

The first added line is the essential fix (step 1 of the data sheet's write procedure). `cli()`/`sei()` are needed only if interrupts are used in the program (to restore the previous state exactly, save and restore SREG instead of calling `sei()`).
