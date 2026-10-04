---
marks: 15
topics: [usart]
kind: code
source: {page: 84}
note: "Part (i) is printed as 'Calculate the baud rate' (the UBRR value is presumably meant); (iv) refers to 'steps a to c' for (i)-(iii)."
---
Consider, you are continuously receiving data from a PC using UART in polling approach. The connection details are: Baud rate: 4800 bps, no parity, 1 stop bit (code: 0), 8 data bits (code: 011), and asynchronous communication (code: 0). Assume a clock speed of 4 MHz. (3+3+6+3=15)

(i) Calculate the baud rate.

(ii) Initialize ATmega32 for the given parameters.

(iii) Write a C code that continuously receives a word from the PC, write that word to PORTA, and sleeps for 2 seconds and repeats again.

(iv) If double speed transmission mode is used, what changes are needed to be made in steps a to c?

Attached sheet: [ATmega32 pinout and list of registers](figures/sheet-1.png).
