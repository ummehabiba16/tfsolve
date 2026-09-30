---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**(i) Extra PTE bits needed:** the standard *use/reference bit (R)* (already assumed present for Clock) plus the *dirty/modified bit (M)*. We also conceptually need a (software) "write-back in progress" flag per frame so the algorithm does not try to evict/re-issue a flush for a page whose write-back is already underway.

**(ii) Hardware support required:** the MMU must automatically *set* $R=1$ on any access (read or write) and *set* $M=1$ on any write, without trapping to software (this is standard on most architectures). The OS must be able to read and clear $R$ cheaply (e.g., by manipulating the PTE's permission bits or a dedicated flag) during the periodic clock sweep, and must be able to issue an asynchronous write-back of a page to disk while the process continues running.

**(iii) Modified Clock algorithm (handles dirty pages):**

1.  Clock hand scans frames circularly, as usual.

2.  At the candidate frame: if $R=0$ and $M=0$ $\to$ this page is both unused and clean $\to$ **evict it immediately** (free, no I/O needed).

3.  If $R=0$ and $M=1$ $\to$ unused but dirty: **do not evict yet**; instead *start an asynchronous write-back* of the page to disk (mark it "write pending"), and move the hand on. When the write-back later completes, clear $M$ -- the page is now a cheap (clean) eviction candidate the next time the hand reaches it.

4.  If $R=1$ $\to$ give the page a second chance: clear $R$ to 0 (regardless of $M$) and move the hand on without evicting.

5.  Repeat until a frame with $R=0,\,M=0$ is found (either originally clean, or a dirty page whose background flush has since completed); evict that frame for the incoming page.

*Rationale*: by always preferring clean victims and proactively flushing dirty pages *before* they are actually needed, the algorithm converts what would be a synchronous, expensive dirty-page write-back at fault time into a cheap, already-clean eviction, hiding disk latency behind ongoing execution.
