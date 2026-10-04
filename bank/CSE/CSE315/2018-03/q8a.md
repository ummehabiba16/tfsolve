---
marks: 20
topics: [spi, adc-registers, lcd]
kind: code
source: {page: 68}
---
Two sensors S1 and S2 are connected to an ATmega32, namely MCU0. The microcontroller MCU0 is responsible for reading the sensors and collecting sensor data every 2 seconds. However, MCU0 does not have any LCD connected to it. MCU1 and MCU2 (two other ATmega32's) have two LCD displays connected to them, as described in "LCD.h".

Now, write three programs to be written in MCU0, MCU1 and MCU2 so that MCU0 collects the sensor data and sends the data to MCU1 and MCU2. Readings(s) collected from S1 is sent to MCU1; and reading(s) collected from S2 is sent to MCU2. This data transfer is done in SPI. MCU0 selects which MCU to send the data to, and next sends the data. MCU1 and MCU2, after receiving, show the received data on LCD display. Assume that the LCD displays are connected to MCU1 and MCU2 as described in "LCD.h".

You can use any clock for SPI. You can choose the ADC to be left or right adjusted; either of these two is fine.

*Section B note: a header "LCD.h" is assumed; call `LCD_init()` to initialize the LCD and `LCD_string(str)` to show a string. The ATmega32 runs at 1 MHz unless specified otherwise.*

Attached sheet: [Table 1 (register descriptions) and Figure 1 (ATmega32 pin diagram)](figures/sheet-1.png).
