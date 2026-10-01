---
marks: 10
topics: [segmentation-8086, instruction-encoding]
kind: numerical
source: {page: 4}
note: "The '(b)' label and the marks (10) are handwritten in the margin of the scan."
---
In an 8086 microprocessor, **CS = 2000H, IP = 0954H, DS = 3000H, BX = 00FEH**

| Memory Address (in hex) | 200F8 | 200F9 | 200FA | 200FB | 200FC | 200FD | 200FE | 200FF |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Values (in hex) | 12 | 34 | 56 | 78 | 90 | AB | CD | EF |

| Memory Address (in hex) | 300F8 | 300F9 | 300FA | 300FB | 300FC | 300FD | 300FE | 300FF |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Values (in hex) | FE | DC | BA | 09 | 87 | 65 | 43 | 21 |

Calculate the next instruction's physical address if currently executing instruction is: **JMP [BX]**
