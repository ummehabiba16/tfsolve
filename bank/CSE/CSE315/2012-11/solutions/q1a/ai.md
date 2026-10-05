---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "S to INT0 (PD2, rising edge), T to ADC0 (PA0, ADC interrupt; alarm if ADC > 614, i.e. 60 C = 3 V), stop switch to INT1 (PD3, falling edge, pull-up), buzzer on PB0, start signal to the fire-fighting system on PB1, Timer1 interrupt for the 1-minute timeout. Flowchart: main sets up and sleeps; INT0 ISR starts ADC; ADC ISR checks 60 C and starts buzzer + timer; INT1 ISR stops buzzer and timer; timer ISR after 60 s raises the start signal."
sources: ["EHP ATmega32 Interrupt slides 13-23 (external interrupts)", "EHP 6. AVR ADC slides 16-36 (ADC with interrupt)", "EHP Timer_Part_1 slides 25-27 (overflow interrupt for long delays)"]
---
**(i) Block diagram**

```text
                             ATmega16/32
                     +---------------------------+
 Smoke sensor S ---->| PD2 / INT0                |
 (0 V / 5 V)         |                    PB0    |---> driver ---> Buzzer
 Temp sensor T ----->| PA0 / ADC0                |
 (0-5 V = 0-100 C)   |                    PB1    |---> START to automated
 Stop switch ------->| PD3 / INT1                |     fire-fighting system
 (to GND, pull-up)   | AVCC = AREF = +5 V        |
 +5 V, GND --------->| VCC, GND                  |
                     | Timer1 (internal): 1 min  |
                     +---------------------------+
```

- **S** is digital, so it goes to **INT0** (rising edge = smoke detected): no polling.
- **T** is analog, so it goes to **ADC0**; the conversion is started only after smoke is detected and finishes with an **ADC interrupt**. Threshold: 60 °C = $60/100 \times 5 = 3$ V, so $ADC = 3 \times 1024/5 = 614.4$; alarm if **ADC > 614**.
- **Stop switch** on **INT1** (falling edge).
- **Timer1** (e.g. 1 s CTC or overflow interrupt, counted to 60) measures 1 minute after the buzzer starts.
- **Buzzer** on **PB0**, **start signal** to the fire-fighting system on **PB1**.

**(ii) Flowchart**

```text
 MAIN                         INT0 ISR (smoke)            ADC ISR (temperature ready)
 +----------------------+     +---------------------+     +-------------------------------+
 | ports, INT0 rising,  |     | start ADC conversion|     | T = ADC                       |
 | INT1 falling, ADC +  |     | (ADSC = 1)          |     | T > 614 and smoke still on?   |
 | interrupt, Timer1,   |     +---------------------+     |   yes: buzzer ON (PB0 = 1),   |
 | sei()                |                                 |        seconds = 0, start     |
 +----------+-----------+                                 |        Timer1                 |
            v                                             |   no: if smoke still on,      |
 +----------------------+                                 |       start next conversion   |
 | sleep / idle loop    |<-+                              +-------------------------------+
 +----------+-----------+  |
            +--------------+

 INT1 ISR (stop switch)        TIMER1 ISR (every 1 s)
 +-------------------------+   +-----------------------------------------+
 | buzzer OFF (PB0 = 0)    |   | seconds = seconds + 1                   |
 | stop Timer1             |   | seconds = 60 ?                          |
 +-------------------------+   |   yes: START signal ON (PB1 = 1),       |
                               |        stop Timer1                      |
                               |   no:  return                           |
                               +-----------------------------------------+
```

*Assumptions:* 5 V reference, active-high buzzer driver and start input, a switch to ground with the internal pull-up for "stop".
