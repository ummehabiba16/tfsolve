---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) An interrupt between setting EEMWE and EEWE (more than 4 cycles) clears EEMWE, so EEWE writes nothing; disable interrupts around those two lines. (ii) Read the cell first and return if it equals ucData."
sources: ["EHP ATMega32_Core slides 29-35 (EECR: EEMWE, EEWE; steps to write EEPROM)", "EHP ATMega32_Core slides 33, 40 (EEPROM read)"]
---
**(i)** EEMWE is cleared by hardware **4 clock cycles** after it is set, and EEWE takes effect only if it is written within those 4 cycles. If an **interrupt occurs between line 10 (EEMWE = 1) and line 12 (EEWE = 1)**, the ISR runs for more than 4 cycles, EEMWE has been cleared by the time line 12 executes, and **nothing is written to the EEPROM**. (Another such case: an EEPROM write cannot start while the CPU is writing to Flash, as with a boot loader.)

*Avoid it* by disabling interrupts globally during the two timed writes and restoring them afterwards:

```c
uint8_t sreg = SREG;     /* save global interrupt state */
cli();                   /* no interrupt between EEMWE and EEWE */
EECR |= (1<<EEMWE);
EECR |= (1<<EEWE);
SREG = sreg;             /* restore */
```

**(ii)** Read the current content first and write only if it differs:

```c
#include <avr/io.h>
#include <avr/interrupt.h>

void EEPROM_write(unsigned int uiAddr, unsigned char ucData)
{
    uint8_t sreg;
    /* Wait for completion of previous write */
    while(EECR & (1<<EEWE))
    ;
    /* Read the current value at this address */
    EEAR = uiAddr;
    EECR |= (1<<EERE);           /* start eeprom read */
    if (EEDR == ucData)          /* same data already there */
        return;                  /* avoid the costly write */

    /* Set up address and data registers */
    EEAR = uiAddr;
    EEDR = ucData;
    sreg = SREG;
    cli();
    /* Write logical one to EEMWE */
    EECR |= (1<<EEMWE);
    /* Start eeprom write by setting EEWE */
    EECR |= (1<<EEWE);
    SREG = sreg;
}
```
