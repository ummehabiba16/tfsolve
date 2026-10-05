---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Quiescence search: at the depth cutoff, apply the evaluation function only to quiescent positions (those unlikely to swing wildly in value soon); non-quiescent positions (e.g. pending captures or checks) are expanded further, usually only with captures, until quiet positions are reached. This avoids misleading evaluations (part of the horizon problem)."
sources: ["AIMA 3e sec. 5.4.2 (cutting off search, quiescence search)"]
---
**Quiescence search.** In depth-limited game search, the evaluation function is applied at the cutoff depth. If the position at the cutoff is in the middle of a tactical exchange (for example, White has just captured a knight but Black can recapture the queen next move), the static evaluation is **misleading**: it says White is ahead by a knight when White is about to lose its queen.

The idea is to apply the evaluation function only to **quiescent** positions: positions that are unlikely to show wild swings in value in the near future (no pending captures, checks or promotions). Non-quiescent positions at the cutoff are **expanded further**, usually considering only "noisy" moves such as captures, until quiet positions are reached. This extra search is quiescence search.

```text
if CUTOFF-TEST(s, depth):
    if QUIESCENT(s): return EVAL(s)
    else: search further, considering only captures / checks, until quiescent
```

It reduces evaluation errors caused by the cutoff and partly addresses the **horizon effect**, although singular extensions are also needed for that.
