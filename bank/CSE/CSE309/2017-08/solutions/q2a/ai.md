---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Order K, F, Ow, P, T, M, Ma, V, C: K -> Ow o gway K'; K' -> ungfu P anda K' | ungfu F urious5 K' | eps; F -> Ow o gway K' F (T|M|Ma|V|C); Ow -> warrior K F Ow'; Ow' -> o gway K' F masterofmaster Ow' | o gway K' F X K shifumaster Ow' | dragon K F Ow' | eps; P -> P'; P' -> o P' | eps; T -> T'; T' -> igress T' | eps; M has no non-recursive alternative."
sources: ["MMA syntax analysis slides 27-60 (Elimination of left recursion)", "Dragon book 2e Algorithm 4.19, sec. 4.3.3"]
---
**Reading the grammar.** Bold letters in the paper are nonterminals; lower-case words are terminals. The productions are

```text
K  -> K ungfu P anda | K ungfu F urious5 | Ow o gway
F  -> K F T | K F M | K F Ma | K F V | K F C
Ow -> K F masterofmaster | F K shifumaster | Ow dragon K F | warrior K F
P  -> P o | eps
T  -> T igress | eps
M  -> M onkey
Ma -> f Ma antis
V  -> f V iper
C  -> f C rane
```

**Method (Algorithm 4.19).** Fix an order of the nonterminals, here $K, F, O_w, P, T, M, M_a, V, C$. For each $A_i$: (a) replace every production $A_i \to A_j\gamma$ with $j < i$ by $A_i \to \delta_1\gamma \mid \dots \mid \delta_k\gamma$, where $A_j \to \delta_1 \mid \dots \mid \delta_k$ are the current productions of $A_j$; (b) eliminate the **immediate** left recursion among the $A_i$-productions: $A \to A\alpha \mid \beta$ becomes $A \to \beta A'$, $A' \to \alpha A' \mid \epsilon$.

The recursion here is both immediate ($K$, $O_w$, $P$, $T$, $M$) and indirect ($K \Rightarrow O_w \Rightarrow K F \ldots$ and $F \Rightarrow K F T \Rightarrow \ldots$).

**$i = 1$, $K$.** Immediate recursion: $\alpha_1 = ungfu\,P\,anda$, $\alpha_2 = ungfu\,F\,urious5$, $\beta = O_w\,o\,gway$.

```text
K  -> Ow o gway K'
K' -> ungfu P anda K' | ungfu F urious5 K' | eps
```

**$i = 2$, $F$.** Every alternative of $F$ starts with $K$; replace $K$ by its (new) production $K \to O_w\,o\,gway\,K'$. No immediate recursion remains.

```text
F -> Ow o gway K' F T | Ow o gway K' F M | Ow o gway K' F Ma
   | Ow o gway K' F V | Ow o gway K' F C
```

**$i = 3$, $O_w$.** Replace the leading $K$ in $O_w \to K F masterofmaster$ and the leading $F$ in $O_w \to F K shifumaster$ (five alternatives, one for each production of $F$). Now the alternatives of $O_w$ that start with $O_w$ are $\alpha$-parts, and the only $\beta$ is $warrior\,K\,F$:

```text
Ow  -> warrior K F Ow'
Ow' -> o gway K' F masterofmaster Ow'
     | o gway K' F T  K shifumaster Ow'
     | o gway K' F M  K shifumaster Ow'
     | o gway K' F Ma K shifumaster Ow'
     | o gway K' F V  K shifumaster Ow'
     | o gway K' F C  K shifumaster Ow'
     | dragon K F Ow'
     | eps
```

**$P$ and $T$** have only immediate recursion with an $\epsilon$ alternative as $\beta$:

```text
P  -> P'          P' -> o P'      | eps
T  -> T'          T' -> igress T' | eps
```

**$M \to M\,onkey$** has **no non-recursive alternative** ($\beta$ is missing), so $M$ derives no string; the result is $M \to \;$(nothing) and $M' \to onkey\,M' \mid \epsilon$ is unreachable. $M_a \to f\,M_a\,antis$, $V \to f\,V\,iper$, $C \to f\,C\,rane$ are not left-recursive (they start with the terminal $f$) and remain unchanged; like $M$ they never terminate, so the alternatives of $F$ that use $M, M_a, V, C$ are useless.

**Resulting grammar (no left recursion, useless symbols kept):**

```text
K   -> Ow o gway K'
K'  -> ungfu P anda K' | ungfu F urious5 K' | eps
F   -> Ow o gway K' F T | Ow o gway K' F M | Ow o gway K' F Ma | Ow o gway K' F V | Ow o gway K' F C
Ow  -> warrior K F Ow'
Ow' -> o gway K' F masterofmaster Ow' | o gway K' F T K shifumaster Ow' | o gway K' F M K shifumaster Ow'
     | o gway K' F Ma K shifumaster Ow' | o gway K' F V K shifumaster Ow' | o gway K' F C K shifumaster Ow'
     | dragon K F Ow' | eps
P   -> P'             P' -> o P' | eps
T   -> T'             T' -> igress T' | eps
Ma  -> f Ma antis     V  -> f V iper      C -> f C rane
```

If the useless nonterminals $M, M_a, V, C$ are also removed, only the $T$-alternative of $F$ survives: $F \to O_w\,o\,gway\,K'\,F\,T$, and $O_w'$ keeps $o\,gway\,K'\,F\,masterofmaster\,O_w'$, $o\,gway\,K'\,F\,T\,K\,shifumaster\,O_w'$, $dragon\,K\,F\,O_w'$ and $\epsilon$.

*Check:* the algorithm was run by a script on this grammar and produced exactly the productions above.
