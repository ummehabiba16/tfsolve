---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Write: no wait for a previous write (EEWE), no interrupt protection between EEMWE and EEWE, 16-bit ucData into the 8-bit EEDR. Read: no EEWE poll before reading, and EEMRE does not exist in EECR (compile error / wrong bit)."
sources: ["EHP ATMega32_Core slides 25-35, 40 (EEPROM registers, EECR bits, steps to write, EEPROM_write/EEPROM_read functions)"]
---
Compared with the correct functions in the slides:

**EEPROM_write**

1. **No wait for the previous write.** Step 1, "wait until EEWE becomes zero" (`while(EECR & (1<<EEWE));`), is missing. An EEPROM write takes several ms. If the function is called again (e.g. in a loop), EEAR and EEDR are changed and EEWE is set while the previous write is still in progress, so data is lost or corrupted.
2. **Timed sequence not protected.** EEWE must be set within **4 clock cycles** of EEMWE. If an interrupt occurs between lines 7 and 9, EEMWE is cleared by hardware and **nothing is written**. Disable interrupts (`cli()`, then restore SREG) around the two lines.
3. **Data type.** `ucData` is `unsigned int` (16 bits), but EEDR and each EEPROM cell are **8 bits**. The upper byte is silently lost, so a caller who passes a value above 255 loses data. It should be `unsigned char`.

**EEPROM_read**

4. **No wait for an ongoing write.** The user should poll EEWE before starting a read. If a write is in progress, it is **neither possible to read the EEPROM nor to change EEAR**, so the read returns wrong data.
5. **EEMRE does not exist.** EECR has only EERIE, EEMWE, EEWE and EERE. There is no "master read enable", so `(1<<EEMRE)` is a compile error (undefined). If it were defined as some other bit, it would wrongly set that bit (e.g. EEMWE) and could arm a write. A read needs only EERE.
6. The address must be 0 to 1023 (1KB EEPROM). Neither function checks `uiAddress`.

**Corrected code**

```c
void EEPROM_write(unsigned int uiAddress, unsigned char ucData)
{
    uint8_t sreg;
    /* Wait for completion of previous write */
    while(EECR & (1<<EEWE));
    /* Set up address and data registers */
    EEAR = uiAddress;
    EEDR = ucData;
    sreg = SREG;
    cli();
    /* Write logical one to EEMWE */
    EECR |= (1<<EEMWE);
    /* Start eeprom write by setting EEWE */
    EECR |= (1<<EEWE);
    SREG = sreg;
}

unsigned char EEPROM_read(unsigned int uiAddress)
{
    /* Wait for completion of previous write */
    while(EECR & (1<<EEWE));
    /* Set up address register */
    EEAR = uiAddress;
    /* Start eeprom read by writing EERE */
    EECR |= (1<<EERE);
    /* Return data from data register */
    return EEDR;
}
```
