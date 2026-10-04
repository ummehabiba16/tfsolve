---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Separate write strobes: one decoder for all banks, every read reads all banks; cheap, but needs write-strobe logic. Separate decoders: each bank has its own decoder enabled by its bank select; any read/write selects only the needed banks, but needs one decoder per bank (more hardware). For the 80486: WRn' = BEn' OR MWTC' (four 2-input OR gates)."
sources: ["Brey, The Intel Microprocessors, Sec. 10-4 and 10-6 (separate bank decoders vs separate bank write strobes; 80386/80486 memory interface with BE3'-BE0')", "MHE 80386-updated slides 4, 12 (four banks, BE0-BE3)"]
---
**i. Separate write signal (write strobe) for each bank**

- One address decoder selects the whole memory block (all banks together). A **read** always reads **all banks** at once; the processor simply takes the bytes it needs from the data bus.
- For a **write**, only the addressed bytes may change, so a separate write strobe $\overline{WR_n}$ is made for each bank from its bank-enable signal and the write signal.
- **Pros:** only **one decoder** is needed, so less hardware and lower cost; simple, and the most common method. Reading extra bytes does no harm.
- **Cons:** extra gates are needed for the write strobes; all banks are active on every read (slightly more power, and devices with read side effects, such as I/O, cannot share this scheme).

**ii. Separate decoder for each bank**

- Each bank has its own decoder, enabled by its own bank select ($\overline{BE_n}$, or A0/$\overline{BHE}$ on the 8086). The common $\overline{MRDC}$/$\overline{MWTC}$ go to all banks.
- **Pros:** only the banks actually addressed are enabled, for both read and write; no write-strobe logic; works for any device, including I/O.
- **Cons:** **one decoder per bank** (4 decoders for a 32-bit bus), so more chips, board space and cost. Usually considered the more wasteful method.

**Write-strobe circuit for the 80486**

The 80486 has a 32-bit data bus organised as 4 banks with active-low bank enables $\overline{BE3}$-$\overline{BE0}$ and the active-low memory write $\overline{MWTC}$. A bank must be written only when **both** its $\overline{BE_n}$ and $\overline{MWTC}$ are low. For active-low signals this is an **OR** gate:

$$\overline{WR_n} = \overline{BE_n} + \overline{MWTC}, \qquad n = 0, 1, 2, 3$$

```text
 BE0' ---+
         OR ---- WR0'  -> bank 0 (D7-D0)
 MWTC' --+
 BE1' ---+
         OR ---- WR1'  -> bank 1 (D15-D8)
 MWTC' --+
 BE2' ---+
         OR ---- WR2'  -> bank 2 (D23-D16)
 MWTC' --+
 BE3' ---+
         OR ---- WR3'  -> bank 3 (D31-D24)
 MWTC' --+
        (one 74ALS32 quad 2-input OR)
```

| $\overline{BE_n}$ | $\overline{MWTC}$ | $\overline{WR_n}$ |
|:-:|:-:|:-:|
| 0 | 0 | **0** (write this bank) |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

A single decoder (from A31-A2 and M/$\overline{IO}$) drives the $\overline{CS}$ of all four banks, and $\overline{MRDC}$ goes to the $\overline{OE}$ of all banks.
