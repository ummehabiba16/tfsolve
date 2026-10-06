---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "A copying (stop-and-copy) collector moves objects to new addresses, so the pointers inside the copied objects, and pointers from other objects, roots and older generations to them, would still refer to the old (From-space) addresses if objects were copied bitwise. It is handled by (1) leaving a forwarding address (NewLocation) in each old object, so later references to it are redirected to the copy and each object is copied only once; (2) scanning every copied object and replacing each pointer field by the new address (Cheney's scan), and (3) for generations, keeping a remembered set of old-to-young pointers (via a write barrier), which are treated as roots and updated when young objects move."
sources: ["KMS Chapter 7 slides 79-92 (Relocating, Copying Garbage Collectors, Cheney)", "Dragon book 2e sec. 7.6.4, 7.7.3 (Generational Garbage Collection)"]
changes:
  - "2026-10-06: replaced the two ASCII sketches by one TikZ figure comparing the bitwise copy with the forwarding-address copy"
---
**Why a bitwise copy is not enough.** A stop-and-copy (copying) collector **relocates** objects: each live object is copied from the From space (or a young generation) to a new address in the To space (or an older generation). A plain bitwise copy reproduces the object's fields exactly, including its **pointer fields**, which still hold the **old addresses** in From space. Also, other objects, the root set and objects in **older generations** that point to the moved object still hold its old address. After the collection, From space is reused, so all these pointers would be dangling.

![Bitwise copy (wrong) versus pointer-translating copy with forwarding addresses (correct)](figures/copy.png)

**How it is handled:**

1. **Forwarding addresses (NewLocation).** When an object is copied, its new address is recorded in the old copy (`NewLocation(o)`). Whenever another reference to `o` is found later, the collector sees that `o` was already copied and uses the forwarding address instead of copying again. This keeps sharing and cycles intact.
2. **Scanning and translating pointers.** Every copied object is **scanned** (Cheney's `unscanned` pointer). Each pointer field `o.r` is replaced by `LookupNewLocation(o.r)`, which copies the target if necessary and returns its new address. The root set is translated the same way.

3. **Generational collectors: the remembered set.** When only the young generation is collected, pointers from **older generations into the young one** must also be found and updated, without scanning the whole old generation. A **write barrier** records every store that creates such a pointer in a **remembered set**. During a minor collection, these entries are treated as extra roots, and after the young objects are moved, the pointers in the old generation are updated to the new addresses.

So copying collection must be a **pointer-translating** copy, not a raw memory copy.
