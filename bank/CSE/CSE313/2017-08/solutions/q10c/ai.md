---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "NFU never forgets: pages used heavily early keep high counters and are never evicted though no longer needed; fix by aging (shift the counter right before adding the R bit at the left)."
sources: ["Tanenbaum MOS 4e, sec. 3.4.6-3.4.7 (NFU, aging)"]
---
**Case where NFU performs badly.** NFU **never forgets**: a page's counter only grows. Consider a multi-pass compiler: pages used heavily in pass 1 accumulate **large counters**. In pass 2 the pass-1 pages are no longer needed, but their counters remain higher than those of the pass-2 pages (which have just started to be counted), so on a page fault NFU evicts the **pass-2 pages** that are in current use (low counter) and keeps the useless pass-1 pages. The result is many page faults.

**Modification: aging.** At every clock tick:

1. **shift the counter right by one bit** (so old references lose weight: each tick halves the history), and
2. **add the R bit at the leftmost bit** (not at the right end), then clear R.

The counter now weights *recent* references more heavily (the most recent tick is the most significant bit), so a page not used for several ticks has a small counter and is replaced first. (Aging also uses a finite counter, so it forgets references older than the number of bits; e.g. with 8 bits, anything older than 8 ticks is forgotten.)
