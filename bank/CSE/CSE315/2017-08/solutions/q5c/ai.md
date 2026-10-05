---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Connect MOSI, MISO and SCK of the ATmega32 (master) to all three slaves in parallel and give each slave its own SS' line from a master output pin (e.g. PB4, PB3, PB2). To send to A: SS_A low, write SPDR, wait for SPIF, SS_A high; then the same with SS_B and SS_C. Only the selected slave listens; the others ignore SCK and keep MISO tri-stated."
sources: ["EHP Serial Communication slides 84-92, 108 (master-slave connection, slave select, transmission steps, multiple slaves)"]
---
**Connection (independent slaves)**

```text
 ATmega32 (master)      Device A      Device B      Device C
 MOSI (PB5)  ---------> MOSI          MOSI          MOSI     <- one shared line
 MISO (PB6)  <--------- MISO          MISO          MISO     <- one shared line
 SCK  (PB7)  ---------> SCK           SCK           SCK      <- one shared line
 PB4  (SS_A) ---------> SS'
 PB3  (SS_B) ---------------------->  SS'
 PB2  (SS_C) ------------------------------------>  SS'
```

- **MOSI, MISO, SCK** are shared by all three devices.
- Each device has its **own slave-select** line, driven by a separate output pin of the master (PB4 = SS, plus any two free port pins).

**Sending to A, B and C one after another**

1. Configure the ATmega32 as master: MOSI, SCK and the three SS pins as outputs; all SS lines high (no device selected); `SPCR = (1<<SPE)|(1<<MSTR)|(1<<SPR0)`.
2. Pull **SS_A low**, write the byte to **SPDR**, wait for **SPIF**, pull SS_A high.
3. Do the same with **SS_B**, then with **SS_C**.

```c
void spi_send_to(uint8_t ss_pin, uint8_t data) {
    PORTB &= ~(1 << ss_pin);           // select this device
    SPDR = data;                       // start transfer
    while (!(SPSR & (1 << SPIF)));     // wait until done
    PORTB |=  (1 << ss_pin);           // deselect
}
// spi_send_to(PB4, a); spi_send_to(PB3, b); spi_send_to(PB2, c);
```

Only the device whose SS' is low shifts in the data; the others ignore SCK and keep their MISO in high impedance, so there is no conflict. (A daisy chain with one SS line is an alternative when the devices support it.)
