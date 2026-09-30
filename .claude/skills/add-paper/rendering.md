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
| Code / pseudocode / shell commands | fenced block with a language: ```` ```c ````, ```` ```text ```` | Keeps spacing; long lines wrap in the PDF |
| Two code blocks side by side | one after the other, each under a bold label (`**Code block 1**`) | Tables cannot hold code |
| Diagrams (RPC flow, disk layout, trees) | a ```` ```text ```` block with an ASCII drawing, or a table; never a huge `\underbrace` formula | Formulas cannot wrap |
| Gantt charts | ```` ```gantt ```` block: optional `# caption`, then one `P1 0 30` per line | Drawn as TikZ in the PDF, readable as text on GitHub |
| Figures from the scan | `![Figure for Q5(b)](figures/q5b-1.png)` with the PNG saved next to the part | Missing files fail lint |
| Special symbols in text (→ ✓ ≤ × ⟹) | use math: `$\to$`, `$\checkmark$`, `$\le$`, `$\times$`, `$\Rightarrow$`; plain `--` and quotes are fine | The PDF font has no glyph for many Unicode symbols |
| Quotes and file names | straight quotes, and code spans for names: `` `/foo/bar` `` | Avoids curly quotes inside code |
| Headings (`#`) | never inside question or solution files; use a bold lead-in (`**(ii) Performance.**`) | They would break the PDF's table of contents |
| Raw LaTeX | avoid (`\begin{tabular}`, `\hspace`, `\newline`). Forbidden: `\input`, `\include`, `\write`, `\def`, `\usepackage`, and anything else lint blocks | Not rendered by GitHub; security |

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
| `image not found` | Save the crop at that path or fix the path |
| `a code block is never closed` | Add the closing ```` ``` ```` line |
| `unknown topic 'x' (did you mean y?)` | Use the suggested id, or add the topic to `course.yaml` (after asking the user) |
| `question N is not listed in any section` | Add the question number to the right section in `paper.yaml` |
| `folder is YYYY-MM but exam_date is ...` | Rename the folder to the exam month |
| PDF looks wrong but check is OK (e.g. a list shows as one paragraph) | Compare with an existing file that renders well, and add the missing blank lines |
