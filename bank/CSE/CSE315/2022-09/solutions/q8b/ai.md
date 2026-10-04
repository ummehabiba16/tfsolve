---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(1) Single shared bus, detached DMA controller: I/O devices, DMAC, CPU and memory all on the system bus (each transfer uses the bus twice). (2) Single bus, integrated DMA-I/O: devices attached directly to the DMAC (or the DMA logic built into the I/O module), which uses the system bus once per transfer. (3) Separate I/O bus: the DMAC connects to the system bus on one side and an I/O bus with all devices on the other."
sources: ["Stallings, Computer Organization and Architecture, Sec. 7.5 (alternative DMA configurations)", "Brey, The Intel Microprocessors, Ch. 13 (DMA, HOLD/HLDA, 8237)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (DMA)"]
---
In every arrangement the DMA controller (DMAC) asks the CPU for the bus with **HOLD**. The CPU finishes its current bus cycle, floats its buses and answers **HLDA**. The DMAC then drives the address and control lines and moves data directly between memory and the I/O device. The three ways differ in where the I/O devices are attached.

**1. Single bus, detached DMA**

```text
 +-----+   +------+   +-------+   +-------+   +--------+
 | CPU |   | DMAC |   | I/O 1 |   | I/O 2 |   | Memory |
 +--+--+   +--+---+   +---+---+   +---+---+   +---+----+
    |         |           |           |           |
 ===+=========+===========+===========+===========+===== system bus
```

All modules share the system bus. The DMAC does **programmed transfers in two bus cycles**: read from the I/O device, then write to memory (or the reverse).
*Pros:* cheapest, simplest. *Cons:* each word uses the bus **twice**, so the CPU is held off for longer.

**2. Single bus, integrated DMA-I/O**

```text
 +-----+         +--------+
 | CPU |         | Memory |
 +--+--+         +---+----+
    |                |
 ===+=====+==========+========+========= system bus
          |                   |
      +---+----+          +---+----+
      |  DMAC  |          |  DMAC  |
      +-+----+-+          +---+----+
        |    |                |
     [I/O] [I/O]            [I/O]
```

Each DMAC is connected **directly** to its own I/O devices (or the DMA logic is built into the I/O controller) by a path that is not the system bus.
*Pros:* the data path DMAC-to-device does not use the system bus, so each transfer uses the bus **once**. *Cons:* more DMA hardware (one controller per device group).

**3. Separate I/O bus**

```text
 +-----+   +--------+   +------+
 | CPU |   | Memory |   | DMAC |
 +--+--+   +---+----+   +-+--+-+
    |          |          |  |
 ===+==========+==========+  |          system bus
                             |
           ==+=======+=======+====      I/O bus
             |       |       |
          [I/O 1] [I/O 2] [I/O 3]
```

One DMAC connects to the system bus on one side and to a separate **I/O bus** on the other, and all I/O devices sit on the I/O bus.
*Pros:* only **one** DMAC interface to the system bus, each transfer uses the system bus once, and new devices are easy to add. *Cons:* an extra bus and more complex DMAC.

*Note:* if the question means the three DMA **transfer modes** instead, they are: **burst (block)** mode (DMAC keeps the bus until the whole block is moved, CPU halted), **cycle stealing** (one word per HOLD/HLDA, CPU slowed slightly), and **transparent/interleaved** (transfers only in bus cycles the CPU does not use, no CPU slowdown).
