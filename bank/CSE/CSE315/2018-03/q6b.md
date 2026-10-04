---
marks: 10
topics: [timer-input-capture, lcd]
kind: code
source: {page: 68}
---
Write C program to be written in an ATmega32 so that it determines the time period of a uniform square waveform and shows the time period in seconds on LCD. Assume that the LCD is connected to the ATmega according to the requirements of the header "LCD.h".

Note that ICNC = 1 activates the noise canceller, ICES = 0 selects the falling edge as the input capture event generator, and WGM = 0000 makes the timer operate in normal mode. Clock select "001" makes the timer operate without any prescaling.

*Section B note: a header "LCD.h" is assumed; call `LCD_init()` to initialize the LCD and `LCD_string(str)` to show a string. The ATmega32 runs at 1 MHz unless specified otherwise.*

Attached sheet: [Table 1 (register descriptions) and Figure 1 (ATmega32 pin diagram)](figures/sheet-1.png).
