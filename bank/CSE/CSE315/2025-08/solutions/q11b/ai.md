---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Master: DDRB = MOSI, SCK, PB4, PB3 out; both SS lines high; SPCR = SPE|MSTR|SPR0. Slaves: DDRB = MISO out; SPCR = SPE."
sources: ["EHP Serial Communication slides 90-103 (SPCR, SPI master/slave config)"]
---
Assumptions: MSB first (DORD = 0), mode 0 (CPOL = CPHA = 0), SPI clock = fosc/16, polling (no SPI interrupt). Q is selected by P's PB4 and R by P's PB3.

```c
#include <avr/io.h>

/* Master P */
void SPI_MasterInit(void)
{
    /* MOSI (PB5), SCK (PB7), SS_Q (PB4), SS_R (PB3) as output; MISO input */
    DDRB = (1<<DDB5)|(1<<DDB7)|(1<<DDB4)|(1<<DDB3);
    /* both slaves deselected (SS high) */
    PORTB |= (1<<PB4)|(1<<PB3);
    /* Enable SPI, Master, set clock rate fck/16 */
    SPCR = (1<<SPE)|(1<<MSTR)|(1<<SPR0);
}

/* Slaves Q and R (same code on both) */
void SPI_SlaveInit(void)
{
    /* Set MISO output, all others input */
    DDRB = (1<<DDB6);
    /* Enable SPI (MSTR = 0 -> slave) */
    SPCR = (1<<SPE);
}
```

On the master, $\overline{SS}$ (PB4) is set as an output so that it does not switch the master back to slave mode, and it is used as a general pin to select Q.
