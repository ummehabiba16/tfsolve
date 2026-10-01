---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) About 99.22% cannot be accessed in real mode; (ii) page size 256 B; (iii) virtual memory 2^34 B = 16GB; (iv) pre-fetch queue 10 bytes."
sources: ["MHE 8086-Memory_Organization slides 10-12 (append 0H, paragraph)", "MHE 80286 slides 3, 43-44, 66 (selector, 1GB virtual memory)", "MHE 80386-updated slides 4, 7, 21-22 (paging, 15-byte queue)"]
---
Given: 20-bit microprocessor, so registers and offsets are 20 bits. Address bus 28 bits, so physical memory $=2^{28}$ B = 256MB (byte-addressable). Six 16-bit segment registers. Longest instruction 10 bytes. 3 access-control bits in virtual memory mode.

**(i) Memory not accessible in Real Mode**

In real mode the segment register works as in the 8086: it is appended with 0H (shifted left by 4 bits) and the offset is added.

$$PA_{max} = FFFF0H + FFFFFH = 1FFFEFH$$

So only addresses 000000H to 1FFFEFH can be reached:

$$1FFFF0H = 2{,}097{,}136 \text{ locations} \approx 2\text{MB}$$

$$\text{Not accessible} = 1-\frac{2{,}097{,}136}{2^{28}} = 1 - 0.0078 = \mathbf{99.22\%}$$

**(ii) Page size**

In protected mode the linear address has the width of the physical address, 28 bits (as in the 80386, where both are 32 bits). With 1K entries each:

- Directory field: $\log_2 1024 = 10$ bits
- Page table field: 10 bits
- Offset $= 28-10-10 = 8$ bits

$$\text{Page size} = 2^{8} = \mathbf{256\text{ B}}$$

**(iii) Virtual memory size**

In virtual memory mode the 16-bit segment register holds a selector, and 3 of its bits are access-control bits (TI and RPL, as in the 80286). That leaves $16-3=13$ index bits per table, and TI selects one of two tables (GDT or LDT):

$$\text{Segments} = 2^{13}\times 2 = 2^{14}$$

Each segment can have the full 20-bit offset, so it is $2^{20}$ B = 1MB:

$$\text{Virtual memory} = 2^{14}\times2^{20} = 2^{34}\text{ B} = \mathbf{16\,GB}$$

*Check against the 80286 slide: $2^{14}\times 2^{16} = 1$GB.*

**(iv) Size of the pre-fetch queue**

The queue must be able to hold the longest instruction so that a complete instruction is always ready for the decoder. In the 8086 the queue is 6 bytes for 6-byte instructions, and in the 80386 the instruction code queue is 15 bytes for 15-byte instructions. Here the longest instruction is 10 bytes $= 80$ bits, which is exactly 4 fetches over the 20-bit data bus ($4\times20 = 80$).

$$\text{Pre-fetch queue} = \mathbf{10\text{ bytes}}$$
