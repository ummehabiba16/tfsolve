---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Master: select Q, read a; select R, read b; sum = a + b (8-bit); send sum to Q, then to R, each with SS low around the transfer."
sources: ["EHP Serial Communication slides 91-92, 104-108 (transmission steps, multiple slaves)"]
---
```c
int main(void)
{
    char a, b, sum;

    SPI_MasterInit();

    /* (i) receive the 8-bit number from Q (send a dummy byte) */
    SPI_Select(PB4);
    a = SPI_Transceiver(0x00);
    SPI_Deselect(PB4);

    /* (ii) receive the 8-bit number from R */
    SPI_Select(PB3);
    b = SPI_Transceiver(0x00);
    SPI_Deselect(PB3);

    /* (iii) 8-bit sum, sent to both Q and R */
    sum = a + b;                    /* char arithmetic: sum mod 256 */

    SPI_Select(PB4);
    SPI_Transceiver(sum);
    SPI_Deselect(PB4);

    SPI_Select(PB3);
    SPI_Transceiver(sum);
    SPI_Deselect(PB3);

    while(1);
}
```

Each slave must already have loaded its number into SPDR (`Slave_Run` in (c)) before the master starts clocking. The master may wait a short time after pulling $\overline{SS}$ low before writing SPDR.
