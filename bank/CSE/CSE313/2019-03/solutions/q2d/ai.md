---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) 20 -> 8212; (ii) 4100 -> 4100; (iii) 8300 -> 24684."
sources: ["Tanenbaum MOS 4e, sec. 3.3.1 (page tables, fig. 3-9)"]
---
Page size $=4\text{ KB}=4096$ B; frame number from the table of the figure: page 0 $\to$ 2, page 1 $\to$ 1, page 2 $\to$ 6, page 3 $\to$ 0, ...

$$\text{physical address} = \text{frame}\times4096 + \text{offset}$$

| Virtual address | Page = addr div 4096 | Offset | Frame | Physical address |
|:-:|:-:|:-:|:-:|:-:|
| 20 | 0 | 20 | 2 | $2\times4096+20=\mathbf{8212}$ |
| 4100 | 1 | 4 | 1 | $1\times4096+4=\mathbf{4100}$ |
| 8300 | 2 | $8300-8192=108$ | 6 | $6\times4096+108=24576+108=\mathbf{24684}$ |
