---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Single-level: 2^52 entries x 8 B = 2^55 B = 32 PiB; inverted table: 2^20 frames x 80 bits = 10 MB."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2-3.3.4 (page tables, inverted page tables)"]
---
**(i) Single-level page table for one process.**

- Page size $4\text{ KB}=2^{12}$, virtual address 64 bits $\Rightarrow$ VPN has $64-12=52$ bits, so there are $2^{52}$ entries.
- Each entry holds the **52-bit frame number plus 12 bits of information $=64$ bits $=8$ bytes**.

$$2^{52}\times 8\text{ B}=2^{55}\text{ B}=\mathbf{32\ PiB}\approx3.6\times10^{16}\text{ bytes}$$

(far bigger than any memory, so impossible).

(The stated physical memory of 4 GB would need only 20-bit frame numbers; the question prescribes 52 bits per entry.)

**(ii) Inverted page table (one for all processes).** One entry per **physical frame**: $4\text{ GB}/4\text{ KB}=2^{20}$ entries. Each entry stores the **virtual page number (52 bits), the process ID (16 bits) and 12 bits of information**; the frame number is implicit (the index of the entry).

$$52+16+12=80\text{ bits}=10\text{ bytes}$$

$$2^{20}\times10\text{ B}=10{,}485{,}760\text{ B}=\mathbf{10\ MB}$$

So the inverted table is only 10 MB for all processes together, independent of the size of the virtual address space and of the number of processes (a hash table is added to search it quickly).
