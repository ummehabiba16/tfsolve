---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Flags 0101 1110 0101 0101 give IOPL = 01. Only a device more trusted than IOPL may do I/O, so Device 2 (privilege 00) gets the port; Devices 1 (11) and 3 (10) cause an interrupt."
sources: ["MHE 80286 slides 16-17 (flag register, IOPL D13-D12)"]
---
**Decode the flag register** 0101 1110 0101 0101 (D15 ... D0):

| D15 | D14 NT | D13 D12 IOPL | D11 OF | D10 DF | D9 IF | D8 TF | D7 SF | D6 ZF | D5 | D4 AF | D3 | D2 PF | D1 | D0 CF |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 1 | **01** | 1 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |

So **IOPL = 01**. Level 00 is the highest (most trusted) and 11 the lowest.

**Rule (slide 17):** if the requester's privilege level is **higher (more trusted) than IOPL**, the I/O is executed without hindrance. If it is lower, an interrupt occurs and execution is suspended.

| Device | Privilege level | Compared with IOPL = 01 | Result |
|:--|:-:|:--|:--|
| Device 1 | 11 | lower (less trusted) | interrupt, denied |
| Device 2 | 00 | higher (more trusted) | **access granted** |
| Device 3 | 10 | lower (less trusted) | interrupt, denied |

**Conclusion: Device 2 gets access to the I/O port.**
