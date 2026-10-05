---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) Pull-up resistors on D7-D0: during INTA nothing drives the bus, so the CPU always reads FFH. (ii) A 74ALS244 with inputs wired to 1000 0000 and its enables driven by INTA': it puts 80H on the bus only during INTA, high impedance otherwise. (iii) Feed several active-low IR lines into the '244 inputs (D7 pulled high) and a NAND gate to INTR, giving a different vector per request; or use the 8259A PIC (8 vectors each, cascadable to 64)."
sources: ["Brey, The Intel Microprocessors, Sec. 12-2 and 12-3 (INTR and INTA; pull-up resistors for vector FFH; 74ALS244 vector; expanding the interrupt structure; 8259A)"]
---
During the interrupt acknowledge ($\overline{INTA}$) cycle the 8086 reads the **interrupt type number** from D7-D0.

**(i) Always a fixed vector, e.g. FFH**

Connect **pull-up resistors** (e.g. 4.7 k$\Omega$) from each of D7-D0 to +5 V. During $\overline{INTA}$ no device drives the data bus, so the resistors pull every line high and the CPU reads **1111 1111 = FFH**. The ISR address is stored at $4 \times FFH = 3FCH$. At other times the resistors are weak, so normal bus devices simply override them.

```text
 +5V -- R -- D7     ...     +5V -- R -- D0      (vector = FFH)
```

**(ii) A fixed vector (e.g. 80H) only when needed, high impedance otherwise**

Use a **74ALS244 three-state buffer**: wire its inputs to the vector **1000 0000** (A for D7 to +5 V, the rest to ground) and connect both enables $\overline{1G}$, $\overline{2G}$ to $\overline{INTA}$.

```text
          +5V  GND GND GND GND GND GND GND
           |    |   |   |   |   |   |   |
         +-A----A---A---A---A---A---A---A-+
         |           74ALS244             |
 INTA' --| 1G', 2G'                       |
         +-Y----Y---Y---Y---Y---Y---Y---Y-+
           D7   D6  D5  D4  D3  D2  D1  D0     (80H only during INTA)
```

When $\overline{INTA}$ = 0 the buffer drives **80H** onto the bus; when $\overline{INTA}$ = 1 its outputs are in the **high-impedance** state, so it does not disturb normal memory/I/O transfers.

**(iii) Expanding the number of vectors**

Connect up to 7 active-low request lines $\overline{IR0}$-$\overline{IR6}$ (each with a pull-up) to the '244 inputs A1-A7 (D0-D6), tie the D7 input high, and feed all IR lines to a **NAND gate** (74ALS30) whose output drives INTR. Any active request raises INTR, and during $\overline{INTA}$ the buffer places a vector that depends on which line is low (IR0 = FEH, IR1 = FDH, ..., IR6 = BFH). Simultaneous requests give other vectors, so priority is resolved in the vector table.

A better way is the **8259A Programmable Interrupt Controller**: 8 requests per chip with programmable priority and masking, 8 consecutive vectors, and up to 9 chips cascaded for **64** interrupt inputs.
