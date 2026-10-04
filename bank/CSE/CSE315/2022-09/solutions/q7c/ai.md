---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "3 = data becomes valid; 1 = STB_B' falls (data latched); 4 = IBF_B rises; 7 = STB_B' rises (transfer into the 8255 complete); 8 = INTR rises; 2 = data invalid; 6 = RD' falls; 5 = INTR falls; 9 = RD' rises (IBF then falls)."
sources: ["Brey, The Intel Microprocessors, Sec. 11-3 (82C55 mode 1 strobed input: STB, IBF, INTR, INTE)", "Hall, Microprocessors and Interfacing, Ch. 9 (8255 handshake input timing)"]
---
**Mode 1 strobed input sequence** (Port B)

1. The typewriter puts a byte on PB0-PB7 and pulses $\overline{STB_B}$ low.
2. $\overline{STB_B}$ low makes the 8255 latch the data and set **IBF_B** = 1 (input buffer full), which tells the typewriter not to send another byte.
3. When $\overline{STB_B}$ returns high (with IBF = 1 and INTE_B = 1), the 8255 raises **INTR**.
4. The CPU runs the ISR and reads the port: $\overline{RD}$ falling clears INTR; $\overline{RD}$ rising clears IBF_B, so the typewriter may send the next byte.

**Timing diagram with event IDs** (circled numbers shown as (n))

```text
                     (1)       (7)               (6)        (9)
STB'   ---------------+         +--------------------------------------
                      |_________|
                     (4)
IBF                   +---------------------------------------+
       _______________|                                       |________
                                  (8)             (5)
INTR                              +----------------+
       ___________________________|                |___________________
RD'    -------------------------------------------+          +---------
                                                  |__________|
DATA   ----------<=====================>-------------------------------
                (3)                   (2)
```

| ID | Event | Where on the diagram |
|:-:|:--|:--|
| 3 | Typewriter sends data to the port lines | DATA becomes valid, before $\overline{STB_B}$ falls |
| 1 | 8255 loads data into its input latch | $\overline{STB_B}$ falling edge |
| 4 | 8255 forbids the typewriter to send the next data | IBF_B rising (caused by $\overline{STB_B}$ low) |
| 7 | Data transfer (typewriter $\to$ 8255) complete | $\overline{STB_B}$ rising edge |
| 8 | 8255 informs the CPU by an interrupt | INTR rising (caused by $\overline{STB_B}$ rising) |
| 2 | Typewriter indicates data is no longer valid | DATA ends (after $\overline{STB_B}$ rises) |
| 6 | CPU starts reading the data | $\overline{RD}$ falling edge |
| 5 | 8255 prevents a second interrupt for the same data | INTR falling (caused by $\overline{RD}$ falling) |
| 9 | Read complete | $\overline{RD}$ rising edge (it then clears IBF_B) |

*Note:* event 7 could also be read as IBF_B falling at the end of the read (the whole byte has reached the CPU and the 8255 is ready for the next one). The rising edge of $\overline{STB_B}$ is used here because it ends the typewriter's transfer and is what triggers INTR (event 8).
