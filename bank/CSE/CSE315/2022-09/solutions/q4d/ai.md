---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "R too low: large current 5 V/R flows when S is pressed (wasted power, heating, can overload the supply/switch). R too high: the pin is only weakly pulled up, so input leakage current drops the 'high' voltage below the logic-1 threshold, the rise time (R x pin capacitance) is slow and noise is picked up. Typical choice ~10 k."
sources: ["EHP ATMega32 Basic IO slides 30-35 (pull-up resistor, opposing factors in choosing R)"]
---
In Figure 4(d), R is a **pull-up** resistor: with S open the pin is pulled to 5 V (logic 1); with S closed the pin is connected to ground (logic 0) and a current flows through R.

**If R is too low (e.g. 10 $\Omega$-100 $\Omega$)**

- When S is pressed, the current from 5 V through R and the switch to ground is $I = 5\ \text{V}/R$. For R = 100 $\Omega$ this is 50 mA; for 10 $\Omega$, 0.5 A.
- This **wastes power** (a big drain for a battery-powered device), **heats** the resistor and switch contacts, and can overload the supply or damage the switch.
- In the limit R = 0, pressing S short-circuits the supply.

**If R is too high (e.g. several M$\Omega$)**

- The pin is only weakly connected to 5 V. The input has a small **leakage current** $I_{IL}$, and the pin voltage when S is open becomes $V = 5 - I_{IL} R$. With a large R this can fall **below the logic-1 threshold**, so an open switch may read as 0 or undefined.
- The pin capacitance $C$ is charged through R, so the **rise time** $\approx RC$ when S opens is long. The pin passes slowly through the undefined region, and fast presses can be missed.
- A weak pull-up is easily disturbed by **noise**: the pin behaves almost like a floating input.

**Conclusion:** R must be low enough to give a solid, fast, noise-free logic 1, but high enough to keep the current small when the switch is closed. A value around **4.7 k$\Omega$-10 k$\Omega$** is typical (10 k$\Omega$ gives 0.5 mA when pressed). The ATmega32's internal pull-up (about 20-50 k$\Omega$) is a compromise of this kind.
