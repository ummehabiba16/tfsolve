---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Master: SPI_Transceiver writes SPDR, waits for SPIF, returns SPDR; select/deselect pull the slave's SS low/high. Slave: SPI_SlaveTransceiver preloads SPDR, waits for SPIF, returns the received byte."
sources: ["EHP Serial Communication slides 91-92, 97-99, 104-107 (transmission steps, SPIF, data exchange)"]
---
Assumptions as in (b). SPI is full duplex: whatever is in a device's SPDR is exchanged with the other side's SPDR during the 8 clock pulses.

```c
/* ----- Master P ----- */
void SPI_Select(uint8_t pin)      /* pin = PB4 (Q) or PB3 (R) */
{
    PORTB &= ~(1<<pin);           /* pull SS low: activate slave */
}

void SPI_Deselect(uint8_t pin)
{
    PORTB |= (1<<pin);            /* pull SS high */
}

char SPI_Transceiver(char cData)  /* send and receive one byte */
{
    /* Start transmission */
    SPDR = cData;
    /* Wait for transmission complete */
    while(!(SPSR & (1<<SPIF)));
    /* Return newly received data */
    return SPDR;
}

/* ----- Slaves Q and R ----- */
char SPI_SlaveTransceiver(char cData)
{
    /* load the byte to be shifted out when the master clocks */
    SPDR = cData;
    /* Wait for reception complete */
    while(!(SPSR & (1<<SPIF)));
    /* Return data register (byte received from master) */
    return SPDR;
}

/* program of a slave (number = its stored 8-bit value) */
void Slave_Run(char number)
{
    char sum;
    SPI_SlaveTransceiver(number);   /* step (i)/(ii): send number, get dummy */
    sum = SPI_SlaveTransceiver(0);  /* step (iii): receive the sum */
    /* use sum ... */
}
```
