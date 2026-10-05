---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "10-bit successive-approximation ADC; 8 multiplexed single-ended channels (PA0-PA7), differential channels with gain 1x/10x/200x; reference AVCC, internal 2.56 V or external AREF; sample and hold; 13-260 us conversion (13 ADC clocks, prescaler 2-128, 50-200 kHz for full resolution); single, free-running or auto-triggered conversion; left/right adjusted result in ADCH:ADCL; conversion-complete interrupt; noise reduction sleep mode."
sources: ["EHP 6. AVR ADC slides 16-30, 45-47 (ADC of ATmega, channels, reference, result registers, ADCSRA, ADC clock, auto trigger)"]
---
- **10-bit resolution**, successive-approximation converter: output 0-1023 (step = $V_{ref}/1024$, 4.88 mV at 5 V).
- **8 single-ended input channels** (ADC0-ADC7 on PA0-PA7) through an analog multiplexer; one conversion at a time.
- **Differential channels** (e.g. ADC1 - ADC0) with **programmable gain 1x, 10x or 200x**; result in two's complement.
- **Reference voltage** selectable (REFS1:0 in ADMUX): **AVCC**, **internal 2.56 V**, or **external AREF**.
- **Sample-and-hold** circuit keeps the input constant during conversion.
- **Conversion time** 13 ADC clocks (25 for the first), i.e. 13-260 µs; ADC clock from a **prescaler** (2-128) and 50-200 kHz for full accuracy.
- **Modes:** single conversion, **free running**, or **auto-triggered** by a timer, analog comparator or external interrupt (ADATE, SFIOR).
- **Result** in ADCH:ADCL, **left or right adjusted** (ADLAR); read ADCL first.
- **Interrupt** on conversion complete (ADIF/ADIE), and an **ADC noise reduction sleep mode**.
