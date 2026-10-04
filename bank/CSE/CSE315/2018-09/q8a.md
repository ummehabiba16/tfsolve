---
marks: 15
topics: [adc-registers]
kind: code
source: {page: 63}
note: "Printed as 'prescalar'."
---
You need to write a C code for an ATmega32/16 based system to control temperature of a medicine storage facility. The facility requires the room temperature to be within 4-10 degree Celsius. If the temperature falls below the range, it should be increased by turning on the heater and when the temperature exceeds the range, the room needs to be cooled down by turning on the air cooler. Both the heater and air cooler stay off while temperature is within the desired range. A temperature sensor is used to measure the temperature of the room.

The output voltage of the temperature sensor is linearly proportional to the temperature and produces an output of 0V to 5.0 V for 0 degree to 20 degree Celsius linearly. Assume that you are using polling mode, reference voltage of 5 V (code: 0x1) and a prescalar of 2 (code:0x1). The sensor is connected to the pin ADC0 (code:0x0). You can turn on the heater and air cooler by writing a logic 1 to PB0 and PB1, respectively. Each time you turn on the heater or the air cooler, wait for 20 seconds before taking a new reading from temperature sensor.

**Registers (from the attached list)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| ADMUX | REFS1 | REFS0 | ADLAR | MUX4 | MUX3 | MUX2 | MUX1 | MUX0 |
| ADCSRA | ADEN | ADSC | ADATE | ADIF | ADIE | ADPS2 | ADPS1 | ADPS0 |

Attached sheet: [ATmega32 pinout and list of registers](figures/sheet-1.png).
