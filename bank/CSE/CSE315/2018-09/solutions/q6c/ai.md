---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "EEPROM_write waits for EEWE = 0, loads EEAR and EEDR, sets EEMWE and then EEWE within 4 cycles; main calls it for addresses 0-25 with data 'a' + address."
sources: ["EHP ATMega32_Core slides 26-36 (EEPROM registers, write steps, EEPROM_write, a-z example)"]
---
```c
#include <avr/io.h>
#include <avr/interrupt.h>

void EEPROM_write(unsigned int uiAddress, unsigned char ucData)
{
    while (EECR & (1 << EEWE));      // 1. wait for the previous write to finish
    EEAR = uiAddress;                // 2. address
    EEDR = ucData;                   // 3. data
    cli();                           //    EEWE must follow EEMWE within 4 cycles
    EECR |= (1 << EEMWE);            // 4. master write enable
    EECR |= (1 << EEWE);             // 5. start the write
    sei();
}

int main(void)
{
    unsigned int uiAddress;
    for (uiAddress = 0; uiAddress < 26; uiAddress++)
        EEPROM_write(uiAddress, 'a' + uiAddress);   // 'a' = 97 ... 'z' = 122
    while (1);
}
```

Each write takes about 8.5 ms; the `while (EECR & (1<<EEWE))` loop at the start of `EEPROM_write` makes each call wait for the previous one, so no extra delay is needed (the slide example also adds a 200 ms delay).
