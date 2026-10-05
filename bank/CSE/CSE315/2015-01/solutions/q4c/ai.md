---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "RS-232 uses different, inverted voltage levels (logic 1 = -3 to -25 V, logic 0 = +3 to +25 V) from the ATmega's TTL/CMOS levels (0 V and 5 V), so they cannot be connected directly (wrong logic and possible damage). Solution: a line driver/receiver level converter such as the MAX232 (single 5 V supply with charge-pump capacitors) between TxD/RxD and the RS-232 lines."
sources: ["EHP Serial Communication slides (USART pins, RS-232)", "Mazidi, AVR Microcontroller and Embedded Systems, Ch. 11 (RS232 voltage levels, MAX232)"]
---
**Problem: voltage levels.** RS-232 was defined long before TTL logic and uses **different, inverted, bipolar levels**:

| | RS-232 | ATmega16 (TTL/CMOS, 5 V) |
|:--|:--|:--|
| Logic 1 (mark) | **-3 V to -25 V** | about +5 V |
| Logic 0 (space) | **+3 V to +25 V** | about 0 V |

So the ATmega's TxD (0/5 V) is not a valid RS-232 signal, and an RS-232 line (e.g. $\pm$12 V) connected directly to RxD would give the wrong logic and could **damage** the microcontroller.

**Solution: a level converter (line driver/receiver)** such as the **MAX232** (or MAX233). It runs from a single +5 V supply, uses charge-pump capacitors to make about $\pm$10 V, converts the ATmega's TxD (TTL) into RS-232 levels for the PC, and converts the PC's RS-232 signal back to TTL for RxD (inverting as required).

```text
 ATmega16 TxD (PD1) --> T1in  MAX232  T1out --> RS-232 RxD (DB-9 pin 2)
 ATmega16 RxD (PD0) <-- R1out MAX232  R1in  <-- RS-232 TxD (DB-9 pin 3)
                         (+ 4 charge-pump capacitors, common GND)
```
