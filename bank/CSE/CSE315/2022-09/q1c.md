---
marks: 15
topics: [adc-registers, external-interrupts]
kind: code
source: {page: 33}
---
Suppose you are to design a Fire Alarm System. There is a smoke sensor (S) and a temperature sensor (T) connected to ATmega32. The S sensor provides 0V if there is no smoke and jumps to 5V when it detects any smoke. The T sensor provides voltage in the range of 0V to 5V in proportional to the temperature between 0°C to 100°C.

If there is smoke and the temperature is above 70°C, you are to light up an LED connected to the ATmega32.

i) Draw a circuit diagram showing the connection among S, T, LED and ATmega32

ii) Write a C code for the system

Your system should avoid unnecessary computation to be energy efficient.
