---
marks: 7
topics: [privilege-protection, registers-flags]
kind: analysis
mandatory: true
source: {page: 14}
---
Suppose in an 80286 microprocessor the flag register currently holds the following value:

0101 1110 0101 0101. Now three I/O devices request for the same I/O port simultaneously. Device 1 has the privilege level bits set as 11, Device 2 has the privilege level bits set as 00, Device 3 has the privilege level bits set as 10. Now, with the help of the following figure 1(c), evaluate the device requests and conclude which device will get the access of the specified I/O port.

| Bit | D15 | D14 | D13 D12 | D11 | D10 | D9 | D8 | D7 | D6 | D5 | D4 | D3 | D2 | D1 | D0 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Flag | -- | NT | IOPL | OF | DF | IF | TF | SF | ZF | -- | AF | -- | PF | -- | CF |

*Figure 1(c): the 80286 flag register; "--" marks the shaded (unused) bits.*
