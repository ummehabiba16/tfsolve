---
marks: 15
topics: [timer-pwm]
kind: diagram
source: {page: 67-68}
note: "Printed as 'as followa'."
---
A PWM wave generation in ATmega32 is using **Phase Correct PWM** with **Non-inverting mode**. Specially, the bits chosen are WGM = 1010 and COM1A = 10. In these settings, TOP = ICR1 and compare match event occurs at OCR1A.

Now, the TOP is not fixed in this scenario. The TOP is updated in runtime as followa:

```c
// register set ups
OCR1A = 100;
while (1)
{
    for (i = 0; i < 5; i++)
    {
        ICR1 = 200 + 100 * i;
        _delay_us(400);
    }
}
```

***_delay_us()*** gives delay in microseconds. Here, no prescaler has been used.

Now, draw the generated waveform and determine its frequency and duty cycle.

*Section B note: a header "LCD.h" is assumed; call `LCD_init()` to initialize the LCD and `LCD_string(str)` to show a string. The ATmega32 runs at 1 MHz unless specified otherwise.*
