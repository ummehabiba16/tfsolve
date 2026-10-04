---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Interrupt (with a priority encoder/controller giving the lowest ID the highest priority). Reasons: efficiency (the CPU is not busy checking 16 devices), fast response to any device (no waiting for a polling round), and hardware priority so the lowest-ID device is served first (polling checks in round-robin order and cannot assign priority)."
sources: ["EHP ATmega32 Interrupt slides 2-4, 9 (interrupts vs polling: efficiency, monitoring several devices, priority; lower vector number = higher priority)"]
---
**Use interrupts.** Connect the 16 request lines through a priority encoder / interrupt controller (e.g. a 16-to-4 priority encoder or cascaded 8259As) that gives the **lowest ID the highest priority** and supplies the 4-bit ID as the interrupt vector.

**Reasons**

1. **Efficiency.** With polling the CPU must keep reading all 16 devices even when none needs service, wasting almost all of its time. With interrupts the CPU does useful work (or sleeps) and is involved only when a device actually asks for service.
2. **Monitoring many devices with fast response.** With polling a device that triggers just after its turn waits until the CPU has checked the other 15 devices, so the response time grows with the number of devices. With interrupts each request reaches the CPU immediately, and the device's ID (vector) takes the CPU straight to the right service routine without searching.
3. **Priority.** The requirement "if several trigger together, serve the lowest ID" is a **priority** rule. Interrupt hardware resolves it automatically and at once: the priority encoder passes the lowest active ID, just as the ATmega32 gives the lower vector number the higher priority. Polling checks devices one after another in a fixed (round-robin) order, so it cannot assign priority to simultaneous requests without extra software work, and a request may be found late.
