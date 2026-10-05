---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "1. Wait until EEWE = 0 (previous write done). 2. (Wait for any Flash self-programming, SPMEN = 0.) 3. Write the address to EEAR. 4. Write the data to EEDR. 5. Write 1 to EEMWE (with EEWE = 0). 6. Within 4 clock cycles write 1 to EEWE; keep interrupts disabled between 5 and 6."
sources: ["EHP ATMega32_Core slides 26-35 (EEAR, EEDR, EECR, steps to write into EEPROM, EEPROM_write)"]
---
**Registers:** EEAR (address 0-1023), EEDR (data), EECR (control: EEMWE, EEWE, EERE).

**Steps**

1. **Wait until EEWE becomes 0**: a previous write (about 8.5 ms) must have finished.
2. (Only if the program can write Flash, e.g. a boot loader: wait until SPMEN in SPMCR is 0.)
3. Write the new EEPROM **address** to **EEAR**.
4. Write the new **data** to **EEDR**.
5. Write a logical **1 to EEMWE** while writing 0 to EEWE in EECR.
6. **Within four clock cycles** after setting EEMWE, write a logical **1 to EEWE**. (Hardware clears EEMWE after 4 cycles, so interrupts must be disabled between steps 5 and 6.)

The CPU is halted for 2 cycles after EEWE is set, and EEWE is cleared by hardware when the write is done.

```c
void EEPROM_write(unsigned int addr, unsigned char data)
{
    while (EECR & (1 << EEWE));   // 1
    EEAR = addr;                  // 3
    EEDR = data;                  // 4
    cli();
    EECR |= (1 << EEMWE);         // 5
    EECR |= (1 << EEWE);          // 6
    sei();
}
```
