---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Vector = 1 followed by IR6'..IR0'; vector address = that of the highest-priority active input (order IR3, IR5, IR2, IR6, IR1, IR4, IR0). K = D9H, L = 13D2BH; M = 0101111, N = F3E4AH; O = BBH, P = 32E54H; Q = 1000101, R = 987B4H; S = ECH, T = 4C215H; U = 0111011, V = 32E54H."
sources: ["Brey, The Intel Microprocessors, Sec. 12-3 (expanding the interrupt structure with the 74ALS244; priority resolved by the vector table)"]
---
**Rules from the circuit and the first table**

- During $\overline{INTA}$ the 74ALS244 puts the IR lines on the data bus: D0 = $\overline{IR0}$, ..., D6 = $\overline{IR6}$, and D7 is pulled up to 1. So

$$\text{Vector} = 1\ \overline{IR6}\ \overline{IR5}\ \overline{IR4}\ \overline{IR3}\ \overline{IR2}\ \overline{IR1}\ \overline{IR0}$$

- An input is **active when it is 0**.
- For several active inputs, the table entry for that vector must hold the ISR address of the **highest-priority** active input. Priority: IR3 > IR5 > IR2 > IR6 > IR1 > IR4 > IR0.
- Single-input addresses: IR0 = 1F342H, IR1 = 4C215H, IR2 = 32E54H, IR3 = 987B4H, IR4 = C3E42H, IR5 = 13D2BH, IR6 = F3E4AH.

*Check with the given row:* 1110110 has IR3 and IR0 active, giving vector F6H; IR3 has the higher priority, so 987B4H. This matches the table.

**Solving each row**

| Row | IR6 ... IR0 | Vector | Active inputs | Highest priority | Vector address |
|:-:|:-:|:-:|:--|:-:|:-:|
| K, L | 1 0 1 1 0 0 1 | **K = D9H** (1101 1001) | IR5, IR2, IR1 | IR5 | **L = 13D2BH** |
| M, N | **M = 0 1 0 1 1 1 1** | AFH (1010 1111) | IR6, IR4 | IR6 | **N = F3E4AH** |
| O, P | 0 1 1 1 0 1 1 | **O = BBH** (1011 1011) | IR6, IR2 | IR2 | **P = 32E54H** |
| Q, R | **Q = 1 0 0 0 1 0 1** | C5H (1100 0101) | IR5, IR4, IR3, IR1 | IR3 | **R = 987B4H** |
| S, T | 1 1 0 1 1 0 0 | **S = ECH** (1110 1100) | IR4, IR1, IR0 | IR1 | **T = 4C215H** |
| U, V | **U = 0 1 1 1 0 1 1** | BBH (1011 1011) | IR6, IR2 | IR2 | **V = 32E54H** |

For the rows where the vector is given (M, Q, U), drop the leading 1 of the vector: AFH = 1|010 1111, so IR6...IR0 = 0101111; C5H = 1|100 0101, so 1000101; BBH = 1|011 1011, so 0111011 (the same pattern as row O, so V = P).

*Note:* all rows were checked with a short script that applies the priority order.
