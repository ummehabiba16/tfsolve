# Writing content that renders well: rules and known fixes

Question and solution files must look right in **two** places: on GitHub (its Markdown with `$math$`) and in the PDF (Pandoc → LaTeX). Follow these rules while writing, and use the fixes when `tfsolve lint` or `tfsolve check` reports a problem.

## Rules

| Element | Write it like this | Why |
|---|---|---|
| Inline math | `$T = 10\text{ ms}$`: no space right after the opening `$` or before the closing `$` | Otherwise it is not recognised as math |
| Math followed by a digit | `$\times$ 3` or `$5\times3$`, **never** `$\times$3` | `$` immediately followed by a digit breaks math parsing |
| Display math | on its own line with a blank line before and after: `$$D=\frac{F}{1-F}R\,T$$` | GitHub renders `$$` only as a separate line |
| Long formulas | at most one relation or about 60 visible characters per `$$` line; split `A = B, C = D, E = F` into several `$$` lines | Display math cannot wrap and runs off the page |
| Lists `(i) (ii)` / `(a) (b)` / `i. ii.` | each item its own paragraph, blank line between, **no indentation**; nested sub-items also start at the left margin | GitHub shows 4-space-indented lines as a code block |
| Bullets / numbered steps | `- item` / `1. step`, blank line before the list | Pandoc needs the blank line |
| Tables | pipe tables with a header row: `\| Process \| A \| B \|` then `\|:--\|:-:\|:-:\|`. A table with no natural header gets one (`\| Parameter \| Value \|`) | The PDF converts only pipe tables; HTML tables are dropped |
| Merged cells (multicolumn) | not possible; repeat or restructure the header (`Frame 1 \| Frame 2 ...`) and add an italic caption line below | Pipe tables have no colspan |
| Wide tables (7+ columns) | fine; the PDF shrinks them to fit. Keep cells short (`5 read, 6 write`) | Long cells make the shrunken text tiny |
| Code / pseudocode / shell commands | fenced block with a language: ```` ```c ````, ```` ```text ```` | Keeps spacing; long lines wrap in the PDF; a real language (`c`, `python`, `bash`, ...) gets syntax colours on the site and in the PDF, `text` stays plain |
| Two code blocks side by side | one after the other, each under a bold label (`**Code block 1**`) | Tables cannot hold code |
| Diagrams in solutions (state diagrams, trees, memory maps, networks, flows) | a TikZ figure: `figures/<name>.tex` plus its rendered `figures/<name>.png`, linked as `![description](figures/<name>.png)`; see "Diagrams as TikZ figures" below. Never an ASCII drawing in a ```` ```text ```` block, and never a huge `\underbrace` formula | ASCII art breaks in proportional fonts and on phones; formulas cannot wrap |
| Gantt charts | ```` ```gantt ```` block: optional `# caption`, then one `P1 0 30` per line | Drawn as TikZ in the PDF, readable as text on GitHub |
| Figures from the scan | `![Figure for Q5(b)](figures/q5b-1.png)` with the PNG saved next to the part | Missing files fail lint |
| Special symbols in text (→ ✓ ≤ × ⟹) | use math: `$\to$`, `$\checkmark$`, `$\le$`, `$\times$`, `$\Rightarrow$`; plain `--` and quotes are fine | The PDF font has no glyph for many Unicode symbols |
| Quotes and file names | straight quotes, and code spans for names: `` `/foo/bar` `` | Avoids curly quotes inside code |
| Headings (`#`) | never inside question or solution files; use a bold lead-in (`**(ii) Performance.**`) | They would break the PDF's table of contents |
| Raw LaTeX | avoid (`\begin{tabular}`, `\hspace`, `\newline`). Forbidden: `\input`, `\include`, `\write`, `\def`, `\usepackage`, and anything else lint blocks | Not rendered by GitHub; security |

## Diagrams as TikZ figures

**When to draw one.** Whenever the question asks for a diagram, and whenever a solution defines a Markov chain or a queue (states, transitions, balance equations): the state or rate diagram is the expected answer. Also for recursion trees, memory maps, queueing networks and similar structures. Keep a transition table or matrix next to the figure if the solution has one; the figure does not replace it.

**Files.** Put the source and the image next to the solution: `solutions/q5a/figures/states.tex` and `states.png`, with short names (`states`, `chain`, `tree`, `network`). A question repeated in another exam gets its own copy of both files. Write the source as a standalone document:

```latex
\documentclass[border=6pt]{standalone}
\usepackage{amsmath}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\begin{document}
\begin{tikzpicture}[>=Stealth,font=\small,
 s/.style={draw,thick,circle,minimum size=1.1cm,inner sep=0pt,fill=blue!8},
 e/.style={->,thick},
 lab/.style={font=\small,fill=white,inner sep=1.5pt},
 every loop/.style={->,thick,looseness=6}]
\node[s] (0) at (0,0) {$0$};
\node[s] (1) at (2.4,0) {$1$};
\draw[e] (0) to[bend left=30] node[lab]{$\lambda$} (1);
\draw[e] (1) to[bend left=30] node[lab]{$\mu$} (0);
\node[font=\scriptsize] at (1.2,-1.2) {state = number of customers in the system};
\end{tikzpicture}
\end{document}
```

Style: states are circles (`fill=blue!8`, with `orange!15` for a special group such as blocked or busy states), boxes are `rounded corners`, labels sit on the arrow with a white background, `\tfrac` for probabilities, `edge[loop above]` for self-loops, and one or two `\scriptsize` caption lines below the drawing to explain the state notation. Keep a figure at most about 15 cm wide: break long captions into several lines, because a wide figure is shrunk to the text width in the PDF.

**Render the PNG** (200 dpi, the same as the other figures) from the repository root:

```bash
f=bank/CSE/CSE301/2025-09/solutions/q5b/figures/states.tex; d=$(mktemp -d); cp "$f" "$d/f.tex" && (cd "$d" && pdflatex -interaction=nonstopmode -halt-on-error f.tex >/dev/null) && .venv/bin/python -c "import pymupdf,sys; pymupdf.open(sys.argv[1])[0].get_pixmap(dpi=200).save(sys.argv[2])" "$d/f.pdf" "${f%.tex}.png" || grep -A2 '^!' "$d/f.log"
```

**Link it** in the solution as its own paragraph: `![State diagram: (0,0) to (1,0) at lambda, ...](figures/states.png)`. Write the alt text in plain words without `$` (it is what GitHub shows if the image fails and what screen readers read), and describe what the figure shows. If you add or replace a figure in an existing solution, add a dated `changes:` line, e.g. `"2026-10-12: added a TikZ state diagram (answer unchanged)"`.

**Check before you finish.** Open the PNG and compare it with the solution arrow by arrow: every transition in the table or matrix is drawn once, in the right direction, with the right rate or probability, and nothing extra is drawn. Recompute any numbers shown in the figure (tree node values, traffic-equation rates) rather than copying them. Look for labels that overlap arrows or each other. Then run `tfsolve check`.

## Known problems and fixes

| Reported as | Fix |
|---|---|
| `raw HTML; use a pipe table` | Rewrite the `<table>` as a pipe table (see the merged-cells rule); remove `<br>` and `` `<!-- -->`{=html} `` |
| `indented 4+ spaces` | Move the line to the left margin; keep a blank line between items |
| `put display math $$...$$ on its own line` | Break the paragraph: blank line, `$$...$$`, blank line, rest of the text |
| `very long display equation` / `layout: ... NNpt too wide` inside math | Split the formula into several `$$` lines, one relation each |
| `layout: ... too wide` in a table | Shorten cell text, move long explanations below the table, or split the table |
| `layout: ... too wide` in text | A long unbroken token (URL, long code in backticks): break it or put it in a code block |
| `the font has no glyph for 'X'` | Replace the symbol with LaTeX math or ASCII (see the symbols rule) |
| `image not found` | Save the crop at that path or fix the path; for a TikZ figure, render the `.tex` to `.png` (see above) |
| TikZ: `Undefined control sequence` at `\tfrac` | Add `\usepackage{amsmath}` to the figure's preamble |
| TikZ: `\\` line breaks vanish, or `$` missing | The `.tex` was written through an unquoted shell heredoc; write the file with a quoted heredoc (`<<'EOF'`) or an editor |
| TikZ: a figure looks tiny in the PDF | It is too wide; split the caption into lines, shorten labels or tighten the node spacing |
| `a code block is never closed` | Add the closing ```` ``` ```` line |
| `unknown topic 'x' (did you mean y?)` | Use the suggested id, or add the topic to `course.yaml` (after asking the user) |
| `question N is not listed in any section` | Add the question number to the right section in `paper.yaml` |
| `folder is YYYY-MM but exam_date is ...` | Rename the folder to the exam month |
| PDF looks wrong but check is OK (e.g. a list shows as one paragraph) | Compare with an existing file that renders well, and add the missing blank lines |
