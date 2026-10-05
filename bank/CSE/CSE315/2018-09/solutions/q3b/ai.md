---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "The row decoder is 8-to-256, so 256 rows (one row refresh covers all four arrays). 256 refresh cycles x 800 ns = 204.8 us in every 4 ms, so the loss is 204.8 us / 4 ms = 5.12% of computer time."
sources: ["Brey, The Intel Microprocessors, Sec. 10-1 (DRAM refresh, RAS-only refresh, percentage of time lost to refresh)"]
---
**Number of rows.** The row decoder is an **8-line to 256-line** decoder, and one row address activates the same row in **all four** 256 $\times$ 256 arrays. Refreshing a row therefore refreshes 1024 cells at once, and the whole 256K DRAM needs

$$256\ \text{row refreshes in every 4 ms}$$

**Time for one refresh.** Each refresh is one memory cycle (a $\overline{RAS}$-only cycle), the same length as a read or write: **800 ns** (4 clocks of a 5 MHz processor: $4 \times 200$ ns).

$$t_{refresh} = 256 \times 800\ \text{ns} = 204.8\ \mu s \ \text{per 4 ms}$$

**Loss of computer time**

$$\text{Loss} = \frac{204.8\ \mu s}{4\ \text{ms}} \times 100\% = \mathbf{5.12\%}$$

(One refresh about every $4\ \text{ms}/256 = 15.6\ \mu s$.)

*Note:* if all 512 row addresses (9 row bits) had to be refreshed separately, the loss would double to 10.24%. In this design the 9th row bit only drives the 4-to-1 output MUX, so 256 refreshes suffice.
