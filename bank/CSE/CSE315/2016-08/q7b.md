---
marks: 15
topics: [sleep-modes, external-interrupts]
kind: analysis
source: {page: 78-79}
note: "Printed as 'How ATmega32 can be waked up'."
---
Consider the following C program for ATmega32 microcontroller:

```c
#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/sleep.h>
#define MAX 60
volatile unsigned char sleepNow = 0;
unsigned char ovfCount = 0;
ISR(TIMER1_OVF_vect)
{
    if (ovfCount < MAX)
    {
        ovfCount++;
    }
    else
    {
        sleepNow = 1;
    }
}
ISR(INT0_vect)
{
}
int main(void)
{
    DDRD &= ~ ( 1 << PD2 ); // INT0: input ...
    PORTD |= ( 1 << PD2 ); // Enable pullup.
    // Level interrupt INT0 (low level)
    MCUCR &= ~ ( ( 1 << ISC01 ) | ( 1 << ISC00 ) );
    GICR = GICR | (1<<INT0);
    TCCR1A = 0b00000000; // normal mode
    TCCR1B = 0b00000001; // no prescaler, internal clock
    TIMSK = 0b00000100; // Enable Overflow Interrupt
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    sei();
    while (1)
    {
        cli();
        if (sleepNow == 1)
        {
            sleep_enable();
            sei();
            sleep_cpu();
            sleep_disable();
            sleepNow = 0;
            TCNT1 = 0;
        }
        sei();
    }
}
```

*Lines are numbered 1-47 in the paper: line 38 is `sleep_enable();`, line 39 is `sei();`, line 40 is `sleep_cpu();`.*

In this program, ATmega32 is placed into a sleep mode when a certain condition is met to reduce power consumption. Answer the following questions considering this program:

(i) When ATmega32 will be placed into sleep mode?

(ii) How ATmega32 can be waked up from this sleep mode?

(iii) What is the first thing done by ATmega32 after waking up from sleep?

(iv) Which clock domains ($clk_{I/O}$, $clk_{ADC}$, $clk_{CPU}$, $clk_{FLASH}$, $clk_{ASY}$) will be active during this sleep mode?

(v) What is the function of line 38 and 40? What is the effect of removing line 39 from the program?
