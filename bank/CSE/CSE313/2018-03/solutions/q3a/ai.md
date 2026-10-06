---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Max file size = (10 + 512 + 512^2 + 512^3 + 512^4) blocks x 2 KB = 68,853,957,130 blocks, about 1.41e14 bytes (128.25 TB)."
sources: ["Bach, ch. 4 (inode block addressing)", "Tanenbaum MOS 4e, sec. 4.3.2"]
---
A block is $2\text{ K}=2048$ bytes and a block address needs $32\text{ bits}=4$ bytes, so a block of pointers holds $2048/4=512$ addresses. The modified table of contents has 14 entries: **10 direct**, and single, double, triple and quadruple indirect.

| Entry | Data blocks addressed |
|:--|:-:|
| 10 direct | 10 |
| single indirect | $512$ |
| double indirect | $512^2=262{,}144$ |
| triple indirect | $512^3=134{,}217{,}728$ |
| quadruple indirect | $512^4=68{,}719{,}476{,}736$ |
| **Total** | **68,853,957,130** blocks |

$$68{,}853{,}957{,}130\times2048\text{ B}=141{,}012{,}904{,}202{,}240\text{ B}\approx\mathbf{128.25\ TB}$$

(about $2^{47}$ bytes; the quadruple-indirect entry dominates: $512^4\times2\text{ KB}=2^{36}\times2^{11}=2^{47}$ B $=128$ TB).
