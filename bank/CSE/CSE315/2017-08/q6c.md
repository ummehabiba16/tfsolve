---
marks: 10
topics: [ppi-8255, transfer-modes]
kind: diagram
source: {page: 72}
---
Consider you are reading a tape recorder with an 8088 microcomputer system with a built-in 8255 PPI (e.g., MTS-88.C). The tape recorder is connected to PORTA and it is read using strobed I/O mode. You also have an output device connected to PORTB which works in simple I/O mode. You will have to design a flowchart to continuously read data from the tape and output it to PORTB. The 8255 is connected with the 8088 microprocessor in the address 010000xxb. Clearly specify the control word.
