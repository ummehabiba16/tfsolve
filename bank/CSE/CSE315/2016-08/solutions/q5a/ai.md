---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) TWI (I2C): all four devices share just two wires, SDA and SCL. (ii) Every device must support TWI/I2C and have a unique 7-bit address (max 128 devices); SDA and SCL need pull-up resistors (open-drain bus); common ground and compatible voltage/speed; total bus capacitance within 400 pF. (iii) ATmega32 PC1 (SDA, pin 23) and PC0 (SCL, pin 22) to SDA/SCL of all four devices, with pull-ups to Vcc."
sources: ["EHP Serial Communication slides 9, 14-16 (TWI: two-wire bus, 7-bit address, up to 128 devices, sample network)"]
---
**(i) Protocol.** **TWI (Two-wire Serial Interface, Atmel's version of I2C).** It needs only **two wires** for any number of devices: **SDA** (serial data) and **SCL** (serial clock). UART would need a separate link per device, and SPI needs MOSI, MISO, SCK plus one select line per device.

**(ii) Preconditions**

1. All four devices must have a **TWI/I2C interface**.
2. Each device must have a **unique 7-bit address** on the bus (at most 128 addresses); the master selects a device by sending its address.
3. SDA and SCL are **open-drain/open-collector** lines, so each needs one **pull-up resistor** to Vcc (e.g. 4.7 k$\Omega$).
4. All devices share a **common ground** and compatible logic voltage levels, and they must support the chosen bit rate (e.g. 100 kHz or 400 kHz).
5. The bus must be short enough that its capacitance stays within the limit (400 pF).

**(iii) Connections**

```text
                  Vcc   Vcc
                   |     |
                  [Rp]  [Rp]      pull-up resistors (e.g. 4.7 k)
                   |     |
 ATmega32          |     |
 PC1 (SDA) --------+-----|-------+----------+----------+----------+
 PC0 (SCL) --------------+---+---|------+---|------+---|------+---|
                             |   |      |   |      |   |      |   |
                            SCL SDA    SCL SDA    SCL SDA    SCL SDA
                            Device 1   Device 2   Device 3   Device 4
                            (addr 1)   (addr 2)   (addr 3)   (addr 4)
 GND: common to all devices
```

The ATmega32 (master) drives SCL and addresses each device in turn over the same two wires.
