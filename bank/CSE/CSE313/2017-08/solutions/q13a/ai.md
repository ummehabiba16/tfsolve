---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Demand paging loads a page only when it is referenced (page fault); pre-paging loads pages in advance that are expected to be needed (e.g. the whole working set of a process when it starts or restarts)."
sources: ["Tanenbaum MOS 4e, sec. 3.4.8 and 3.6.1 (demand paging, pre-paging)"]
---
- **Demand paging:** a process starts with **none (or few) of its pages in memory**; a page is brought in only **when it is first referenced** (a page fault occurs and the OS loads it). Only pages actually used are loaded, so memory is not wasted, but each first reference costs a page fault, so the start-up of a process generates many faults.
- **Pre-paging:** the OS **loads pages before they are referenced**, based on a prediction: e.g. when a process is started or resumed, load its remembered **working set** at once, or load the pages next to the faulting page. It reduces the number of page faults (and allows large, efficient disk transfers) but wastes memory and I/O if the prediction is wrong.
