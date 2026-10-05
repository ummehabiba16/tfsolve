---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "8086 (2 banks): WR0' (low/even bank, D0-D7) = WR' OR A0, WR1' (high/odd bank, D8-D15) = WR' OR BHE'. 80486 (4 banks): WRn' = MWTC' OR BEn' for n = 0..3. Two-input OR gates (74ALS32) because all signals are active low."
sources: ["Brey, The Intel Microprocessors, Sec. 10-4 and 10-6 (separate bank write strobes for the 8086 and 80386/80486)", "MHE 8086-Memory_Organization slides 3-5 (BHE and A0)"]
---
With separate write strobes, one decoder selects all banks for a read, and each bank gets its own **low-enabled write strobe**. A bank is written only when the write signal **and** its bank select are both low. For active-low signals, "both low" is an **OR** gate.

**8086 (two banks, selected by A0 and $\overline{BHE}$)**

$$\overline{WR0} = \overline{WR} + A0 \quad (\text{low/even bank, D0-D7})$$

$$\overline{WR1} = \overline{WR} + \overline{BHE} \quad (\text{high/odd bank, D8-D15})$$

```text
 WR'  --+
        OR --- WR0'  -> even bank (D0-D7)
 A0   --+
 WR'  --+
        OR --- WR1'  -> odd bank (D8-D15)
 BHE' --+
```

| $\overline{WR}$ | $\overline{BHE}$ | A0 | $\overline{WR1}$ | $\overline{WR0}$ | Write |
|:-:|:-:|:-:|:-:|:-:|:--|
| 0 | 0 | 0 | 0 | 0 | word (both banks) |
| 0 | 0 | 1 | 0 | 1 | odd byte |
| 0 | 1 | 0 | 1 | 0 | even byte |
| 1 | x | x | 1 | 1 | no write |

(In maximum mode use $\overline{MWTC}$ in place of $\overline{WR}$.)

**80486 (four banks, selected by $\overline{BE3}$-$\overline{BE0}$)**

$$\overline{WR_n} = \overline{MWTC} + \overline{BE_n}, \qquad n = 0, 1, 2, 3$$

```text
 MWTC' --+                     MWTC' --+
         OR --- WR0' (D7-D0)           OR --- WR2' (D23-D16)
 BE0'  --+                     BE2'  --+
 MWTC' --+                     MWTC' --+
         OR --- WR1' (D15-D8)          OR --- WR3' (D31-D24)
 BE1'  --+                     BE3'  --+
            (four 2-input OR gates: one 74ALS32)
```

$\overline{WR_n}$ is low only when $\overline{MWTC}$ = 0 and $\overline{BE_n}$ = 0, so only the bytes being written are changed; a read enables all banks with the common $\overline{MRDC}$.
