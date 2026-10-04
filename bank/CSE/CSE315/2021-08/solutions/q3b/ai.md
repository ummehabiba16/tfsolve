---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Latch the edge in a D flip-flop: D = 1, CLK = device's INTR edge; the inverted output Q' drives the processor's active-low level INTR' and holds it low until the request is acknowledged; INTA (active high) is inverted and, together with RESET, drives the flip-flop's CLR', so INTR' returns high after acknowledgement."
sources: ["Brey, The Intel Microprocessors, Sec. 12-2 (converting an edge-triggered request into a level request with a D flip-flop cleared by INTA)"]
---
**Problem.** The device gives a short **edge** (assume a rising edge) on its INTR output. The processor's $\overline{INTR}$ is **level-sensitive and active low**: it must see a steady **low** level until it acknowledges the request with **INTA** (active high). A short pulse may be gone before the processor samples it, and must not cause a second interrupt afterwards.

**Circuit: D flip-flop (e.g. 74ALS74) as an edge-to-level converter**

```text
                Vcc
                 |
            +----+---------+
            |    D     Q   |---- (not used)
 Device ----|> CLK         |
 INTR       |         Q'   |--------------------> INTR' (processor, active-low level)
 (edge)     |   CLR'  PRE' |
            +----+-----+---+
                 |     |
                 |    Vcc
      +----------+
      |
     AND (active-low OR of the two clear sources)
     |  |
     |  +---- RESET' (system reset, active low)
     |
     +---[>o]---- INTA (processor, active high)
```

**Operation**

1. Idle: the flip-flop is clear, Q = 0, so **Q' = 1**: $\overline{INTR}$ inactive (high).
2. The device's rising edge clocks D = 1 into the flip-flop: Q = 1, **Q' = 0**. $\overline{INTR}$ goes **low and stays low**, even though the device's pulse has ended. The edge has been turned into a level.
3. The processor samples $\overline{INTR}$ low (interrupts enabled) and starts the acknowledge cycle: **INTA = 1**. The inverter makes CLR' = 0, which **clears** the flip-flop, so Q' = 1 and $\overline{INTR}$ returns high. The same request cannot be taken twice.
4. The next edge from the device sets the flip-flop again. RESET' also clears it at power-up, so no false request is pending after reset.

*Notes:* if the device's edge is falling, clock the flip-flop through an inverter. During INTA the vector number must still be put on the data bus (e.g. by a 74ALS244 or pull-up resistors), as for any INTR source.
