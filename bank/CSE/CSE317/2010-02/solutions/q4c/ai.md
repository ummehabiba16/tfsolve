---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "SMA* uses all available memory: it expands the best leaf, adds successors one at a time, and when memory is full drops the worst (highest-f, shallowest) leaf, backing its f-value up to the parent; a non-goal node at the memory depth limit gets f = infinity. It is complete and optimal if the shallowest optimal goal fits in memory, otherwise it returns the best reachable solution. With 3 nodes: A, B, G; G-H (H = infinity, B dropped, A remembers 15); I (24); regenerate B; C (infinity); D (20). It returns D (cost 20): the true optimum J (18) is at depth 3 and needs 4 nodes, so it is unreachable."
sources: ["AIMA 1e sec. 4.3 / AIMA 3e sec. 3.5.3 (SMA*)"]
---
**Characteristics of SMA\*** (simplified memory-bounded A\*).

- It works like A\*, expanding the leaf with the lowest $f$ (the deepest such leaf among ties), but it uses **only the available memory** (here 3 nodes).
- Successors are generated **one at a time**, and $f(child)=\max(f(parent),\ g+h)$.
- When memory is full and a node must be added, it **drops the worst leaf** (the highest $f$, the shallowest among ties) and **backs up** its $f$-value into the parent. The parent remembers the best forgotten subtree, and regenerates it only if all other paths look worse.
- A non-goal node at the **maximum depth** allowed by memory (depth 2 here, since a path of 3 nodes fills memory) cannot be expanded further, so its $f=\infty$.
- **Complete** if the depth of the shallowest goal is less than the memory size. **Optimal** if an optimal solution is reachable within memory; otherwise it returns the **best solution reachable** with the memory it has.

**Trace** (memory = 3 nodes; values are $f=g+h$; the brackets show what a parent remembers about forgotten children):

| Step | Action | Memory (f) |
|:-:|:--|:--|
| 1 | start | A(12) |
| 2 | add B | A(12), B(15) |
| 3 | add G; A is fully expanded, so f(A) = min(15, 13) = 13 | A(13), B(15), G(13) |
| 4 | expand G: add H. Memory is full, so drop B (worst leaf); A remembers [B = 15]. H (depth 2, not a goal) gets f = $\infty$ | A(13), G(13), H($\infty$) |
| 5 | add G's other child I (24, goal); drop H; G remembers [H = $\infty$]. G's f becomes min(24, $\infty$) = 24, and A's f becomes min(24, [15]) = 15 | A(15), G(24), I(24) |
| 6 | the best is A's forgotten B (15): regenerate B; drop I (worst leaf); G remembers [I = 24] | A(15), G(24), B(15) |
| 7 | expand B: add C; drop G; A remembers [G = 24]. C (depth 2, not a goal) gets f = $\infty$ | A(15), B(15), C($\infty$) |
| 8 | add B's other child D (20, goal); drop C. B's f becomes min($\infty$, 20) = 20, and A's f becomes min(20, [24]) = 20 | A(20), B(20), D(20) |
| 9 | the lowest-f node is the goal D: **return D** | |

**Result: SMA\* returns goal D with cost 20**, via A-B-D.

**Justification.** Among the goals, J (18) is the cheapest. But it lies at depth 3 (A-G-H-J), and holding its path needs 4 nodes, more than the memory allows: H could only be stored as a dead end with $f=\infty$. The goals reachable within memory are D (20) and I (24), and SMA\* correctly returns the better one, D. With a memory of 4 or more nodes, it would find the optimal goal J (18).
