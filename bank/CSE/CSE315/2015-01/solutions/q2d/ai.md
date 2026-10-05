---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Polling: the CPU keeps checking each device's status. Interrupt: the device signals the CPU when it needs service, and the CPU runs an ISR and then resumes. Advantages of interrupts: efficiency (no CPU time wasted checking), many devices can be served with fast response, and priorities can be assigned (and masked)."
sources: ["EHP ATmega32 Interrupt slides 2-4, 9 (interrupts vs polling: efficiency, monitoring several devices, priority)"]
---
**Basic difference**

- **Polling:** the CPU **continually checks** the status of a device (reads a flag in a loop) to see whether it needs service, and serves it when the condition is found.
- **Interrupt:** the device **sends an interrupt signal** when it needs service. The CPU stops its current work, executes an **interrupt service routine (ISR)**, and then resumes the normal program.

**Advantages of interrupts over polling**

1. **Efficiency:** the CPU does not waste time checking devices that do not need service; it can do other work or sleep (save power) and is used only when an event happens.
2. **Monitoring several devices:** each device is served as soon as it requests, without the CPU visiting every device in turn; response time does not grow with the number of devices, and events are not missed while the CPU is busy elsewhere.
3. **Priority:** interrupts can be given priorities (on the ATmega32 a lower vector number has higher priority), so urgent events are served first; polling serves devices in a fixed round-robin order.
4. **Masking:** individual interrupts can be enabled or disabled as needed.
