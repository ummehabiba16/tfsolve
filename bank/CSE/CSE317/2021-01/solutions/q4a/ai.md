---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Greedy search gets trapped in local optima. Hybrid: run greedy (steepest-descent) improvement to a local optimum, then use SA moves (accept a worse neighbour with probability e^(-d/T)) to escape, repeat with decreasing T, keeping the best solution; greedy gives fast intensification, SA gives diversification."
sources: ["AIMA 3e sec. 4.1.1-4.1.2"]
---
**Main problem of greedy algorithms.** They always take the locally best move and never undo a choice, so they stop at the first **local optimum** (also stuck on ridges and plateaux). The result is generally not the global optimum and depends on the starting point.

**How simulated annealing solves it.** SA accepts a worse move with probability $e^{-\Delta/T}$ (for minimisation, $\Delta>0$ is the increase in cost). At high temperature $T$ it can climb out of the basin of a local optimum; as $T$ decreases it becomes more and more greedy and settles in a good basin. With slow enough cooling it reaches the global optimum with probability approaching 1.

**Complementary strengths.**

- Greedy: very fast convergence to the bottom of the current basin (intensification), but no escape.

- SA: escape from local optima (diversification), but slow, wastes time on random moves near good solutions.

**Hybrid (greedy + SA) for minimising cost $C$.**

```text
function GREEDY-SA(s0, T0, alpha, L, Tmin):
    s <- GREEDY-DESCENT(s0)              // reach a local optimum quickly
    best <- s
    T <- T0
    while T > Tmin:
        repeat L times:
            s' <- RANDOM-NEIGHBOUR(s)
            d  <- C(s') - C(s)
            if d < 0 or RANDOM(0,1) < exp(-d / T):   // SA acceptance
                s <- s'
                if d < 0:
                    s <- GREEDY-DESCENT(s)           // greedy polishing of improvements
                if C(s) < C(best): best <- s
        T <- alpha * T                               // cooling, e.g. alpha = 0.9
    return GREEDY-DESCENT(best)

function GREEDY-DESCENT(s):
    loop:
        n <- the best neighbour of s
        if C(n) >= C(s): return s
        s <- n
```

**How it works.** The greedy phase moves quickly to the bottom of a basin. The SA phase then makes random moves; worse moves are accepted with probability $e^{-d/T}$, which lets the search leave the basin. Whenever an improving move is found, greedy descent immediately exploits it to reach the new local optimum. As $T$ falls, fewer uphill moves are accepted, and the final greedy pass polishes the best solution found. This gives better solutions than greedy search and converges faster than plain SA (similar to "basin hopping" / iterated local search with SA acceptance).
