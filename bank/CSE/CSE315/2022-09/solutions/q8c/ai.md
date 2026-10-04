---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "A membrane key switch is two flexible conductive layers separated by a perforated spacer; pressing pushes the top layer through the hole to touch the bottom one. Cheap, thin, sealed against dust and liquids (microwave ovens, remotes), but little tactile feedback, shorter life and contact bounce, so it needs debouncing and matrix scanning like other contact switches."
sources: ["Hall, Microprocessors and Interfacing, Ch. 9 (keyboard types: mechanical, membrane, capacitive, Hall-effect)", "Brey, The Intel Microprocessors, Sec. 11-4 (keyboard interfacing, debouncing)"]
---
**Construction.** A membrane key switch is a special kind of contact switch made of thin layers:

```text
   finger press
        v
 ================  top flexible layer (conductive ink underneath)
 ====   ====   ==  spacer layer with a hole under each key
 ================  bottom layer (conductive ink on top)
```

Pressing the key pushes the top conductive layer **through the hole in the spacer** onto the bottom layer, which closes the circuit. Releasing it lets the top layer spring back and open the contact. Many keys are printed on the same sheets, usually as a row/column matrix.

**Advantages**

- **Very low cost** and **very thin**; the whole keypad is one flat unit.
- **Sealed**: dust, dirt and liquids cannot get in, so it suits kitchens, factories and medical equipment (microwave ovens, photocopiers, remote controls, ATM keypads).
- The legends are printed on the top sheet, so it is easy to customise.

**Disadvantages**

- Little or no **tactile feedback** (the key hardly moves), so it is hard to type fast; a beep or LED is often used as feedback.
- **Shorter lifetime** than good mechanical keys (a few million presses).
- Like any contact switch it **bounces**, so it needs **debouncing** (hardware or software delay) and is read by **matrix scanning** in the microprocessor system.
