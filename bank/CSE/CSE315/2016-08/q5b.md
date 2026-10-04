---
marks: 20
topics: [usart]
kind: code
source: {page: 76}
---
Suppose, MCAM100 is a programmable pan-tilt video camera. It can be controlled using UART (Universal Asynchronous Serial Receiver & Transmitter). You have to use USART of Atmega32 microcontroller to rotate the camera repeatedly. The required connection parameters are: 8 data bit (code: 011), 1 stop bit (code: 0), no parity bit (code: 00), baud rate 9600 bps and asynchronous mode (code: 0). Sending character 'L' or 'R' will turn the camera left or right respectively. Assume the system clock frequency of ATmega32 is 1 MHz. Now answer the following questions:

(i) Calculate the appropriate value for UBRR (USART Baud Rate Register).

(ii) Write a C function named USART_init which initializes ATmega32 USART for the given parameters.

(iii) Write a C function named USART_send which sends a character through ATmega32 USART using polling.

(iv) Write the main function which continuously does the following things:

a. Rotate the camera left for 5 times. Give 500 milliseconds delay between each successive left rotation.

b. Rotate the camera right for 5 times. Give 200 milliseconds delay between each successive right rotation.

**Registers (from Table 1)**

| Register | Bit 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| UCSRA | RXC | TXC | UDRE | FE | DOR | PE | U2X | MPCM |
| UCSRB | RXCIE | TXCIE | UDRIE | RXEN | TXEN | UCSZ2 | RXB8 | TXB8 |
| UCSRC | URSEL | UMSEL | UPM1 | UPM0 | USBS | UCSZ1 | UCSZ0 | UCPOL |
