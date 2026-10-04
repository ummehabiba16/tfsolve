---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) INTR is level-sensitive: it is sampled only at the end of each instruction (and only if IF = 1) and must stay high until INTA; a short edge/pulse from the alarm can disappear before it is sampled, and the alarm gives no vector. (ii) Latch the edge in a D flip-flop (D = 1, CLK = alarm, Q -> INTR) that is cleared by INTA' (and RESET); put a vector on the data bus during INTA."
sources: ["Brey, The Intel Microprocessors, Sec. 12-2 (INTR is level-sensitive; converting INTR to an edge-triggered input with a D flip-flop)", "MHE 8086 Hardware Specifications slide 12 (INTR held high, INTA)"]
---
**i. The problem**

- The 8086's **INTR is level-sensitive**, not edge-triggered. The CPU samples INTR only during the **last clock cycle of each instruction**, and only if IF = 1. The request must stay at logic 1 **until it is acknowledged** by $\overline{INTA}$.
- The alarm gives an **edge** (a short pulse). If the pulse is over before INTR is sampled (during a long instruction such as MUL/DIV, or while IF = 0 inside another ISR), the interrupt is **simply lost**. If the alarm output instead stays high, the same interrupt is recognized again and again.
- During $\overline{INTA}$ the 8086 reads an **interrupt type number** from the data bus. The alarm does not provide one, so the CPU would read an undefined vector.

**ii. The solution**

Store the edge in a **D flip-flop** (e.g. 74ALS74) and use its Q output as INTR:

```text
                 +5 V
                  |
                +-+---------+
                | D       Q |----------------> INTR (8086)
  Alarm ------->|> CLK      |
  (edge)        |    CLR'   |
                +-----+-----+
                      |
   INTA' ----+        |
             AND -----+      (CLR' = 0 when INTA' = 0 or RESET' = 0)
  RESET' ----+

   During INTA': data bus D7-D0 pulled up (or a 74ALS244) -> vector, e.g. FFh
```

1. The rising edge from the alarm clocks a 1 into the flip-flop, so **Q = INTR = 1 and stays 1**, even after the alarm pulse ends.
2. When the 8086 accepts the interrupt it pulses $\overline{INTA}$. This **clears** the flip-flop, so INTR returns to 0 and the request is not taken twice. RESET also clears it at power-up.
3. During $\overline{INTA}$ a vector number is placed on D7-D0: with pull-up resistors on the data bus the CPU reads **FFh** (type 255), or a 74ALS244 can supply any chosen type. The ISR address is stored at $4 \times$ type in the vector table.

Now every alarm edge produces exactly one interrupt, no matter when it arrives.
