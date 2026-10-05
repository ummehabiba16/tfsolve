---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "MCU0 = SPI master: every 2 s reads S1 (ADC0) and S2 (ADC1), left adjusted (8-bit ADCH); pulls PB4 (SS of MCU1) low and sends the S1 byte, then PB3 (SS of MCU2) low and sends the S2 byte. MCU1 and MCU2 = SPI slaves: wait for SPIF, read SPDR, format the number and call LCD_string()."
sources: ["EHP Serial Communication slides 79-108 (SPI pins, SPCR/SPSR/SPDR, master/slave init, transmit/receive, multiple slaves)", "EHP 6. AVR ADC slides 20-33 (ADMUX, ADCSRA, polling)"]
---
**Connections**

```text
 MCU0 (master)                 MCU1 (slave)        MCU2 (slave)
 PB5 MOSI ------------------->  PB5 MOSI   +----->  PB5 MOSI
 PB7 SCK  ------------------->  PB7 SCK    +----->  PB7 SCK
 PB6 MISO <------------------   PB6 MISO   +-----   PB6 MISO  (not used)
 PB4 (SS1, output) ---------->  PB4 SS'
 PB3 (SS2, output) ------------------------------>  PB4 SS'
 PA0 (ADC0) <- S1, PA1 (ADC1) <- S2        LCD on MCU1 and MCU2 (LCD.h)
```

Assumptions: 1 MHz clock, AVCC = 5 V reference, 8-bit results (ADLAR = 1, read ADCH), SPI clock = fosc/16, mode 0, MSB first.

**MCU0 (master)**

```c
#define F_CPU 1000000UL
#include <avr/io.h>
#include <util/delay.h>

uint8_t read_adc(uint8_t ch)
{
    ADMUX = 0b01100000 | ch;             // AVCC ref, left adjust, channel ch
    ADCSRA |= (1 << ADSC);               // start
    while (!(ADCSRA & (1 << ADIF)));     // poll
    ADCSRA |= (1 << ADIF);               // clear flag
    return ADCH;                         // 8-bit reading
}

void spi_send(uint8_t data)
{
    SPDR = data;                         // start transmission
    while (!(SPSR & (1 << SPIF)));       // wait until done
}

int main(void)
{
    uint8_t s1, s2;
    DDRB = (1 << PB5) | (1 << PB7) | (1 << PB4) | (1 << PB3);   // MOSI, SCK, SS1, SS2 out
    PORTB |= (1 << PB4) | (1 << PB3);    // both slaves deselected
    SPCR = (1 << SPE) | (1 << MSTR) | (1 << SPR0);              // enable, master, fosc/16
    ADCSRA = 0b10000011;                 // ADC on, prescaler 8

    while (1) {
        s1 = read_adc(0);                // sensor S1
        s2 = read_adc(1);                // sensor S2

        PORTB &= ~(1 << PB4);            // select MCU1
        spi_send(s1);
        PORTB |=  (1 << PB4);            // deselect

        PORTB &= ~(1 << PB3);            // select MCU2
        spi_send(s2);
        PORTB |=  (1 << PB3);

        _delay_ms(2000);                 // every 2 seconds
    }
}
```

**MCU1 and MCU2 (slaves, the same program)**

```c
#include <avr/io.h>
#include <stdio.h>
#include "LCD.h"

int main(void)
{
    uint8_t data;
    char buf[16];

    DDRB = (1 << PB6);                   // MISO output, others input
    SPCR = (1 << SPE);                   // enable SPI, slave mode
    LCD_init();

    while (1) {
        while (!(SPSR & (1 << SPIF)));   // wait for a byte from MCU0
        data = SPDR;
        sprintf(buf, "Sensor: %3u", data);
        LCD_string(buf);                 // show the reading
    }
}
```

MCU1 shows the S1 reading and MCU2 the S2 reading, because MCU0 selects only one slave (its SS' low) for each byte; the other slave ignores the clock while its SS' is high.
