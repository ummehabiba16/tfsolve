---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "After the data (and parity) bits the receiver samples the stop bit 16 times (8 in double speed) and takes a majority vote of the three middle samples (8, 9, 10); a 0 sets FE. Only the first stop bit is checked; a new start bit can be detected right after the voting samples."
sources: ["EHP Serial Communication slides 60-62, 71-77 (reception, frame error, clock and data recovery, majority voting on the stop bit)"]
---
**Stop bit detection in the USART receiver**

1. **Start-bit synchronization.** The receiver samples RxD at 16 times the baud rate (8 times in double-speed mode). A high-to-low transition starts the start-bit check; samples 8, 9, 10 must be low (majority) for a valid start bit. This aligns the receiver's sampling with the incoming frame.
2. **Data and parity bits.** Each following bit is sampled 16 times, and its value is the **majority vote of the three centre samples** (8, 9, 10; or 4, 5, 6 in double speed).
3. **Stop bit.** After the last data bit (and parity bit, if used), the next bit time is the **stop bit**. It is sampled the same way: majority of the three centre samples.
   - If the majority is **1**: valid stop bit. The complete frame is moved from the shift register into the receive buffer (UDR) and **RXC** is set.
   - If the majority is **0**: the stop bit is missing (wrong baud rate, noise, or wrong frame format), so the **Frame Error flag FE** is set for that character.
4. Only the **first stop bit** is checked. If two stop bits are used, the receiver ignores the second one.
5. For quick resynchronization, the receiver can detect the **start bit of the next frame** right after the samples used for the stop-bit vote, without waiting for the end of the stop bit.

```text
 RxD  ... | D7 | (P) |  stop bit (should be 1)  | next start
 samples          1 2 3 4 5 6 7 [8 9 10] ...
                              majority -> 1: OK, 0: FE = 1
```
