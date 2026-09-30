---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Initial layout at address $A0$: a data block $D$ immediately followed by inode block $I$, whose pointer $b[0]$ references $A0$ (i.e. $I$ points at $D$).

In LFS, an in-place update is never performed. Modifying a single byte of the file's data ($D$) triggers a cascading, append-only update:

1.  The **modified data block** $D'$ (new content) is written to a fresh location at the current tail of the log, say address $A1$.

2.  Since $D$ moved, the file's **inode must also change** (its pointer $b[0]$ needs to reference the new location $A1$ instead of the old $A0$): a new inode $I'$ (with $b[0]{:}A1$) is written right after $D'$, at the next free address, say $A2$.

3.  Because $I$ itself moved (from wherever it previously was recorded to now $A2$), the **inode map (imap)** entry for this file's inode number is updated to point at $A2$. Since the imap is looked up directly (not through further indirection), the cascade stops here -- it does not chain any further.

**Updated layout:**

|  |  |
|:---|:---|
| Old (now dead/garbage, awaiting cleaning) | $A0$: $[\,D \mid I\;(b[0]{:}A0)\,]$ |
| New (live, appended at the log's tail) | $A1$: $[\,D'\,]$ $A2$: $[\,I'\;(b[0]{:}A1)\,]$ |

and $\text{imap}[\text{inode \#}]$ is updated to $A2$. The old $[D\,|\,I]$ pair at $A0$ is no longer referenced by anything live and becomes garbage, to be reclaimed later by segment cleaning.
