---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "As an SDT (postfix: every action at the end of its body) it works bottom-up, but not top-down, because N -> N , num is left recursive. Eliminating left recursion with inherited attributes gives: N -> num { R.icnt = 1; R.imax = num.val; R.imaxi = 0; R.igt = (num.val > 0) } R { N.maxi = R.smaxi; N.gt = R.sgt }; R -> , num { i = R.icnt; R1.icnt = i + 1; R1.imax, R1.imaxi updated if num.val > R.imax; R1.igt = R.igt + (num.val > i) } R1 { R.smaxi = R1.smaxi; R.sgt = R1.sgt }; R -> eps { R.smaxi = R.imaxi; R.sgt = R.igt }."
sources: ["KMS Chapter 5 slides 48-55, 62-69 (SDT, Postfix SDT, Eliminating Left Recursion from SDTs)", "Dragon book 2e sec. 5.4.1, 5.4.4"]
---
**SDT (postfix).** The SDD is S-attributed, so each rule becomes an action at the right end of its production:

```text
L -> '{' N '}'    { print(N.maxi); print(N.gt); }
N -> num          { N.cnt = 1; N.max = num.val; N.maxi = 0;
                    N.gt = (num.val > 0) ? 1 : 0; }
N -> N1 ',' num   { i = N1.cnt;  N.cnt = i + 1;
                    if (num.val > N1.max) { N.max = num.val; N.maxi = i; }
                    else { N.max = N1.max; N.maxi = N1.maxi; }
                    N.gt = N1.gt + ((num.val > i) ? 1 : 0); }
```

**Can it be implemented during top-down parsing? No.** The production $N \to N_1\ ','\ \textbf{num}$ is **left recursive**, so a predictive (top-down) parser would loop forever. It also could not choose between the two $N$-productions, since both start with **num**. (It is fine for bottom-up LR parsing, where postfix actions run at the reductions.)

**Transformation for top-down parsing.** Eliminate the left recursion ($N \to N\alpha \mid \beta$ becomes $N \to \beta R$, $R \to \alpha R \mid \epsilon$). The values accumulated so far are passed *down* the list as **inherited** attributes of $R$ (prefix `i`), and the final results come back *up* as **synthesized** attributes (prefix `s`):

```text
L -> '{' N '}'    { print(N.maxi); print(N.gt); }

N -> num          { R.icnt = 1;  R.imax = num.val;  R.imaxi = 0;
                    R.igt = (num.val > 0) ? 1 : 0; }
     R            { N.maxi = R.smaxi;  N.gt = R.sgt; }

R -> ',' num      { i = R.icnt;  R1.icnt = i + 1;
                    if (num.val > R.imax) { R1.imax = num.val; R1.imaxi = i; }
                    else { R1.imax = R.imax; R1.imaxi = R.imaxi; }
                    R1.igt = R.igt + ((num.val > i) ? 1 : 0); }
     R1           { R.smaxi = R1.smaxi;  R.sgt = R1.sgt; }

R -> eps          { R.smaxi = R.imaxi;  R.sgt = R.igt; }
```

- Each action computing inherited attributes of $R$ or $R_1$ is placed **before** that symbol.
- Each action computing synthesized attributes is placed at the **end**.

The SDT is L-attributed, and the grammar is LL(1): $R$ chooses `,` or $\epsilon$ on lookahead `}`. So it can be executed during top-down (recursive-descent) parsing. For {3, 6, 1, 2, 5}, the inherited values go 1/3/0/1, then 2/6/1/2, then 3/6/1/2, 4/6/1/2, 5/6/1/3 (cnt/max/maxi/gt), and $R \to \epsilon$ returns maxi = 1, gt = 3.
