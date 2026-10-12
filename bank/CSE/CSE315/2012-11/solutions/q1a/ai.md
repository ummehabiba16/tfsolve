---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "S to INT0 (PD2, rising edge), T to ADC0 (PA0, ADC interrupt; alarm if ADC > 614, i.e. 60 C = 3 V), stop switch to INT1 (PD3, falling edge, pull-up), buzzer on PB0, start signal to the fire-fighting system on PB1, Timer1 interrupt for the 1-minute timeout. Flowchart: main sets up and sleeps; INT0 ISR starts ADC; ADC ISR checks 60 C and starts buzzer + timer; INT1 ISR stops buzzer and timer; timer ISR after 60 s raises the start signal."
sources: ["EHP ATmega32 Interrupt slides 13-23 (external interrupts)", "EHP 6. AVR ADC slides 16-36 (ADC with interrupt)", "EHP Timer_Part_1 slides 25-27 (overflow interrupt for long delays)"]
changes:
  - "2026-10-12: replaced the two ASCII sketches by a TikZ block diagram and TikZ flowcharts (answer unchanged)"
---
**(i) Block diagram**

![Fire control system: S on INT0, T on ADC0, stop switch on INT1, buzzer on PB0, start signal on PB1](figures/block.png)

- **S** is digital, so it goes to **INT0** (rising edge = smoke detected): no polling.
- **T** is analog, so it goes to **ADC0**; the conversion is started only after smoke is detected and finishes with an **ADC interrupt**. Threshold: 60 °C = $60/100 \times 5 = 3$ V, so $ADC = 3 \times 1024/5 = 614.4$; alarm if **ADC > 614**.
- **Stop switch** on **INT1** (falling edge).
- **Timer1** (e.g. 1 s CTC or overflow interrupt, counted to 60) measures 1 minute after the buzzer starts.
- **Buzzer** on **PB0**, **start signal** to the fire-fighting system on **PB1**.

**(ii) Flowchart**

![Flowcharts: main program and the INT0, ADC, INT1 and Timer1 ISRs](figures/flow.png)

*Assumptions:* 5 V reference, active-high buzzer driver and start input, a switch to ground with the internal pull-up for "stop".
