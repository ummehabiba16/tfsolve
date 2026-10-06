---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Per-track seek = 100/32767 ms; SSTF 18 tracks = 0.055 ms; SCAN to the end 98,301 tracks = 300 ms; C-SCAN 196,602 tracks = 600 ms (LOOK variants: 18 and 29 tracks)."
sources: ["OSTEP ch. 37 (hard disks, disk scheduling)", "Tanenbaum MOS 4e, sec. 5.4.3"]
---
**Geometry.** $1\text{ GB}/4\text{ KB} = 262{,}144$ blocks; with 8 blocks per track there are $262{,}144/8 = 32{,}768$ tracks (0 to 32767). Block $b$ is on track $\lfloor b/8\rfloor$. The maximum seek (track 0 to track 32767, i.e. 32,767 tracks) is 100 ms, so we assume the seek time is proportional to the number of tracks crossed:

$$t_{\text{track}} = \frac{100}{32767}\text{ ms}\approx 0.00305\text{ ms}$$

Batches in tracks (head starts at track 0, SCAN direction initially *upward*; the arm position carries over from one batch to the next):

| Batch | Blocks | Tracks |
|:-:|:--|:--|
| 1 | 1, 40, 2, 15 | 0, 5, 0, 1 |
| 2 | 10, 1, 13, 32, 2, 7 | 1, 0, 1, 4, 0, 0 |
| 3 | 70, 49, 0, 6, 28 | 8, 6, 0, 0, 3 |

**i. SSTF** (always the nearest request):

- batch 1: $0\to0\to1\to5$: 5 tracks (head at 5)
- batch 2: $5\to4\to1\to0$: 5 tracks (head at 0)
- batch 3: $0\to3\to6\to8$: 8 tracks (head at 8)

Total $=18$ tracks $\Rightarrow 18\times0.00305 \approx \mathbf{0.055\ ms}$.

**ii. SCAN** (the arm sweeps all the way to the end of the disk before it reverses): batch 1: from track 0 up to track 32767 (32,767 tracks); batch 2: the arm is at the top and moves down to track 0 (32,767); batch 3: up to track 32767 again (32,767). Total $=98{,}301$ tracks $\Rightarrow\mathbf{300\ ms}$.

**iii. C-SCAN** (sweep up to the end, then jump back to track 0 without servicing): each batch costs $32{,}767$ (up) $+\,32{,}767$ (return) tracks. Three batches: $6\times32{,}767=196{,}602$ tracks $\Rightarrow\mathbf{600\ ms}$ (300 ms if the return jump is not counted as seeking).

**If the arm turns around at the last request instead of at the disk end** (LOOK / C-LOOK, the "elevator" of Tanenbaum):

| Algorithm | Batch 1 | Batch 2 | Batch 3 | Total tracks | Time |
|:--|:-:|:-:|:-:|:-:|:-:|
| LOOK | 5 | 5 | 8 | 18 | 0.055 ms |
| C-LOOK | 5 | 9 | 15 | 29 | 0.089 ms |

*Note.* The paper does not say whether the arm goes to the end of the disk, so both readings are given; the SSTF value is unaffected. (The values were computed with a short script.)
