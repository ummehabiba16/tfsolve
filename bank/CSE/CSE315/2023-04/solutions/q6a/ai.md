---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "(i) A memory chip has fewer address pins than the CPU; decoding the extra upper address lines into a chip-select gives each chip its own unique address range, so it does not respond at every address or clash with other chips on the data bus. (ii) 32-bit address, word addressable: addresses 0 to 2^32 - 1, so the maximum address is FFFFFFFFh."
sources: ["Brey, The Intel Microprocessors, Sec. 10-2 (address decoding, NAND and 74LS138 decoders)", "Rafiquzzaman, Microprocessors and Microcomputer-Based System Design, Ch. 5 (memory interfacing)"]
---
**(i) Why address decoding is essential**

- A microprocessor has more address lines than a memory chip. The 8086 has 20 (A19-A0, 1 MB), but a 2K $\times$ 8 EPROM has only 11 (A10-A0) and an 8K $\times$ 8 RAM has 13.
- The chip's own address pins connect to the **low** address lines. If the remaining **upper** lines were ignored, the chip would be selected for **every** combination of those lines: a 2 KB EPROM would appear $2^{9} = 512$ times in the 1 MB space, and it would drive the data bus at the same time as any other memory or I/O chip (bus contention, wrong data).
- **Address decoding** uses the upper address lines (and control signals such as M/$\overline{IO}$) to produce a **chip-select** ($\overline{CS}$/$\overline{CE}$) that is active for **only one block** of addresses. Each chip then has a **unique address range**, and only one device drives the data bus at a time.

*Example 1 (NAND decoder):* a 2K $\times$ 8 EPROM at **FF800H-FFFFFH** on an 8086. A10-A0 go to the EPROM. A19-A11 are all 1 in this range, so a 9-input NAND gate of A19-A11 gives $\overline{CE}$ = 0 only for FF800H-FFFFFH.

```text
A19 --+
 ...  |NAND o---- CE'  (EPROM 2K x 8, A10-A0 from bus)
A11 --+
```

*Example 2 (74LS138):* A19-A17 drive the select inputs of a 3-to-8 decoder; each of the 8 outputs selects one 128 KB block (Y0: 00000H-1FFFFH, ..., Y7: E0000H-FFFFFH), so 8 memory chips can share the bus without conflict.

**(ii) Maximum allowable address**

With a 32-bit address bus there are $2^{32}$ distinct addresses, $0$ to $2^{32}-1$. In a **word-addressable** memory each address names one whole word (not one byte), so all $2^{32}$ addresses are used for words:

$$\text{Maximum address} = 2^{32} - 1 = \mathbf{FFFFFFFFh} \ (4\,294\,967\,295)$$

The memory therefore holds $2^{32}$ words (e.g. 8 GB if a word is 16 bits).
