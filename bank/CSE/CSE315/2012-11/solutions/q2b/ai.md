---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "ICP1 (PD6) -> optional noise canceller (ICNC1: 4 equal samples) -> edge detector (ICES1: rising or falling) -> on the selected edge the current TCNT1 is copied into ICR1 and ICF1 is set (interrupt TIMER1_CAPT_vect if TICIE1 = 1); the analog comparator output can be selected as the source instead (ACIC). Software takes the difference of two ICR1 values (plus overflows) to get period or pulse width."
sources: ["EHP Timer_Part_1 slides 11, 33-37 (input capture: ICP1, ICR1, period measurement)", "ATmega32 datasheet, Timer/Counter1 Input Capture Unit (block diagram)"]
---
**Block diagram**

```text
 ICP1 (PD6) ------------+
                        +--> [ MUX ]  (ACIC selects the source)
 analog comparator ACO -+       |
                                v
                     [ noise canceller ]   (enabled by ICNC1)
                                |
                                v
                     [ edge detector ]     (ICES1: 1 = rising, 0 = falling)
                                |
              +-----------------+------------------+
              v                                    v
   copy TCNT1 --> ICR1 (16-bit)          set ICF1 in TIFR --> TIMER1_CAPT
   (read ICR1L, then ICR1H)                                   interrupt if TICIE1 = 1
```

**Operation (external input on ICP1)**

1. The signal enters on **ICP1 (PD6)**. (ACIC = 1 would select the analog comparator output instead.)
2. If **ICNC1 = 1**, the **noise canceller** accepts a level change only after 4 equal successive samples, filtering spikes (adds a 4-clock delay).
3. The **edge detector** looks for the edge selected by **ICES1** (1 = rising, 0 = falling).
4. When that edge occurs, the hardware **copies the current TCNT1 value into ICR1** (the capture) and sets the **ICF1** flag. If **TICIE1** = 1 and interrupts are enabled, the **input capture interrupt** runs.
5. In the ISR the program reads ICR1 (the time of the edge). The difference between two captures, plus 65536 for each overflow in between, gives the **period** (same edge) or **pulse width** (alternate edges by toggling ICES1). Because the capture is done in hardware, the time stamp is exact even if the ISR starts late.
